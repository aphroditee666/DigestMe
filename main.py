# main.py
import os
import sys
import argparse
import logging
from datetime import datetime
from pathlib import Path

from src.config_loader import ConfigLoader
from src.rss_fetcher import RSSFetcher
from src.content_filter import ContentFilter
from src.summarizer import Summarizer
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
    "其他AI/深度学习领域相关"
]

def run_once(config_path: str):
    loader = ConfigLoader(config_path)
    config = loader.load()

    logger.info(f"开始抓取 {len(config.rss_sources)} 个 RSS 源")

    fetcher = RSSFetcher()
    filter = ContentFilter(config.claude)
    summarizer = Summarizer(config.claude)
    writer = MarkdownWriter(config.output.base_dir)

    articles_by_category = {cat: [] for cat in CATEGORIES_TO_OUTPUT}

    for source in config.rss_sources:
        try:
            logger.info(f"抓取: {source.name}")
            articles = fetcher.fetch(source.name, source.url)

            for article in articles:
                try:
                    category = filter.classify(article.title, article.source)

                    if category in CATEGORIES_TO_OUTPUT:
                        logger.info(f"  分类为 {category}: {article.title}")

                        summary = summarizer.summarize(
                            title=article.title,
                            source=article.source,
                            url=article.url
                        )

                        articles_by_category[category].append(summary)
                    else:
                        logger.info(f"  跳过（{category}）: {article.title}")

                except Exception as e:
                    logger.error(f"  处理文章失败: {article.title}, 错误: {e}")
                    continue

        except Exception as e:
            logger.error(f"  抓取源失败: {source.name}, 错误: {e}")
            continue

    generated_at = datetime.now()
    for category, articles in articles_by_category.items():
        if articles:
            output_path = writer.write(category, articles, generated_at)
            logger.info(f"写入 {category} 文档: {output_path}")

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