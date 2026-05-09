import os
from datetime import datetime
from typing import List, Optional
from src.summarizer import ArticleSummary, TrendSummary

class MarkdownWriter:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir

    def _format_date(self, dt: datetime) -> str:
        return dt.strftime("%Y-%m-%d %H:%M")

    def _get_filename(self, category: str, dt: datetime) -> str:
        date_str = dt.strftime("%Y-%m-%d")
        category_slug = category.replace("/", "_").replace(" ", "_")
        return f"{date_str}-{category_slug}-digest.md"

    def _next_available_path(self, filepath: str) -> str:
        if not os.path.exists(filepath):
            return filepath

        base, ext = os.path.splitext(filepath)
        index = 1
        while True:
            candidate = f"{base}-{index}{ext}"
            if not os.path.exists(candidate):
                return candidate
            index += 1

    def _render_trend_summary(self, ts: TrendSummary) -> str:
        lines = [
            "## 本周进展与趋势",
            "",
            ts.summary_text,
            "",
            "### 关键趋势",
        ]
        for trend in ts.key_trends:
            lines.append(f"- {trend}")
        lines.append("")
        lines.append("---")
        lines.append("")
        return "\n".join(lines)

    def _render_article(self, article: ArticleSummary) -> str:
        lines = [
            f"## [{article.title}]({article.url})",
            "",
            f"**来源:** {article.source}",
        ]

        if article.arxiv_url:
            lines.append(f"**arXiv:** [{article.arxiv_url}]({article.arxiv_url})")

        if article.github_url:
            lines.append(f"**GitHub:** [{article.github_url}]({article.github_url})")

        lines.extend([
            "",
            "### 摘要",
            article.summary,
            "",
            "### 关键要点",
        ])

        for point in article.key_points:
            lines.append(f"- {point}")

        lines.append("")
        return "\n".join(lines)

    def write_all(self, articles_by_category: dict, trends_by_category: dict, generated_at: datetime) -> str:
        """Write all categories into a single markdown file."""
        date_str = generated_at.strftime("%Y-%m-%d")
        filename = f"{date_str}-digest.md"
        filepath = self._next_available_path(os.path.join(self.base_dir, filename))

        lines = [
            f"# 资讯汇总",
            "",
            f"> 生成时间: {self._format_date(generated_at)}",
            "",
            "---",
            ""
        ]

        for category, articles in articles_by_category.items():
            if not articles:
                continue
            lines.append(f"# {category}")
            lines.append("")

            trend = trends_by_category.get(category)
            if trend:
                lines.append(self._render_trend_summary(trend))

            for article in articles:
                lines.append(self._render_article(article))
                lines.append("---")
                lines.append("")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(lines))

        return filepath

    def write(self, category: str, articles: List[ArticleSummary], generated_at: datetime, trend_summary: Optional[TrendSummary] = None) -> str:
        category_dir = os.path.join(self.base_dir, category)
        os.makedirs(category_dir, exist_ok=True)

        filename = self._get_filename(category, generated_at)
        filepath = self._next_available_path(os.path.join(category_dir, filename))

        lines = [
            f"# {category}资讯汇总",
            "",
            f"> 生成时间: {self._format_date(generated_at)}",
            "",
            "---",
            ""
        ]

        if trend_summary:
            lines.append(self._render_trend_summary(trend_summary))

        for article in articles:
            lines.append(self._render_article(article))
            lines.append("---")
            lines.append("")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(lines))

        return filepath
