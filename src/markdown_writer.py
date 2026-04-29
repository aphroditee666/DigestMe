import os
from datetime import datetime
from typing import List
from src.summarizer import ArticleSummary

class MarkdownWriter:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir

    def _format_date(self, dt: datetime) -> str:
        return dt.strftime("%Y-%m-%d %H:%M")

    def _get_filename(self, category: str, dt: datetime) -> str:
        date_str = dt.strftime("%Y-%m-%d")
        category_slug = category.replace("/", "_").replace(" ", "_")
        return f"{date_str}-{category_slug}-digest.md"

    def _render_article(self, article: ArticleSummary) -> str:
        lines = [
            f"## [{article.title}]({article.url})",
            "",
            f"**来源:** {article.source}",
            "",
            "### 摘要",
            article.summary,
            "",
            "### 关键要点",
        ]

        for point in article.key_points:
            lines.append(f"- {point}")

        lines.append("")
        return "\n".join(lines)

    def write(self, category: str, articles: List[ArticleSummary], generated_at: datetime) -> str:
        category_dir = os.path.join(self.base_dir, category)
        os.makedirs(category_dir, exist_ok=True)

        filename = self._get_filename(category, generated_at)
        filepath = os.path.join(category_dir, filename)

        lines = [
            f"# {category}资讯汇总",
            "",
            f"> 生成时间: {self._format_date(generated_at)}",
            "",
            "---",
            ""
        ]

        for article in articles:
            lines.append(self._render_article(article))
            lines.append("---")
            lines.append("")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(lines))

        return filepath