import json
import logging
import os
from datetime import datetime
from typing import Optional

from src.summarizer import ArticleSummary

logger = logging.getLogger(__name__)


class DigestCache:
    def __init__(self, path: str):
        self.path = path
        self._data = self._load()

    def _load(self) -> dict:
        if not os.path.exists(self.path):
            return {"articles": {}}
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if not isinstance(data, dict):
                return {"articles": {}}
            data.setdefault("articles", {})
            return data
        except Exception as e:
            logger.warning(f"Failed to load digest cache {self.path}: {e}")
            return {"articles": {}}

    def _save(self):
        directory = os.path.dirname(self.path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self._data, f, ensure_ascii=False, indent=2)

    def _key(self, url: str, source: str, title: str) -> str:
        if url:
            return url
        return f"{source}::{title}"

    def _entry(self, url: str, source: str, title: str) -> dict:
        key = self._key(url, source, title)
        articles = self._data.setdefault("articles", {})
        return articles.setdefault(key, {
            "title": title,
            "url": url,
            "source": source,
        })

    def get_category(self, url: str, source: str, title: str) -> Optional[str]:
        entry = self._data.get("articles", {}).get(self._key(url, source, title), {})
        return entry.get("category")

    def set_category(self, url: str, source: str, title: str, category: str):
        entry = self._entry(url, source, title)
        entry["category"] = category
        entry["updated_at"] = datetime.now().isoformat()
        self._save()

    def get_summary(self, url: str, source: str, title: str) -> Optional[ArticleSummary]:
        entry = self._data.get("articles", {}).get(self._key(url, source, title), {})
        summary = entry.get("summary")
        if summary is None:
            return None
        return ArticleSummary(
            title=entry.get("title", title),
            url=entry.get("url", url),
            source=entry.get("source", source),
            summary=summary,
            key_points=entry.get("key_points", []),
            arxiv_url=entry.get("arxiv_url", ""),
            github_url=entry.get("github_url", ""),
        )

    def set_summary(self, summary: ArticleSummary):
        entry = self._entry(summary.url, summary.source, summary.title)
        entry.update({
            "summary": summary.summary,
            "key_points": summary.key_points,
            "arxiv_url": summary.arxiv_url,
            "github_url": summary.github_url,
            "updated_at": datetime.now().isoformat(),
        })
        self._save()
