import logging
import re
from html.parser import HTMLParser
import feedparser
from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Dict, List, Optional
from dateutil import parser as date_parser

logger = logging.getLogger(__name__)

@dataclass
class Article:
    title: str
    url: str
    published: Optional[datetime]
    source: str
    content: str = ""

    def to_dict(self):
        return {
            'title': self.title,
            'url': self.url,
            'published': self.published.isoformat() if self.published else None,
            'source': self.source,
            'content': self.content
        }

class _TextExtractor(HTMLParser):
    """Strip HTML tags and extract plain text, preserving paragraph boundaries."""

    def __init__(self):
        super().__init__()
        self._parts: list[str] = []
        self._skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'noscript'):
            self._skip = True

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'noscript'):
            self._skip = False
        # Treat block-level elements as paragraph breaks
        if tag in ('p', 'div', 'li', 'br', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'tr', 'blockquote'):
            if self._parts and self._parts[-1] != '\n':
                self._parts.append('\n')

    def handle_data(self, data):
        if self._skip:
            return
        text = data.strip()
        if text:
            self._parts.append(text)

    def get_text(self) -> str:
        return ' '.join(self._parts)


def _strip_html(html_text: str) -> str:
    """Convert HTML to plain text. Returns empty string if no meaningful text found."""
    extractor = _TextExtractor()
    extractor.feed(html_text)
    result = extractor.get_text()
    # Collapse whitespace
    result = re.sub(r'[ \t]+', ' ', result)
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result.strip()


def _extract_content(entry) -> str:
    content = getattr(entry, 'content', None)
    if isinstance(content, (list, tuple)) and content:
        first = content[0]
        if isinstance(first, dict):
            value = first.get('value', '')
        else:
            value = getattr(first, 'value', '')
        if value:
            return _strip_html(value)

    summary = getattr(entry, 'summary', '')
    if summary:
        return _strip_html(summary)

    description = getattr(entry, 'description', '')
    if description:
        return _strip_html(description)

    return ""

class RSSFetcher:
    # Registry: URL pattern → (source_name, limit) → List[Article]
    _custom_fetchers: Dict[str, Callable] = {}

    @classmethod
    def register(cls, url_pattern: str, fetcher_fn: Callable):
        """Register a custom fetcher for a URL pattern."""
        cls._custom_fetchers[url_pattern] = fetcher_fn

    def _dispatch_custom(self, source_name: str, url: str, limit: int) -> List[Article] | None:
        for pattern, fetcher_fn in self._custom_fetchers.items():
            if pattern in url:
                logger.info(f"Using custom fetcher for: {source_name}")
                return fetcher_fn(source_name, limit)
        return None

    def fetch(self, source_name: str, url: str, limit: int = 20) -> List[Article]:
        custom_result = self._dispatch_custom(source_name, url, limit)
        if custom_result is not None:
            return custom_result

        feed = feedparser.parse(url)
        articles = []

        for entry in feed.entries[:limit]:
            title = getattr(entry, 'title', 'No Title')
            link = getattr(entry, 'link', '')
            published_str = getattr(entry, 'published', None)

            published = None
            if published_str:
                try:
                    published = date_parser.parse(published_str)
                except Exception:
                    published = None

            articles.append(Article(
                title=title,
                url=link,
                published=published,
                source=source_name,
                content=_extract_content(entry)
            ))

        return articles
