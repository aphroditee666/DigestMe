# main.py
import importlib
import os
import sys
import argparse
import logging
from datetime import datetime, timedelta
from pathlib import Path

from src.config_loader import ConfigLoader, SUBTYPE_TECH, SUBTYPE_PRODUCT, SUBTYPE_ACADEMIC
from src.digest_cache import DigestCache
from src.rss_fetcher import RSSFetcher
from src.custom_fetcher import register_all
from src.summarizer import Summarizer, TrendSummarizer, TrendSummary, ArticleSummary
from src.markdown_writer import MarkdownWriter
from src.html_writer import HTMLWriter
from src.scheduler import Scheduler
from src.full_text_fetcher import FullTextFetcher

# Register custom fetchers for sources without standard RSS feeds
register_all()


def _load_prompts(module_name: str):
    """Dynamically import a prompts module by name, e.g. 'prompts_ai_digest' → src.prompts_ai_digest."""
    return importlib.import_module(f"src.{module_name}")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def _normalize_datetime(dt):
    if dt and dt.tzinfo is not None and dt.utcoffset() is not None:
        return dt.replace(tzinfo=None)
    return dt


def _is_recent_enough(published, cutoff: datetime) -> bool:
    if published is None:
        return True
    published = _normalize_datetime(published)
    return published >= cutoff


def _chunks(items, size: int):
    size = max(size, 1)
    for start in range(0, len(items), size):
        yield items[start:start + size]


ACADEMIC_ELIGIBLE_CATEGORIES = {"AIGC视觉生成", "自动驾驶"}


def _apply_reclassification(summarizer, summary, old_category: str, title: str, categories_to_output: list, is_academic: bool = False):
    """Compare LLM's verified category against the original. Returns new category or None (filter out)."""
    vc = summary.verified_category
    if not vc or vc == old_category:
        return old_category
    normalized = summarizer._normalize_category(vc)
    if normalized == "其它" or normalized not in categories_to_output:
        logger.info(f"  filtered by reclassification: {title} ({vc})")
        return None
    if is_academic and normalized not in ACADEMIC_ELIGIBLE_CATEGORIES:
        logger.info(f"  filtered by reclassification (academic): {title} ({vc})")
        return None
    logger.info(f"  reclassified: {title} {old_category} → {normalized}")
    return normalized


def _init_articles_by_category(categories):
    """Return {category: {subtype: []}} with 3 subtypes for academic-eligible categories, 2 for others."""
    result = {}
    for cat in categories:
        if cat in ACADEMIC_ELIGIBLE_CATEGORIES:
            result[cat] = {SUBTYPE_ACADEMIC: [], SUBTYPE_TECH: [], SUBTYPE_PRODUCT: []}
        else:
            result[cat] = {SUBTYPE_TECH: [], SUBTYPE_PRODUCT: []}
    return result


def _classify_pending(summarizer: Summarizer, pending: list, batch_size: int) -> dict:
    """Classify pending articles in batches. Returns {index: {"category": str, "subtype": str}}."""
    results = {}
    for batch in _chunks(pending, batch_size):
        items = [
            {"index": item["index"], "title": item["article"].title, "source": item["article"].source}
            for item in batch
        ]
        try:
            results.update(summarizer.classify_batch(items))
        except Exception as e:
            logger.warning(f"Batch classification failed, falling back to single calls: {e}")
            for item in batch:
                article = item["article"]
                results[item["index"]] = {
                    "category": summarizer.classify_only(article.title, article.source),
                    "subtype": ""  # empty → backfill from source default in caller
                }
    return results


def _compute_digest_index(base_dir: str, date_str: str) -> int:
    """Return the next available index across .md and .html (0 = no suffix)."""
    prefix = f"{date_str}-digest"
    max_idx = -1
    if not os.path.isdir(base_dir):
        return 0
    for fname in os.listdir(base_dir):
        if not fname.startswith(prefix):
            continue
        if not (fname.endswith('.md') or fname.endswith('.html')):
            continue
        stem = fname[len(prefix):]
        for ext in ('.md', '.html'):
            if stem.endswith(ext):
                stem = stem[:-len(ext)]
                break
        if stem == '':
            max_idx = max(max_idx, 0)
        elif stem.startswith('-'):
            try:
                max_idx = max(max_idx, int(stem[1:]))
            except ValueError:
                pass
    return max_idx + 1


def run_once(config_path: str):
    loader = ConfigLoader(config_path)
    config = loader.load()

    prompts = _load_prompts(config.digest.prompts_module)
    CATEGORIES_TO_OUTPUT = prompts.CATEGORIES_TO_OUTPUT

    logger.info(f"Fetching {len(config.rss_sources)} RSS sources")

    fetcher = RSSFetcher()
    summarizer = Summarizer(config.claude, prompts=prompts)
    writer = MarkdownWriter(config.output.base_dir)
    cache = DigestCache(config.digest.cache_path)
    source_enrich_map = {s.name: s.enrich for s in config.rss_sources}
    source_subtype_map = {s.name: s.subtype for s in config.rss_sources}
    academic_source_names = {s.name for s in config.rss_sources if s.category == "学术论文"}

    articles_by_category = _init_articles_by_category(CATEGORIES_TO_OUTPUT)
    cutoff = datetime.now() - timedelta(days=config.digest.recent_days)
    candidates = []
    pending_classification = []
    categories_by_index = {}
    subtypes_by_index = {}
    seen_urls = set()
    total_seen = 0
    total_recent = 0
    total_summarized = 0

    for source in config.rss_sources:
        try:
            logger.info(f"Fetching: {source.name}")
            articles = fetcher.fetch(source.name, source.url, limit=source.limit)

            for article in articles:
                total_seen += 1
                if not _is_recent_enough(article.published, cutoff):
                    logger.info(f"  old article skipped: {article.title}")
                    continue

                total_recent += 1
                if article.url in seen_urls:
                    logger.info(f"  duplicate skipped: {article.title}")
                    continue
                seen_urls.add(article.url)
                index = len(candidates)
                candidates.append(article)

                cached_category = cache.get_category(article.url, article.source, article.title)
                if cached_category:
                    categories_by_index[index] = cached_category
                    cached_subtype = cache.get_subtype(article.url, article.source, article.title)
                    default_subtype = source_subtype_map.get(source.name, SUBTYPE_PRODUCT)
                    subtype = cached_subtype or default_subtype
                    if source.name in academic_source_names:
                        subtype = SUBTYPE_ACADEMIC
                    subtypes_by_index[index] = subtype
                else:
                    pending_classification.append({"index": index, "article": article})

        except Exception as e:
            logger.error(f"  failed to fetch source {source.name}: {e}")
            continue

    batch_results = _classify_pending(
        summarizer,
        pending_classification,
        config.digest.classification_batch_size
    )

    for item in pending_classification:
        idx = item["index"]
        article = item["article"]
        result = batch_results.get(idx, {})
        category = result.get("category", "")
        if category:
            categories_by_index[idx] = category
            llm_subtype = result.get("subtype", "")
            source_default = source_subtype_map.get(article.source, SUBTYPE_PRODUCT)
            final_subtype = llm_subtype or source_default
            if article.source in academic_source_names:
                final_subtype = SUBTYPE_ACADEMIC
            subtypes_by_index[idx] = final_subtype
            cache.set_category(article.url, article.source, article.title, category, final_subtype)

    # Phase 2: separate cached vs pending articles
    pending_summarization = []
    for index, article in enumerate(candidates):
        category = categories_by_index.get(index, "")
        is_academic = article.source in academic_source_names
        try:
            if is_academic:
                if category not in ("AIGC视觉生成", "自动驾驶"):
                    logger.info(f"  filtered academic {category}: {article.title}")
                    continue
            else:
                if category not in CATEGORIES_TO_OUTPUT:
                    logger.info(f"  filtered {category}: {article.title}")
                    continue

            subtype = subtypes_by_index.get(index) or source_subtype_map.get(article.source, SUBTYPE_PRODUCT)
            if article.source in academic_source_names:
                subtype = SUBTYPE_ACADEMIC
            cached_summary = cache.get_summary(article.url, article.source, article.title)
            if cached_summary:
                if not cached_summary.subtype:
                    cached_summary.subtype = subtype
                articles_by_category[category][cached_summary.subtype].append(cached_summary)
                total_summarized += 1
                logger.info(f"  cached {category}/{cached_summary.subtype}: {article.title}")
            else:
                pending_summarization.append({
                    "index": index,
                    "article": article,
                    "category": category,
                    "subtype": subtype
                })
        except Exception as e:
            logger.error(f"  failed to process article {article.title}: {e}")
            continue

    # Phase 2.5: enrich short content by fetching full article body from original URL
    if config.digest.enrich_content and pending_summarization:
        enricher = FullTextFetcher(min_content_length=config.digest.enrich_min_chars)
        for item in pending_summarization:
            article = item["article"]
            if source_enrich_map.get(article.source, True):
                item["article"] = enricher.enrich(article)

    # Phase 3: batch summarize pending articles
    if pending_summarization:
        batches = list(_chunks(pending_summarization, config.digest.summarization_batch_size))
        for batch in batches:
            try:
                batch_input = [
                    {
                        "index": item["index"],
                        "title": item["article"].title,
                        "source": item["article"].source,
                        "url": item["article"].url,
                        "content": item["article"].content
                    }
                    for item in batch
                ]
                summaries = summarizer.summarize_batch(batch_input)
                for item in batch:
                    idx = item["index"]
                    cat = item["category"]
                    subtype = item.get("subtype", SUBTYPE_PRODUCT)
                    if idx in summaries:
                        s = summaries[idx]
                        is_acad = item["article"].source in academic_source_names
                        new_cat = _apply_reclassification(summarizer, s, cat, item["article"].title, CATEGORIES_TO_OUTPUT, is_acad)
                        if new_cat is None:
                            continue
                        cat = new_cat
                        if is_acad:
                            subtype = SUBTYPE_ACADEMIC
                        s.subtype = subtype
                        cache.set_summary(s)
                        articles_by_category[cat][subtype].append(s)
                        total_summarized += 1
                        logger.info(f"  summarized {cat}/{subtype}: {item['article'].title}")
                    else:
                        logger.warning(f"  batch missing result, falling back to single: {item['article'].title}")
                        article = item["article"]
                        summary = summarizer.summarize(
                            title=article.title, source=article.source,
                            url=article.url, content=article.content,
                            subtype=subtype
                        )
                        is_acad = article.source in academic_source_names
                        new_cat = _apply_reclassification(summarizer, summary, cat, article.title, CATEGORIES_TO_OUTPUT, is_acad)
                        if new_cat is None:
                            continue
                        cat = new_cat
                        if is_acad:
                            subtype = SUBTYPE_ACADEMIC
                            summary.subtype = subtype
                        cache.set_summary(summary)
                        articles_by_category[cat][subtype].append(summary)
                        total_summarized += 1
            except Exception as e:
                logger.warning(f"Batch summarization failed, falling back to single: {e}")
                for item in batch:
                    try:
                        article = item["article"]
                        cat = item["category"]
                        subtype = item.get("subtype", SUBTYPE_PRODUCT)
                        summary = summarizer.summarize(
                            title=article.title, source=article.source,
                            url=article.url, content=article.content,
                            subtype=subtype
                        )
                        is_acad = article.source in academic_source_names
                        new_cat = _apply_reclassification(summarizer, summary, cat, article.title, CATEGORIES_TO_OUTPUT, is_acad)
                        if new_cat is None:
                            continue
                        cat = new_cat
                        if is_acad:
                            subtype = SUBTYPE_ACADEMIC
                            summary.subtype = subtype
                        cache.set_summary(summary)
                        articles_by_category[cat][subtype].append(summary)
                        total_summarized += 1
                        logger.info(f"  summarized {cat}/{subtype}: {article.title}")
                    except Exception as e2:
                        logger.error(f"  failed: {article.title}: {e2}")
                        continue

    logger.info(
        f"Seen {total_seen}, recent {total_recent}, summarized {total_summarized}, "
        f"skipped {total_recent - total_summarized}"
    )

    trend_summarizer = TrendSummarizer(config.claude, prompts=prompts) if config.digest.enable_trend_summary else None
    trends_by_category = {}
    if trend_summarizer:
        for category, subtypes in articles_by_category.items():
            all_articles = [a for articles in subtypes.values() for a in articles]
            if all_articles:
                try:
                    logger.info(f"Trend summary: {category} ({len(all_articles)} articles)")
                    trends_by_category[category] = trend_summarizer.summarize_trends(category, all_articles)
                except Exception as e:
                    logger.error(f"Trend summary failed: {category}, error: {e}")
                    trends_by_category[category] = TrendSummary(
                        category_name=category,
                        summary_text="Trend summary is temporarily unavailable.",
                        key_trends=[]
                    )

    generated_at = datetime.now()
    output_format = config.output.output_format
    date_str = generated_at.strftime("%Y-%m-%d")
    file_index = _compute_digest_index(config.output.base_dir, date_str)

    # Token & timing report
    s1 = summarizer.client.stats
    s2 = trend_summarizer.client.stats if trend_summarizer else None
    total_input = s1.input_tokens + (s2.input_tokens if s2 else 0)
    total_output = s1.output_tokens + (s2.output_tokens if s2 else 0)
    total_calls = s1.call_count + (s2.call_count if s2 else 0)
    total_time_s = (s1.total_time_ms + (s2.total_time_ms if s2 else 0)) / 1000.0
    logger.info(
        "=== Token & Time Report ==="
    )
    logger.info(
        f"  LLM calls: {total_calls} "
        f"(classify/summarize: {s1.call_count}, trend: {s2.call_count if s2 else 0})"
    )
    logger.info(
        f"  Input tokens:  {total_input:,}"
    )
    logger.info(
        f"  Output tokens: {total_output:,}"
    )
    logger.info(
        f"  Total tokens:  {total_input + total_output:,}"
    )
    logger.info(
        f"  LLM time:      {total_time_s:.1f}s"
    )

    # Build stats for writer calls
    category_counts = {cat: sum(len(v) for v in subtypes.values()) for cat, subtypes in articles_by_category.items()}
    stats = {
        "generated_at": generated_at,
        "articles_seen": total_seen,
        "articles_recent": total_recent,
        "articles_summarized": total_summarized,
        "categories": category_counts,
        "token_total": total_input + total_output,
        "llm_time": total_time_s,
        "config_path": config_path,
    }

    # Markdown output
    if output_format in ("markdown", "both"):
        md_path = writer.write_all(articles_by_category, trends_by_category, generated_at, file_index=file_index)
        stats["file_size"] = Path(md_path).stat().st_size
        writer.update_readme(md_path, stats)
        logger.info(f"Wrote digest (md): {md_path}")

    # HTML output
    if output_format in ("html", "both"):
        html_writer = HTMLWriter(config.output.base_dir, pages_url=config.output.pages_url)
        html_path = html_writer.write_all(articles_by_category, trends_by_category, generated_at, stats, file_index=file_index)
        stats["file_size"] = Path(html_path).stat().st_size
        html_writer.update_readme(html_path, stats)
        logger.info(f"Wrote digest (html): {html_path}")

    logger.info("Done")


def render_only(config_path: str):
    """Re-render HTML/MD from cache only — no fetching, no LLM calls."""
    loader = ConfigLoader(config_path)
    config = loader.load()

    prompts = _load_prompts(config.digest.prompts_module)
    CATEGORIES_TO_OUTPUT = prompts.CATEGORIES_TO_OUTPUT

    cache = DigestCache(config.digest.cache_path)
    source_subtype_map = {s.name: s.subtype for s in config.rss_sources}
    academic_source_names = {s.name for s in config.rss_sources if s.category == "学术论文"}

    articles_by_category = _init_articles_by_category(CATEGORIES_TO_OUTPUT)

    total_summarized = 0
    for key, entry in cache._data.get("articles", {}).items():
        summary_text = entry.get("summary")
        if not summary_text:
            continue
        category = entry.get("category", "")
        source = entry.get("source", "")
        is_academic = source in academic_source_names
        if is_academic:
            if category not in ("AIGC视觉生成", "自动驾驶"):
                continue
            subtype = SUBTYPE_ACADEMIC
        elif category not in CATEGORIES_TO_OUTPUT:
            continue
        else:
            subtype = entry.get("subtype") or source_subtype_map.get(source, SUBTYPE_PRODUCT)
        s = ArticleSummary(
            title=entry.get("title", ""),
            url=entry.get("url", ""),
            source=entry.get("source", ""),
            summary=summary_text,
            key_points=entry.get("key_points", []),
            arxiv_url=entry.get("arxiv_url", ""),
            github_url=entry.get("github_url", ""),
            subtype=subtype,
        )
        articles_by_category[category][subtype].append(s)
        total_summarized += 1

    logger.info(f"Loaded {total_summarized} cached summaries across {len(CATEGORIES_TO_OUTPUT)} categories")

    # Trend summaries — re-run LLM calls (articles may have changed)
    trend_summarizer = TrendSummarizer(config.claude, prompts=prompts) if config.digest.enable_trend_summary else None
    trends_by_category = {}
    if trend_summarizer:
        for category, subtypes in articles_by_category.items():
            all_articles = [a for articles in subtypes.values() for a in articles]
            if all_articles:
                try:
                    logger.info(f"Trend summary: {category} ({len(all_articles)} articles)")
                    trends_by_category[category] = trend_summarizer.summarize_trends(category, all_articles)
                except Exception as e:
                    logger.error(f"Trend summary failed: {category}: {e}")

    generated_at = datetime.now()
    output_format = config.output.output_format
    date_str = generated_at.strftime("%Y-%m-%d")
    file_index = _compute_digest_index(config.output.base_dir, date_str)

    category_counts = {cat: sum(len(v) for v in subtypes.values()) for cat, subtypes in articles_by_category.items()}
    stats = {
        "generated_at": generated_at,
        "articles_seen": total_summarized,
        "articles_recent": total_summarized,
        "articles_summarized": total_summarized,
        "categories": category_counts,
        "token_total": 0,
        "llm_time": 0,
        "config_path": config_path,
    }

    if output_format in ("markdown", "both"):
        writer = MarkdownWriter(config.output.base_dir)
        md_path = writer.write_all(articles_by_category, trends_by_category, generated_at, file_index=file_index)
        stats["file_size"] = Path(md_path).stat().st_size
        writer.update_readme(md_path, stats)
        logger.info(f"Wrote digest (md): {md_path}")

    if output_format in ("html", "both"):
        html_writer = HTMLWriter(config.output.base_dir, pages_url=config.output.pages_url)
        html_path = html_writer.write_all(articles_by_category, trends_by_category, generated_at, stats, file_index=file_index)
        stats["file_size"] = Path(html_path).stat().st_size
        html_writer.update_readme(html_path, stats)
        logger.info(f"Wrote digest (html): {html_path}")

    logger.info("Render done")


def main():
    parser = argparse.ArgumentParser(description='DigestMe — RSS digest generator')
    parser.add_argument('--config', default='config.yaml', help='Config file path')
    parser.add_argument('--once', action='store_true', help='Run once without scheduler')
    parser.add_argument('--render-only', action='store_true', help='Re-render HTML/MD from cache only (no fetch, no LLM)')
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        logger.error(f"Config file does not exist: {config_path}")
        sys.exit(1)

    if args.render_only:
        render_only(str(config_path))
    elif args.once:
        run_once(str(config_path))
    else:
        loader = ConfigLoader(str(config_path))
        config = loader.load()

        scheduler = Scheduler()
        scheduler.schedule_weekly(
            config.schedule.days,
            config.schedule.time,
            lambda: run_once(str(config_path))
        )

        logger.info(f"Scheduled weekly: {', '.join(config.schedule.days)} {config.schedule.time}")
        scheduler.run()


if __name__ == "__main__":
    main()
