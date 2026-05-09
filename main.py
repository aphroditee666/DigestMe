# main.py
import importlib
import sys
import argparse
import logging
from datetime import datetime, timedelta
from pathlib import Path

from src.config_loader import ConfigLoader
from src.digest_cache import DigestCache
from src.rss_fetcher import RSSFetcher
from src.summarizer import Summarizer, TrendSummarizer, TrendSummary
from src.markdown_writer import MarkdownWriter
from src.scheduler import Scheduler


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
    categories = {}
    for batch in _chunks(pending, batch_size):
        items = [
            {"index": item["index"], "title": item["article"].title, "source": item["article"].source}
            for item in batch
        ]
        try:
            categories.update(summarizer.classify_batch(items))
        except Exception as e:
            logger.warning(f"Batch classification failed, falling back to single calls: {e}")
            for item in batch:
                article = item["article"]
                categories[item["index"]] = summarizer.classify_only(article.title, article.source)
    return categories


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

    articles_by_category = {cat: [] for cat in CATEGORIES_TO_OUTPUT}
    cutoff = datetime.now() - timedelta(days=config.digest.recent_days)
    candidates = []
    pending_classification = []
    categories_by_index = {}
    total_seen = 0
    total_recent = 0
    total_summarized = 0

    for source in config.rss_sources:
        try:
            logger.info(f"Fetching: {source.name}")
            articles = fetcher.fetch(source.name, source.url)

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
                else:
                    pending_classification.append({"index": index, "article": article})

        except Exception as e:
            logger.error(f"  failed to fetch source {source.name}: {e}")
            continue

    batch_categories = _classify_pending(
        summarizer,
        pending_classification,
        config.digest.classification_batch_size
    )
    categories_by_index.update(batch_categories)

    for item in pending_classification:
        article = item["article"]
        category = categories_by_index.get(item["index"])
        if category:
            cache.set_category(article.url, article.source, article.title, category)

    for index, article in enumerate(candidates):
        category = categories_by_index.get(index, "")
        try:
            if category in CATEGORIES_TO_OUTPUT:
                cached_summary = cache.get_summary(article.url, article.source, article.title)
                if cached_summary:
                    summary = cached_summary
                else:
                    summary = summarizer.summarize(
                        title=article.title,
                        source=article.source,
                        url=article.url,
                        content=article.content
                    )
                    cache.set_summary(summary)
                articles_by_category[category].append(summary)
                total_summarized += 1
                logger.info(f"  summarized {category}: {article.title}")
            else:
                logger.info(f"  skipped {category}: {article.title}")
        except Exception as e:
            logger.error(f"  failed to process article {article.title}: {e}")
            continue

    logger.info(
        f"Seen {total_seen}, recent {total_recent}, summarized {total_summarized}, "
        f"skipped {total_recent - total_summarized}"
    )

    trend_summarizer = TrendSummarizer(config.claude, prompts=prompts) if config.digest.enable_trend_summary else None
    trends_by_category = {}
    if trend_summarizer:
        for category, articles in articles_by_category.items():
            if articles:
                try:
                    logger.info(f"Trend summary: {category} ({len(articles)} articles)")
                    trends_by_category[category] = trend_summarizer.summarize_trends(category, articles)
                except Exception as e:
                    logger.error(f"Trend summary failed: {category}, error: {e}")
                    trends_by_category[category] = TrendSummary(
                        category_name=category,
                        summary_text="Trend summary is temporarily unavailable.",
                        key_trends=[]
                    )

    generated_at = datetime.now()
    output_path = writer.write_all(articles_by_category, trends_by_category, generated_at)
    logger.info(f"Wrote digest: {output_path}")

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
