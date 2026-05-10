# main.py
import importlib
import sys
import argparse
import logging
from datetime import datetime, timedelta
from pathlib import Path

from src.config_loader import ConfigLoader, SUBTYPE_TECH, SUBTYPE_PRODUCT
from src.digest_cache import DigestCache
from src.rss_fetcher import RSSFetcher
from src.custom_fetcher import register_all
from src.summarizer import Summarizer, TrendSummarizer, TrendSummary
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

    articles_by_category = {cat: {SUBTYPE_TECH: [], SUBTYPE_PRODUCT: []} for cat in CATEGORIES_TO_OUTPUT}
    cutoff = datetime.now() - timedelta(days=config.digest.recent_days)
    candidates = []
    pending_classification = []
    categories_by_index = {}
    subtypes_by_index = {}
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
                index = len(candidates)
                candidates.append(article)

                cached_category = cache.get_category(article.url, article.source, article.title)
                if cached_category:
                    categories_by_index[index] = cached_category
                    cached_subtype = cache.get_subtype(article.url, article.source, article.title)
                    subtypes_by_index[index] = cached_subtype or source_subtype_map.get(source.name, SUBTYPE_PRODUCT)
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
            subtypes_by_index[idx] = final_subtype
            cache.set_category(article.url, article.source, article.title, category, final_subtype)

    # Phase 2: separate cached vs pending articles
    pending_summarization = []
    for index, article in enumerate(candidates):
        category = categories_by_index.get(index, "")
        try:
            if category in CATEGORIES_TO_OUTPUT:
                subtype = subtypes_by_index.get(index) or source_subtype_map.get(article.source, SUBTYPE_PRODUCT)
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
            else:
                logger.info(f"  skipped {category}: {article.title}")
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
            all_articles = subtypes.get(SUBTYPE_TECH, []) + subtypes.get(SUBTYPE_PRODUCT, [])
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
        md_path = writer.write_all(articles_by_category, trends_by_category, generated_at)
        stats["file_size"] = Path(md_path).stat().st_size
        writer.update_readme(md_path, stats)
        logger.info(f"Wrote digest (md): {md_path}")

    # HTML output
    if output_format in ("html", "both"):
        html_writer = HTMLWriter(config.output.base_dir)
        html_path = html_writer.write_all(articles_by_category, trends_by_category, generated_at, stats)
        stats["file_size"] = Path(html_path).stat().st_size
        html_writer.update_readme(html_path, stats)
        logger.info(f"Wrote digest (html): {html_path}")

    logger.info("Done")


def main():
    parser = argparse.ArgumentParser(description='DigestMe — RSS digest generator')
    parser.add_argument('--config', default='config.yaml', help='Config file path')
    parser.add_argument('--once', action='store_true', help='Run once without scheduler')
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        logger.error(f"Config file does not exist: {config_path}")
        sys.exit(1)

    if args.once:
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
