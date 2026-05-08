# src/summarizer.py
import re
from dataclasses import dataclass
from typing import List
from src.claude_client import ClaudeClient, ClaudeConfig
from src.prompts import (
    get_summarization_prompt,
    get_classification_prompt,
    get_trend_summary_prompt,
    build_classification_system_prompt,
    build_summarization_system_prompt,
)

@dataclass
class ArticleSummary:
    title: str
    url: str
    source: str
    summary: str
    key_points: List[str]
    arxiv_url: str = ""
    github_url: str = ""

class Summarizer:
    def __init__(self, config: ClaudeConfig):
        self.client = ClaudeClient(config)

    def classify_only(self, title: str, source: str) -> str:
        """Lightweight classification — no article body, tiny output. Saves tokens for '其它' articles."""
        response = self.client.send_message(
            message=get_classification_prompt(title=title, source=source),
            system=build_classification_system_prompt(),
            max_tokens=50
        )
        text = response.strip()
        # Robust matching: find which category name appears in the response
        from src.prompts import CATEGORIES
        for cat in CATEGORIES:
            if cat in text:
                return cat
        return text  # fallback to raw response

    def summarize(self, title: str, source: str, url: str, content: str = "") -> ArticleSummary:
        response = self.client.send_message(
            message=get_summarization_prompt(title=title, source=source, url=url, content=content),
            system=build_summarization_system_prompt(),
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
            github_url=github_url
        )


@dataclass
class TrendSummary:
    category_name: str
    summary_text: str
    key_trends: List[str]


class TrendSummarizer:
    def __init__(self, config: ClaudeConfig):
        self.client = ClaudeClient(config)

    def summarize_trends(self, category: str, articles: List[ArticleSummary]) -> TrendSummary:
        prompt = get_trend_summary_prompt(category_name=category, articles=articles)
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
