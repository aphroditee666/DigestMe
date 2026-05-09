import os
import tempfile

from src.digest_cache import DigestCache
from src.summarizer import ArticleSummary


def test_cache_miss_returns_none():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        cache_path = f.name
    os.unlink(cache_path)

    cache = DigestCache(cache_path)

    assert cache.get_category("https://example.com/a", "Source", "Title") is None
    assert cache.get_summary("https://example.com/a", "Source", "Title") is None


def test_cache_writes_and_reads_category_and_summary():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        cache_path = f.name
    os.unlink(cache_path)
    cache = DigestCache(cache_path)
    summary = ArticleSummary(
        title="Title",
        url="https://example.com/a",
        source="Source",
        summary="Summary",
        key_points=["Point 1", "Point 2"],
        arxiv_url="https://arxiv.org/abs/1234.56789",
        github_url="https://github.com/example/repo",
    )

    cache.set_category("https://example.com/a", "Source", "Title", "Category")
    cache.set_summary(summary)

    reloaded = DigestCache(cache_path)
    cached_summary = reloaded.get_summary("https://example.com/a", "Source", "Title")

    assert reloaded.get_category("https://example.com/a", "Source", "Title") == "Category"
    assert cached_summary.summary == "Summary"
    assert cached_summary.key_points == ["Point 1", "Point 2"]
    assert cached_summary.arxiv_url == "https://arxiv.org/abs/1234.56789"
    assert cached_summary.github_url == "https://github.com/example/repo"
    os.unlink(cache_path)


def test_cache_uses_fallback_key_when_url_missing():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        cache_path = f.name
    os.unlink(cache_path)
    cache = DigestCache(cache_path)

    cache.set_category("", "Source", "Title", "Category")

    reloaded = DigestCache(cache_path)
    assert reloaded.get_category("", "Source", "Title") == "Category"
    os.unlink(cache_path)


def test_cache_ignores_corrupt_json():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as f:
        f.write("{broken")
        cache_path = f.name

    cache = DigestCache(cache_path)

    assert cache.get_category("https://example.com/a", "Source", "Title") is None
    os.unlink(cache_path)
