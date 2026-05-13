# src/summarizer.py
import importlib
import json
import re
from dataclasses import dataclass
from typing import List
from src.claude_client import ClaudeClient, ClaudeConfig


def _default_prompts():
    return importlib.import_module("src.prompts_ai_digest")

@dataclass
class ArticleSummary:
    title: str
    url: str
    source: str
    summary: str
    key_points: List[str]
    arxiv_url: str = ""
    github_url: str = ""
    subtype: str = ""


def _extract_json_array(text: str) -> str:
    start = text.find("[")
    end = text.rfind("]")
    if start == -1 or end == -1 or end < start:
        return text
    return text[start:end + 1]


class Summarizer:
    def __init__(self, config: ClaudeConfig, prompts=None):
        self.client = ClaudeClient(config)
        self.prompts = prompts or _default_prompts()

    def _normalize_category(self, raw: str) -> str:
        """Map AI‑output category to a canonical CATEGORIES key."""
        canonical = self.prompts.CATEGORIES
        if raw in canonical:
            return raw
        # Check substring containment in both directions
        for cat in canonical:
            if raw in cat or cat in raw:
                return cat
        return "其它"

    def classify_only(self, title: str, source: str) -> str:
        """Lightweight classification — no article body, tiny output. Saves tokens for '其它' articles."""
        response = self.client.send_message(
            message=self.prompts.get_classification_prompt(title=title, source=source),
            system=self.prompts.build_classification_system_prompt(),
            max_tokens=50
        )
        text = response.strip()
        for cat in self.prompts.CATEGORIES:
            if cat in text:
                return cat
        return self._normalize_category(text)

    def classify_batch(self, items: List[dict]) -> dict:
        """Classify many articles in one LLM call. Returns {index: {"category": str, "subtype": str}}."""
        if not items:
            return {}

        article_lines = []
        for item in items:
            article_lines.append(
                f'{item["index"]}. title={item["title"]} source={item["source"]}'
            )
        prompt = (
            "Classify each article below. Return only a JSON array. "
            'Each item must have "index", "category", and "subtype".\n\n'
            + "\n".join(article_lines)
        )
        response = self.client.send_message(
            message=prompt,
            system=self.prompts.build_classification_system_prompt(),
            max_tokens=max(100, len(items) * 40)
        )
        data = json.loads(_extract_json_array(response))
        return {int(item["index"]): {"category": self._normalize_category(item["category"]), "subtype": item.get("subtype", "")} for item in data}

    def summarize_batch(self, articles: list) -> dict:
        """Batch summarize multiple articles. Returns {index: ArticleSummary}."""
        if not articles:
            return {}

        prompt = self.prompts.get_batch_summarization_prompt(articles)
        response = self.client.send_message(
            message=prompt,
            system=self.prompts.BATCH_SUMMARIZATION_SYSTEM,
            max_tokens=max(800, len(articles) * 1600)
        )
        data = json.loads(_extract_json_array(response))

        results = {}
        # Build lookup: index → input article for title/url/source
        lookup = {a["index"]: a for a in articles}
        for item in data:
            idx = int(item["index"])
            a = lookup.get(idx)
            results[idx] = ArticleSummary(
                title=a["title"] if a else "",
                url=a["url"] if a else "",
                source=a["source"] if a else "",
                summary=item.get("summary", ""),
                key_points=item.get("key_points", []),
                arxiv_url=item.get("arxiv_url", ""),
                github_url=item.get("github_url", "")
            )
        return results

    def summarize(self, title: str, source: str, url: str, content: str = "", subtype: str = "") -> ArticleSummary:
        response = self.client.send_message(
            message=self.prompts.get_summarization_prompt(title=title, source=source, url=url, content=content),
            system=self.prompts.build_summarization_system_prompt(),
            max_tokens=800
        )

        summary_match = re.search(r'### 摘要\s*\n(.+?)(?=### 关键要点|$)', response, re.DOTALL)
        summary = summary_match.group(1).strip() if summary_match else ""

        points_match = re.findall(r'- (.+)', response)
        key_points = [p.strip() for p in points_match[:5]]

        arxiv_match = re.search(r'### arXiv\s*\n(.+)', response)
        arxiv_raw = arxiv_match.group(1).strip() if arxiv_match else ""
        arxiv_url = ""
        if arxiv_raw and arxiv_raw != "无":
            link_match = re.search(r'https?://arxiv\.org/\S+', arxiv_raw)
            arxiv_url = link_match.group(0).rstrip('.') if link_match else ""

        github_match = re.search(r'### GitHub\s*\n(.+)', response)
        github_raw = github_match.group(1).strip() if github_match else ""
        github_url = ""
        if github_raw and github_raw != "无":
            link_match = re.search(r'https?://github\.com/\S+', github_raw)
            github_url = link_match.group(0).rstrip('.') if link_match else ""

        return ArticleSummary(
            title=title,
            url=url,
            source=source,
            summary=summary,
            key_points=key_points,
            arxiv_url=arxiv_url,
            github_url=github_url,
            subtype=subtype,
        )


@dataclass
class TrendSummary:
    category_name: str
    summary_text: str
    key_trends: List[str]


class TrendSummarizer:
    def __init__(self, config: ClaudeConfig, prompts=None):
        self.client = ClaudeClient(config)
        self.prompts = prompts or _default_prompts()

    def summarize_trends(self, category: str, articles: List[ArticleSummary]) -> TrendSummary:
        prompt = self.prompts.get_trend_summary_prompt(category_name=category, articles=articles)
        response = self.client.send_message(prompt)

        summary_match = re.search(
            r'### 进展与趋势总结\s*\n(.+?)(?=### 关键趋势|$)',
            response, re.DOTALL
        )
        summary_text = summary_match.group(1).strip() if summary_match else ""

        trends_match = re.findall(r'- (.+)', response)
        key_trends = [t.strip() for t in trends_match[:5]]

        return TrendSummary(
            category_name=category,
            summary_text=summary_text,
            key_trends=key_trends
        )
