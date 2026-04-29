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

    def to_dict(self):
        return {
            'title': self.title,
            'url': self.url,
            'published': self.published.isoformat() if self.published else None,
            'source': self.source
        }

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
                source=source_name
            ))

        return articles