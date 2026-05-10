import html
import os
from datetime import datetime
from typing import List, Optional
from src.summarizer import ArticleSummary, TrendSummary


_CSS = r"""
:root {
    --bg: #fafafa;
    --surface: #fff;
    --border: #e5e5e5;
    --text: #1a1a1a;
    --text-secondary: #666;
    --text-muted: #999;
    --accent: #2563eb;
    --accent-light: #eff6ff;
    --badge-bg: #f3f4f6;
    --trend-bg: #fefce8;
    --trend-border: #e5c43d;
    --shadow: 0 1px 3px rgba(0,0,0,.08);
    --shadow-hover: 0 4px 12px rgba(0,0,0,.1);
    --radius: 8px;
    --font: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans SC",sans-serif;
    --mono: "SF Mono","Fira Code","Fira Mono","Roboto Mono",monospace;
}

@media (prefers-color-scheme: dark) {
    :root {
        --bg: #111827;
        --surface: #1f2937;
        --border: #374151;
        --text: #f3f4f6;
        --text-secondary: #9ca3af;
        --text-muted: #6b7280;
        --accent: #60a5fa;
        --accent-light: #1e3a5f;
        --badge-bg: #374151;
        --trend-bg: #292524;
        --trend-border: #a68b02;
        --shadow: 0 1px 3px rgba(0,0,0,.3);
        --shadow-hover: 0 4px 12px rgba(0,0,0,.5);
    }
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: var(--font);
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
}

.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

/* Brand */
.brand {
    display: flex; align-items: center; gap: 10px;
    padding: 20px 0 12px;
    user-select: none;
}
.brand-logo {
    width: 32px; height: 32px; border-radius: 6px;
    background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
    flex-shrink: 0;
}
.brand-text {
    font-size: 18px; font-weight: 600; line-height: 1;
}
.brand-amber { color: #d97706; }
@media (prefers-color-scheme: dark) {
    .brand-amber { color: #f59e0b; }
}

/* Stats Bar */
.stats-bar {
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: 16px 0;
    position: sticky; top: 0; z-index: 100;
    backdrop-filter: blur(8px);
}
.stats-bar .container {
    display: flex; flex-wrap: wrap; align-items: center; gap: 8px 16px;
}
.stats-date { font-weight: 600; font-size: 15px; }
.stats-num { font-size: 14px; color: var(--text-secondary); }
.stats-token { font-size: 12px; color: var(--text-muted); font-family: var(--mono); }
.stats-categories { display: flex; flex-wrap: wrap; gap: 6px; margin-left: auto; }
.cat-pill {
    display: inline-block; padding: 2px 10px; border-radius: 12px;
    font-size: 12px; background: var(--badge-bg); color: var(--text-secondary);
    white-space: nowrap;
}

/* Search */
.search-bar {
    padding: 12px 0;
    background: var(--bg);
    position: sticky; top: 58px; z-index: 99;
}
.search-input {
    width: 100%; padding: 10px 16px; border: 1px solid var(--border);
    border-radius: 8px; font-size: 14px; font-family: var(--font);
    background: var(--surface); color: var(--text);
    outline: none; transition: border-color .2s;
}
.search-input:focus { border-color: var(--accent); }

/* Tab Bar */
.tab-bar {
    padding: 8px 0 16px;
    display: flex; gap: 6px; flex-wrap: wrap;
}
.tab-btn {
    padding: 6px 14px; border: 1px solid var(--border); border-radius: 20px;
    background: var(--surface); color: var(--text-secondary);
    font-size: 13px; cursor: pointer; transition: all .15s;
    font-family: var(--font); white-space: nowrap;
}
.tab-btn:hover { border-color: var(--accent); color: var(--accent); }
.tab-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); }
.tab-count { font-size: 11px; opacity: .7; margin-left: 2px; }

/* Category Section */
.category-section { margin-bottom: 40px; }
.category-header {
    font-size: 20px; font-weight: 700; margin-bottom: 16px;
    padding-bottom: 8px; border-bottom: 2px solid var(--border);
}

/* Trend Card */
.trend-card {
    background: var(--trend-bg); border: 1px solid var(--trend-border);
    border-radius: var(--radius); margin-bottom: 20px; overflow: hidden;
}
.trend-card summary {
    padding: 14px 18px; cursor: pointer; font-weight: 600;
    font-size: 14px; user-select: none;
    color: var(--text); list-style: none;
}
.trend-card summary::-webkit-details-marker { display: none; }
.trend-card summary::before { content: "▸ "; display: inline-block; transition: transform .2s; }
.trend-card[open] summary::before { transform: rotate(90deg); }
.trend-body { padding: 0 18px 16px; font-size: 14px; color: var(--text-secondary); line-height: 1.7; }
.trend-body ul { margin-top: 8px; padding-left: 18px; }
.trend-body li { margin-bottom: 4px; }

/* Subtype Section */
.subtype-section { margin-bottom: 24px; }
.subtype-section:empty { display: none; }
.subtype-header {
    font-size: 16px; font-weight: 600; color: var(--text-secondary);
    margin-bottom: 12px; padding-left: 4px;
}

/* Article Grid */
.article-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 16px;
}

/* Article Card */
.article-card {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 18px 20px;
    box-shadow: var(--shadow); transition: box-shadow .2s;
    display: flex; flex-direction: column;
}
.article-card:hover { box-shadow: var(--shadow-hover); }
.article-card.hidden { display: none; }

.article-title {
    font-size: 15px; font-weight: 600; line-height: 1.4; margin-bottom: 8px;
}
.article-title a { color: var(--text); text-decoration: none; }
.article-title a:hover { color: var(--accent); }

.article-meta {
    font-size: 12px; color: var(--text-muted); margin-bottom: 10px;
    display: flex; gap: 8px; align-items: center; flex-wrap: wrap;
}
.article-source {
    font-weight: 500; color: var(--text-secondary);
}

.article-summary {
    font-size: 13px; color: var(--text-secondary); line-height: 1.6;
    margin-bottom: 10px; flex: 1;
}

.article-badges { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 8px; }
.badge {
    display: inline-block; padding: 2px 8px; border-radius: 4px;
    font-size: 11px; font-family: var(--mono); text-decoration: none;
    background: var(--badge-bg); color: var(--text-secondary);
    transition: background .15s;
}
.badge:hover { background: var(--accent-light); color: var(--accent); }
.badge.arxiv { border-left: 2px solid #b23b3b; }
.badge.github { border-left: 2px solid #333; }

.article-points { font-size: 12px; color: var(--text-muted); }
.article-points ul { padding-left: 16px; }
.article-points li { margin-bottom: 2px; }

/* Footer */
.page-footer {
    text-align: center; padding: 24px 0 40px;
    font-size: 12px; color: var(--text-muted);
    border-top: 1px solid var(--border); margin-top: 40px;
}

/* Mobile */
@media (max-width: 768px) {
    .article-grid { grid-template-columns: 1fr; }
    .stats-bar .container { flex-direction: column; align-items: flex-start; }
    .stats-categories { margin-left: 0; }
    .search-bar { top: 100px; }
    .tab-bar { overflow-x: auto; flex-wrap: nowrap; -webkit-overflow-scrolling: touch; }
}
"""


_JS = r"""
(function() {
    const searchInput = document.getElementById('search');
    const cards = document.querySelectorAll('.article-card');
    const tabBtns = document.querySelectorAll('.tab-btn');
    const sections = document.querySelectorAll('.category-section');
    const trendCards = document.querySelectorAll('.trend-card');

    // Search filter
    searchInput.addEventListener('input', function() {
        const query = this.value.toLowerCase().trim();
        cards.forEach(function(card) {
            const text = (card.getAttribute('data-search-text') || '').toLowerCase();
            card.classList.toggle('hidden', query && text.indexOf(query) === -1);
        });
        // Update category visibility after search
        updateCategoryVisibility();
    });

    // Tab filter
    tabBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
            tabBtns.forEach(function(b) { b.classList.remove('active'); });
            this.classList.add('active');
            filterByTab(this.getAttribute('data-category'));
        });
    });

    function filterByTab(cat) {
        sections.forEach(function(section) {
            if (cat === 'all' || section.getAttribute('data-category') === cat) {
                section.style.display = '';
            } else {
                section.style.display = 'none';
            }
        });
        // Re-apply search on visible cards
        var query = searchInput.value.toLowerCase().trim();
        cards.forEach(function(card) {
            if (card.closest('.category-section').style.display === 'none') {
                card.classList.add('hidden');
            } else if (query) {
                var text = (card.getAttribute('data-search-text') || '').toLowerCase();
                card.classList.toggle('hidden', text.indexOf(query) === -1);
            } else {
                card.classList.remove('hidden');
            }
        });
        updateCategoryVisibility();
    }

    function updateCategoryVisibility() {
        sections.forEach(function(section) {
            var visibleCards = section.querySelectorAll('.article-card:not(.hidden)');
            var hasContent = visibleCards.length > 0;
            section.style.display = hasContent ? '' : 'none';
            // Hide empty subtype sections
            var subtypeSections = section.querySelectorAll('.subtype-section');
            subtypeSections.forEach(function(ss) {
                var visibleInSubtype = ss.querySelectorAll('.article-card:not(.hidden)');
                ss.style.display = visibleInSubtype.length > 0 ? '' : 'none';
            });
        });
    }

    // Keyboard shortcut: / to focus search
    document.addEventListener('keydown', function(e) {
        if (e.key === '/' && document.activeElement !== searchInput) {
            e.preventDefault();
            searchInput.focus();
        }
        if (e.key === 'Escape') { searchInput.blur(); }
    });
})();
"""


class HTMLWriter:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir

    def write_all(
        self,
        articles_by_category: dict,
        trends_by_category: dict,
        generated_at: datetime,
        stats: dict,
        file_index: int = None
    ) -> str:
        date_str = generated_at.strftime("%Y-%m-%d")
        if file_index is not None:
            filename = f"{date_str}-digest.html" if file_index == 0 else f"{date_str}-digest-{file_index}.html"
            filepath = os.path.join(self.base_dir, filename)
        else:
            filename = f"{date_str}-digest.html"
            filepath = self._next_available_path(os.path.join(self.base_dir, filename))

        cat_counts = stats.get("categories", {})
        all_categories = list(articles_by_category.keys())

        parts = [
            "<!DOCTYPE html>",
            '<html lang="zh-CN">',
            "<head>",
            '<meta charset="UTF-8">',
            '<meta name="viewport" content="width=device-width,initial-scale=1">',
            f"<title>Clyde's Digest — {date_str}</title>",
            "<style>",
            _CSS,
            "</style>",
            "</head>",
            "<body>",
            '<div class="container"><div class="brand"><div class="brand-logo"></div><span class="brand-text"><span class="brand-amber">Clyde\'s</span> Digest</span></div></div>',
            self._render_stats_bar(generated_at, stats, cat_counts),
            self._render_search_bar(),
            self._render_tab_bar(all_categories, cat_counts),
            '<div class="container">',
        ]

        for category in all_categories:
            subtypes = articles_by_category.get(category, {})
            total_in_cat = sum(len(v) for v in subtypes.values())
            if total_in_cat == 0:
                continue
            parts.append(f'<section class="category-section" data-category="{html.escape(category)}">')
            parts.append(f'<h2 class="category-header">{html.escape(category)}</h2>')

            trend = trends_by_category.get(category)
            if trend:
                parts.append(self._render_trend_card(trend))

            for subtype, articles in subtypes.items():
                if not articles:
                    continue
                parts.append(f'<div class="subtype-section">')
                parts.append(f'<h3 class="subtype-header">{html.escape(subtype)}</h3>')
                parts.append('<div class="article-grid">')
                for article in articles:
                    parts.append(self._render_article_card(article))
                parts.append('</div>')
                parts.append('</div>')

            parts.append('</section>')

        parts.append('</div>')
        parts.append(self._render_footer(generated_at, stats))
        parts.append("<script>")
        parts.append(_JS)
        parts.append("</script>")
        parts.append("</body>")
        parts.append("</html>")

        os.makedirs(self.base_dir, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(parts))

        return filepath

    def _render_stats_bar(self, generated_at, stats, cat_counts) -> str:
        total_articles = sum(cat_counts.values())
        pills = "".join(
            f'<span class="cat-pill">{html.escape(cat)}:{count}</span>'
            for cat, count in cat_counts.items() if count > 0
        )
        return (
            '<div class="stats-bar">'
            '<div class="container">'
            f'<span class="stats-date">{generated_at.strftime("%Y-%m-%d %H:%M")}</span>'
            f'<span class="stats-num">共 {total_articles} 篇摘要</span>'
            f'<span class="stats-token">Token {stats.get("token_total", 0):,}</span>'
            f'<div class="stats-categories">{pills}</div>'
            '</div></div>'
        )

    def _render_search_bar(self) -> str:
        return (
            '<div class="search-bar"><div class="container">'
            '<input type="text" id="search" class="search-input" '
            'placeholder="搜索标题、来源、摘要... (按 / 聚焦)">'
            '</div></div>'
        )

    def _render_tab_bar(self, categories, cat_counts) -> str:
        total = sum(cat_counts.values())
        buttons = [f'<button class="tab-btn active" data-category="all">全部<span class="tab-count">{total}</span></button>']
        for cat in categories:
            count = cat_counts.get(cat, 0)
            if count > 0:
                buttons.append(
                    f'<button class="tab-btn" data-category="{html.escape(cat)}">'
                    f'{html.escape(cat)}<span class="tab-count">{count}</span></button>'
                )
        return f'<div class="container"><div class="tab-bar">{"".join(buttons)}</div></div>'

    def _render_article_card(self, article: ArticleSummary) -> str:
        search_text = " ".join(
            [article.title, article.source, article.summary] + article.key_points
        )
        lines = [
            '<article class="article-card"'
            f' data-search-text="{html.escape(search_text, quote=True)}">',
            f'<div class="article-title"><a href="{html.escape(article.url)}" target="_blank" rel="noopener">{html.escape(article.title)}</a></div>',
            f'<div class="article-meta"><span class="article-source">{html.escape(article.source)}</span></div>',
            f'<div class="article-summary">{html.escape(article.summary)}</div>',
        ]

        # Badges: arXiv / GitHub
        badges = []
        if article.arxiv_url:
            badges.append(
                f'<a href="{html.escape(article.arxiv_url)}" class="badge arxiv" target="_blank" rel="noopener">arXiv</a>'
            )
        if article.github_url:
            badges.append(
                f'<a href="{html.escape(article.github_url)}" class="badge github" target="_blank" rel="noopener">GitHub</a>'
            )
        if badges:
            lines.append(f'<div class="article-badges">{"".join(badges)}</div>')

        # Key points
        if article.key_points:
            points = "".join(f"<li>{html.escape(p)}</li>" for p in article.key_points)
            lines.append(f'<div class="article-points"><ul>{points}</ul></div>')

        lines.append("</article>")
        return "\n".join(lines)

    def _render_trend_card(self, trend: TrendSummary) -> str:
        points = "".join(f"<li>{html.escape(p)}</li>" for p in trend.key_trends)
        return (
            '<details class="trend-card" open>'
            f'<summary>本周趋势 · {html.escape(trend.category_name)}</summary>'
            '<div class="trend-body">'
            f'<p>{html.escape(trend.summary_text)}</p>'
            f'<ul>{points}</ul>'
            '</div>'
            '</details>'
        )

    def _render_footer(self, generated_at, stats) -> str:
        return (
            '<footer class="page-footer"><div class="container">'
            f'Generated at {generated_at.strftime("%Y-%m-%d %H:%M")}'
            f' · {stats.get("articles_seen", 0)} seen'
            f' · {stats.get("articles_summarized", 0)} summarized'
            f' · {stats.get("token_total", 0):,} tokens'
            f' · {stats.get("llm_time", 0):.1f}s'
            '</div></footer>'
        )

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

    def update_readme(self, filepath: str, stats: dict) -> str:
        """Append HTML file entry to output/README.md."""
        parent = os.path.dirname(self.base_dir.rstrip("/\\")) or self.base_dir
        readme_path = os.path.join(parent, "README.md")

        date_str = stats["generated_at"].strftime("%Y-%m-%d")
        time_str = stats["generated_at"].strftime("%H:%M")
        filename = os.path.basename(filepath)
        rel_path = os.path.relpath(filepath, parent).replace("\\", "/")

        total = stats.get("articles_summarized", 0)
        entry = (f"- [{time_str} HTML — {filename}]({rel_path})"
                 f" | 摘要 {total} 篇 | Token {stats.get('token_total', 0):,}")

        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = "# 日报索引\n\n> 生成时间倒序排列，最新在上。\n\n"

        date_header = f"## {date_str}"
        if date_header in content:
            content = content.replace(date_header + "\n", date_header + "\n\n" + entry + "\n")
        else:
            lines = content.split("\n")
            for i, line in enumerate(lines):
                if line.startswith("## "):
                    lines.insert(i, "")
                    lines.insert(i, entry)
                    lines.insert(i, "")
                    lines.insert(i, f"## {date_str}")
                    break
            else:
                lines.append(f"\n## {date_str}\n\n{entry}\n")
            content = "\n".join(lines)

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return readme_path
