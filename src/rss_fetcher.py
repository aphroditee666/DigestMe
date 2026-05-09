import feedparser
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from dateutil import parser as date_parser

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

def _extract_content(entry) -> str:
    content = getattr(entry, 'content', None)
    if isinstance(content, (list, tuple)) and content:
        first = content[0]
        if isinstance(first, dict):
            value = first.get('value', '')
        else:
            value = getattr(first, 'value', '')
        if value:
            return value

    summary = getattr(entry, 'summary', '')
    if summary:
        return summary

    description = getattr(entry, 'description', '')
    if description:
        return description

    return ""

class RSSFetcher:
    def fetch(self, source_name: str, url: str, limit: int = 10) -> List[Article]:
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
