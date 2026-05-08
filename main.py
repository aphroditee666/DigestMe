# main.py
import sys
import argparse
import logging
from datetime import datetime
from pathlib import Path

from src.config_loader import ConfigLoader
from src.rss_fetcher import RSSFetcher
from src.summarizer import Summarizer, TrendSummarizer, TrendSummary
from src.markdown_writer import MarkdownWriter
from src.scheduler import Scheduler

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

CATEGORIES_TO_OUTPUT = [
    "AIGC视觉生成",
    "多模态大模型/大语言模型",
    "自动驾驶",
    "小样本学习/强化学习"
]


def run_once(config_path: str):
    loader = ConfigLoader(config_path)
    config = loader.load()

    logger.info(f"开始抓取 {len(config.rss_sources)} 个 RSS 源")

    fetcher = RSSFetcher()
    summarizer = Summarizer(config.claude)
    writer = MarkdownWriter(config.output.base_dir)

    articles_by_category = {cat: [] for cat in CATEGORIES_TO_OUTPUT}
    total_classified = 0
    total_summarized = 0

    for source in config.rss_sources:
        try:
            logger.info(f"抓取: {source.name}")
            articles = fetcher.fetch(source.name, source.url)

            for article in articles:
                total_classified += 1
                try:
                    # Phase 1: Lightweight classification (no body content, tiny output)
                    category = summarizer.classify_only(
                        title=article.title,
                        source=article.source
                    )

                    if category in CATEGORIES_TO_OUTPUT:
                        logger.info(f"  ✓ {category}: {article.title}")
                        # Phase 2: Full summarization only for target categories
                        summary = summarizer.summarize(
                            title=article.title,
                            source=article.source,
                            url=article.url,
                            content=article.content
                        )
                        articles_by_category[category].append(summary)
                        total_summarized += 1
                    else:
                        logger.info(f"  — {category} (skip): {article.title}")

                except Exception as e:
                    logger.error(f"  处理文章失败: {article.title}, 错误: {e}")
                    continue

        except Exception as e:
            logger.error(f"  抓取源失败: {source.name}, 错误: {e}")
            continue

    logger.info(f"分类 {total_classified} 篇，摘要 {total_summarized} 篇，跳过 {total_classified - total_summarized} 篇")

    # Trend summarization (unchanged)
    trend_summarizer = TrendSummarizer(config.claude)
    trends_by_category = {}
    for category, articles in articles_by_category.items():
        if articles:
            try:
                logger.info(f"趋势总结: {category} ({len(articles)} 篇)")
                trend = trend_summarizer.summarize_trends(category, articles)
                trends_by_category[category] = trend
            except Exception as e:
                logger.error(f"趋势总结失败: {category}, 错误: {e}")
                trends_by_category[category] = TrendSummary(
                    category_name=category,
                    summary_text="本周趋势总结暂时无法生成。",
                    key_trends=[]
                )

    generated_at = datetime.now()
    output_path = writer.write_all(articles_by_category, trends_by_category, generated_at)
    logger.info(f"写入汇总文档: {output_path}")
    logger.info("完成")


def main():
    parser = argparse.ArgumentParser(description='微信公众号咨询汇总系统')
    parser.add_argument('--config', default='config.yaml', help='配置文件路径')
    parser.add_argument('--once', action='store_true', help='单次运行（不调度）')
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        logger.error(f"配置文件不存在: {config_path}")
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

        logger.info(f"调度已设置: 每周 {', '.join(config.schedule.days)} {config.schedule.time}")
        scheduler.run()


if __name__ == "__main__":
    main()
