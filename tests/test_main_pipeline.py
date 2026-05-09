import tempfile
from datetime import datetime, timedelta
from unittest.mock import Mock, patch

from main import run_once
from src.digest_cache import DigestCache
from src.rss_fetcher import Article
from src.summarizer import ArticleSummary


def _write_config(cache_path):
    config_file = tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8')
    config_file.write(f"""
rss_sources:
  - name: "Source"
    url: "https://example.com/rss"
    category: "Other"
claude:
  api_key: "test-key"
  base_url: ""
  model: "test-model"
digest:
  recent_days: 3
  cache_path: "{cache_path.replace(chr(92), "/")}"
  classification_batch_size: 30
output:
  base_dir: "."
schedule:
  days: []
  time: "09:00"
""")
    config_file.close()
    return config_file.name


def test_run_once_skips_articles_older_than_recent_days():
    with tempfile.NamedTemporaryFile(delete=False) as cache_file:
        cache_path = cache_file.name
    config_path = _write_config(cache_path)
    old_article = Article(
        title="Old",
        url="https://example.com/old",
        published=datetime.now() - timedelta(days=4),
        source="Source",
        content="Old content"
    )

    with patch("main.RSSFetcher") as mock_fetcher_cls, \
         patch("main.Summarizer") as mock_summarizer_cls, \
         patch("main.TrendSummarizer"), \
         patch("main.MarkdownWriter") as mock_writer_cls:
        mock_fetcher_cls.return_value.fetch.return_value = [old_article]
        mock_writer_cls.return_value.write_all.return_value = "out.md"

        run_once(config_path)

    mock_summarizer_cls.return_value.classify_batch.assert_not_called()
    mock_summarizer_cls.return_value.classify_only.assert_not_called()
    mock_summarizer_cls.return_value.summarize.assert_not_called()


def test_run_once_reuses_cached_category_and_summary():
    with tempfile.NamedTemporaryFile(delete=False) as cache_file:
        cache_path = cache_file.name
    config_path = _write_config(cache_path)
    article = Article(
        title="Cached",
        url="https://example.com/cached",
        published=datetime.now(),
        source="Source",
        content="Cached content"
    )
    cached_summary = ArticleSummary(
        title="Cached",
        url="https://example.com/cached",
        source="Source",
        summary="Cached summary",
        key_points=["Point"],
    )
    cache = DigestCache(cache_path)
    cache.set_category(article.url, article.source, article.title, "AIGC视觉生成")
    cache.set_summary(cached_summary)

    with patch("main.RSSFetcher") as mock_fetcher_cls, \
         patch("main.Summarizer") as mock_summarizer_cls, \
         patch("main.TrendSummarizer") as mock_trend_cls, \
         patch("main.MarkdownWriter") as mock_writer_cls:
        mock_fetcher_cls.return_value.fetch.return_value = [article]
        mock_trend_cls.return_value.summarize_trends.return_value = Mock(
            category_name="AIGC视觉生成",
            summary_text="Trend",
            key_trends=[]
        )
        mock_writer_cls.return_value.write_all.return_value = "out.md"

        run_once(config_path)

    mock_summarizer_cls.return_value.classify_batch.assert_not_called()
    mock_summarizer_cls.return_value.classify_only.assert_not_called()
    mock_summarizer_cls.return_value.summarize.assert_not_called()
    written_articles = mock_writer_cls.return_value.write_all.call_args.args[0]
    assert written_articles["AIGC视觉生成"][0].summary == "Cached summary"
