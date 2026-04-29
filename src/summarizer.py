# src/summarizer.py
import re
from dataclasses import dataclass
from typing import List
from src.claude_client import ClaudeClient, ClaudeConfig
from src.prompts import get_summarization_prompt

@dataclass
class ArticleSummary:
    title: str
    url: str
    source: str
    summary: str
    key_points: List[str]

class Summarizer:
    def __init__(self, config: ClaudeConfig):
        self.client = ClaudeClient(config)

    def summarize(self, title: str, source: str, url: str) -> ArticleSummary:
        prompt = get_summarization_prompt(
            title=title,
            source=source,
            url=url
        )

        response = self.client.send_message(prompt)

        summary_match = re.search(r'### 摘要\s*\n(.+?)(?=### 关键要点|$)', response, re.DOTALL)
        summary = summary_match.group(1).strip() if summary_match else ""

        key_points = []
        points_match = re.findall(r'- (.+)', response)
        key_points = [p.strip() for p in points_match[:3]]

        return ArticleSummary(
            title=title,
            url=url,
            source=source,
            summary=summary,
            key_points=key_points
        )