"""
Render HTML from cache without fetching/classifying/summarizing.
For rapid UI iteration: edit html_writer.py CSS/HTML/JS → run render.py → refresh browser.

Usage:
    python render.py --config config/ai_digest/config_ai_digest_outer_rss_merge_v0.yaml
    python render.py --config config/ai_digest/xxx.yaml --with-trends   # include trend cards (LLM)
"""
import argparse
import importlib
import logging
from datetime import datetime
from pathlib import Path

from src.config_loader import ConfigLoader, SUBTYPE_TECH, SUBTYPE_PRODUCT
from src.digest_cache import DigestCache
from src.html_writer import HTMLWriter
from src.summarizer import ArticleSummary, TrendSummarizer, TrendSummary

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def render(config_path: str, with_trends: bool = False):
    loader = ConfigLoader(config_path)
    config = loader.load()
    prompts = importlib.import_module(f"src.{config.digest.prompts_module}")
    CATEGORIES_TO_OUTPUT = prompts.CATEGORIES_TO_OUTPUT

    cache = DigestCache(config.digest.cache_path)
    source_subtype_map = {s.name: s.subtype for s in config.rss_sources}

    articles_by_category = {cat: {SUBTYPE_TECH: [], SUBTYPE_PRODUCT: []} for cat in CATEGORIES_TO_OUTPUT}
    total = 0

    for key, entry in cache._data.get("articles", {}).items():
        category = entry.get("category", "")
        if category not in CATEGORIES_TO_OUTPUT:
            continue

        summary_text = entry.get("summary", "")
        if not summary_text:
            continue

        subtype = entry.get("subtype", "")
        if not subtype:
            for s in config.rss_sources:
                if s.name == entry.get("source", ""):
                    subtype = s.subtype
                    break
        if not subtype:
            subtype = SUBTYPE_PRODUCT

        article = ArticleSummary(
            title=entry.get("title", ""),
            url=entry.get("url", ""),
            source=entry.get("source", ""),
            summary=summary_text,
            key_points=entry.get("key_points", []),
            arxiv_url=entry.get("arxiv_url", ""),
            github_url=entry.get("github_url", ""),
            subtype=subtype,
        )
        articles_by_category[category][subtype].append(article)
        total += 1

    logger.info(f"Loaded {total} summaries from cache")

    # Trends
    trends_by_category = {}
    if with_trends:
        trend_summarizer = TrendSummarizer(config.claude, prompts=prompts)
        for category, subtypes in articles_by_category.items():
            all_articles = subtypes.get(SUBTYPE_TECH, []) + subtypes.get(SUBTYPE_PRODUCT, [])
            if all_articles:
                try:
                    logger.info(f"Trend: {category} ({len(all_articles)} articles)")
                    trends_by_category[category] = trend_summarizer.summarize_trends(category, all_articles)
                except Exception as e:
                    logger.error(f"Trend failed {category}: {e}")
                    trends_by_category[category] = TrendSummary(
                        category_name=category,
                        summary_text="",
                        key_trends=[]
                    )

    generated_at = datetime.now()
    category_counts = {cat: sum(len(v) for v in subtypes.values()) for cat, subtypes in articles_by_category.items()}

    stats = {
        "generated_at": generated_at,
        "articles_seen": total,
        "articles_recent": total,
        "articles_summarized": total,
        "categories": category_counts,
        "token_total": 0,
        "llm_time": 0,
        "config_path": config_path,
    }

    html_writer = HTMLWriter(config.output.base_dir)
    html_path = html_writer.write_all(articles_by_category, trends_by_category, generated_at, stats)
    logger.info(f"Rendered: {html_path}")
    return html_path


def main():
    parser = argparse.ArgumentParser(description="Render HTML from cache (no LLM calls)")
    parser.add_argument("--config", default="config.yaml", help="Config file path")
    parser.add_argument("--with-trends", action="store_true", help="Include trend summaries (LLM calls)")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        logger.error(f"Config file does not exist: {config_path}")
        return

    render(str(config_path), with_trends=args.with_trends)


if __name__ == "__main__":
    main()
