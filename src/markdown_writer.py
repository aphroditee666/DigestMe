import os
from datetime import datetime
from typing import List, Optional
from src.summarizer import ArticleSummary, TrendSummary


def _format_size(size_bytes: int) -> str:
    if size_bytes >= 1024:
        return f"{size_bytes // 1024}KB"
    return f"{size_bytes}B"


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

    def write_all(self, articles_by_category: dict, trends_by_category: dict, generated_at: datetime, file_index: int = None) -> str:
        """Write all categories into a single markdown file."""
        date_str = generated_at.strftime("%Y-%m-%d")
        if file_index is not None:
            filename = f"{date_str}-digest.md" if file_index == 0 else f"{date_str}-digest-{file_index}.md"
            filepath = os.path.join(self.base_dir, filename)
        else:
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

        for category, subtypes in articles_by_category.items():
            total = sum(len(v) for v in subtypes.values())
            if total == 0:
                continue
            lines.append(f"# {category}")
            lines.append("")

            trend = trends_by_category.get(category)
            if trend:
                lines.append(self._render_trend_summary(trend))

            for subtype, articles in subtypes.items():
                if not articles:
                    continue
                lines.append(f"## {subtype}")
                lines.append("")

                for article in articles:
                    lines.append(self._render_article(article))
                    lines.append("---")
                    lines.append("")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(lines))

        return filepath

    def update_readme(self, filepath: str, stats: dict) -> str:
        """Prepend the latest run entry to output/README.md with stats."""
        # Write README one level above base_dir so it sits at output/README.md
        parent = os.path.dirname(self.base_dir.rstrip("/\\")) or self.base_dir
        readme_path = os.path.join(parent, "README.md")

        date_str = stats["generated_at"].strftime("%Y-%m-%d")
        time_str = stats["generated_at"].strftime("%H:%M")
        filename = os.path.basename(filepath)
        rel_path = os.path.relpath(filepath, parent).replace("\\", "/")
        size_str = _format_size(stats["file_size"])

        cat_parts = []
        for cat, count in stats.get("categories", {}).items():
            if count > 0:
                cat_parts.append(f"{cat}:{count}")
        cat_line = " | ".join(cat_parts)

        config_name = stats.get("config_path", "").replace("\\", "/")
        entry_lines = [
            f"- [{time_str} — {filename}]({rel_path}) ({size_str})",
            f"  > 配置: `{config_name}` | 抓取 {stats['articles_seen']} 篇(近期 {stats['articles_recent']}) | 摘要 {stats['articles_summarized']} 篇 | Token {stats['token_total']:,} | {stats['llm_time']:.1f}s",
        ]
        if cat_line:
            entry_lines.append(f"  > {cat_line}")

        new_entry = "\n".join(entry_lines)

        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = "# 日报索引\n\n> 生成时间倒序排列，最新在上。\n\n"

        date_header = f"## {date_str}"
        if date_header in content:
            content = content.replace(date_header + "\n", date_header + "\n\n" + new_entry + "\n")
        else:
            lines = content.split("\n")
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith("## "):
                    insert_pos = i
                    break
            if insert_pos == 0:
                # After header lines (title + blank + quote + blank)
                insert_pos = 4
            section = [f"## {date_str}", "", new_entry, ""]
            lines = lines[:insert_pos] + section + lines[insert_pos:]
            content = "\n".join(lines)

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return readme_path

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
