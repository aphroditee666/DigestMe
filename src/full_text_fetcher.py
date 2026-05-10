"""
Fetch full article body from original URL when RSS/API content is too short
for meaningful summarization.

Uses trafilatura for robust HTML-to-text extraction.
"""
import logging
from typing import Callable
from urllib.request import Request, urlopen
from urllib.error import URLError

import trafilatura

from .rss_fetcher import Article

logger = logging.getLogger(__name__)

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)

REQUEST_TIMEOUT = 15


class FullTextFetcher:
    _custom_fetchers: dict[str, Callable] = {}

    @classmethod
    def register(cls, url_pattern: str, fetcher_fn: Callable):
        """Register a custom page fetcher for a URL pattern (e.g. 'ai.meta.com/blog')."""
        cls._custom_fetchers[url_pattern] = fetcher_fn

    def __init__(self, min_content_length: int = 500):
        self.min_content_length = min_content_length

    def enrich(self, article: Article) -> Article:
        text_len = len(article.content) if article.content else 0

        if text_len > self.min_content_length:
            logger.info(f"  skip (sufficient): {article.title[:40]}... ({text_len} chars)")
            return article

        if not article.url:
            logger.info(f"  skip (no url): {article.title[:40]}...")
            return article

        try:
            html = self._fetch_url(article.url)
            if not html:
                return article

            extracted = trafilatura.extract(
                html,
                include_links=False,
                include_images=False,
                include_tables=False,
            )
            if extracted and len(extracted) > text_len:
                logger.info(f"  ok: {article.title[:40]}... ({text_len} -> {len(extracted)} chars)")
                article.content = extracted
            else:
                logger.info(f"  no-better: {article.title[:40]}... (kept {text_len} chars)")

        except Exception as e:
            logger.warning(f"  fail: {article.title[:40]}... error: {e}")

        return article

    def _fetch_url(self, url: str) -> str | None:
        # Dispatch to custom fetcher if URL matches a registered pattern
        for pattern, fn in self._custom_fetchers.items():
            if pattern in url:
                logger.info(f"  custom fetch: {url[:60]}...")
                try:
                    return fn(url)
                except Exception as e:
                    logger.warning(f"  custom fetch fail: {url[:60]}... error: {e}")
                    return None

        # Default: plain HTTP GET
        req = Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except URLError as e:
            logger.warning(f"  HTTP fail: {url} error: {e}")
            return None
