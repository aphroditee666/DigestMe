import html
import json
import os
from datetime import datetime


_FAVORITES_CSS = r"""
:root {
    --sidebar-w: 260px;
    --primary: #6366f1;
    --primary-light: #818cf8;
    --primary-dark: #4f46e5;
    --primary-bg: #ede4d6;
    --accent: #8b5cf6;
    --bg: #f5f0e5;
    --surface: #fefcf5;
    --border: #e5ddd0;
    --text: #2c2416;
    --text-secondary: #6b5d4e;
    --text-muted: #a09888;
    --shadow-card: 0 2px 8px rgba(0,0,0,.04), 0 1px 2px rgba(0,0,0,.05);
    --shadow-hover: 0 8px 24px rgba(139,92,246,.10);
    --radius: 12px;
    --radius-sm: 8px;
    --font: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans SC",sans-serif;
    --mono: "SF Mono","Fira Code","Fira Mono","Roboto Mono",monospace;
    --card-hl: linear-gradient(135deg, #ede4d6 0%, #f0e8da 50%, #f5efe3 100%);
    --card-normal: linear-gradient(135deg, #fdfaf5 0%, #faf5ed 100%);
}

[data-theme="dark"] {
    --primary: #cba6f7;
    --primary-light: #d9baf9;
    --primary-dark: #b491e8;
    --primary-bg: #221f3a;
    --accent: #cba6f7;
    --bg: #14131c;
    --surface: #1e1d2a;
    --border: #2d2b3e;
    --text: #cdd6f4;
    --text-secondary: #a6adc8;
    --text-muted: #6c7086;
    --shadow-card: 0 2px 8px rgba(0,0,0,.45);
    --shadow-hover: 0 8px 24px rgba(203,166,247,.15);
    --card-hl: linear-gradient(135deg, #1e1d2a 0%, #221f3a 50%, #26233e 100%);
    --card-normal: linear-gradient(135deg, #1e1d2a 0%, #1c1b26 100%);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }

body {
    font-family: var(--font);
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
}

/* Sidebar */
.sidebar {
    position: fixed; top: 0; left: 0; bottom: 0;
    width: var(--sidebar-w);
    background: var(--surface);
    border-right: 1px solid var(--border);
    z-index: 200;
    display: flex; flex-direction: column;
    overflow-y: auto;
}
.sidebar-brand {
    padding: 20px 24px 16px;
    display: flex; align-items: center; gap: 10px; flex-shrink: 0;
}
.sidebar-logo {
    width: 36px; height: 36px; border-radius: 10px;
    background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
    flex-shrink: 0; display: flex; align-items: center; justify-content: center;
    color: #fff; font-size: 18px; font-weight: 700;
}
.sidebar-title { font-size: 17px; font-weight: 700; }
.sidebar-title span { color: var(--primary); }
.sidebar-nav {
    flex: 1; padding: 4px 12px;
}
.sidebar-label {
    font-size: 10px; text-transform: uppercase; letter-spacing: .08em;
    color: var(--text-muted); padding: 12px 12px 6px; font-weight: 600;
}
.sidebar-link {
    display: flex; align-items: center; gap: 10px;
    padding: 10px 12px; border-radius: var(--radius-sm);
    color: var(--text-secondary); text-decoration: none;
    font-size: 14px; font-weight: 500;
    transition: all .15s; cursor: pointer; margin-bottom: 2px;
}
.sidebar-link:hover { background: var(--primary-bg); color: var(--primary); }
.sidebar-link.active { background: var(--primary-bg); color: var(--primary); font-weight: 600; }
.sidebar-count {
    margin-left: auto; font-size: 12px; font-weight: 600;
    background: var(--primary-bg); color: var(--primary);
    padding: 1px 8px; border-radius: 10px; min-width: 24px; text-align: center;
}
.sidebar-link.active .sidebar-count { background: var(--primary); color: #fff; }
.sidebar-footer {
    padding: 12px 24px; border-top: 1px solid var(--border);
    font-size: 12px; color: var(--text-muted); flex-shrink: 0;
}

/* Main */
.main {
    margin-left: var(--sidebar-w);
    min-height: 100vh;
}

/* Topbar */
.topbar {
    position: sticky; top: 0; z-index: 100;
    background: var(--bg); backdrop-filter: blur(12px);
    padding: 12px 0; border-bottom: 1px solid var(--border);
}
.topbar-inner {
    max-width: 1100px; margin: 0 auto; padding: 0 32px;
    display: flex; align-items: center; gap: 12px;
}
.topbar-title { font-size: 18px; font-weight: 700; flex: 1; }
.topbar-stats {
    font-size: 13px; color: var(--text-muted); white-space: nowrap;
}
.topbar-btn {
    width: 38px; height: 38px; border-radius: var(--radius-sm);
    border: 1px solid var(--border); background: var(--surface);
    color: var(--text-secondary); cursor: pointer; font-size: 16px;
    display: flex; align-items: center; justify-content: center;
    transition: all .15s; text-decoration: none;
}
.topbar-btn:hover { border-color: var(--primary); color: var(--primary); }

/* Content */
.content { max-width: 1100px; margin: 0 auto; padding: 0 32px 60px; }

/* Folder section */
.folder-section { margin-bottom: 48px; scroll-margin-top: 80px; }
.folder-header {
    display: flex; align-items: center; gap: 12px;
    font-size: 22px; font-weight: 800; margin-bottom: 20px;
}
.folder-dot {
    width: 10px; height: 10px; border-radius: 50%;
    background: var(--primary); flex-shrink: 0;
}

/* Article Grid */
.article-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 16px;
}

/* Article Card */
.article-card {
    background: var(--card-normal);
    border: 1px solid var(--border);
    border-radius: var(--radius); padding: 20px 22px;
    box-shadow: var(--shadow-card); transition: all .25s;
    display: flex; flex-direction: column;
    position: relative; overflow: hidden;
}
.article-card::before {
    content: ""; position: absolute; top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--primary-light), var(--accent));
    opacity: 0; transition: opacity .25s;
}
.article-card:hover {
    box-shadow: var(--shadow-hover); transform: translateY(-2px);
}
.article-card:hover::before { opacity: 1; }
.article-card.highlight { background: var(--card-hl); }

.article-title {
    font-size: 15px; font-weight: 650; line-height: 1.45; margin-bottom: 10px;
}
.article-title a { color: var(--text); text-decoration: none; }
.article-title a:hover { color: var(--primary); }

.article-meta {
    font-size: 12px; color: var(--text-muted); margin-bottom: 10px;
    display: flex; gap: 8px; align-items: center; flex-wrap: wrap;
}
.article-source {
    font-weight: 600; color: var(--primary); font-size: 11px;
    background: var(--primary-bg); padding: 2px 10px; border-radius: 12px;
}
.article-subtype {
    font-size: 11px; color: var(--text-muted);
    background: var(--bg); padding: 2px 8px; border-radius: 8px;
}

.article-summary {
    font-size: 13px; color: var(--text-secondary); line-height: 1.65;
    margin-bottom: 12px; flex: 1;
}

.article-badges { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 8px; }
.badge {
    display: inline-flex; align-items: center; gap: 4px;
    padding: 3px 10px; border-radius: 6px;
    font-size: 11px; font-weight: 600; font-family: var(--mono);
    text-decoration: none; transition: all .15s;
}
.badge.arxiv { background: #fef2f2; color: #b91c1c; border: 1px solid #fecaca; }
.badge.github { background: #f0f0f5; color: #333; border: 1px solid #d4d4d8; }
[data-theme="dark"] .badge.arxiv { background: #3b1111; color: #fca5a5; border-color: #7f1d1d; }
[data-theme="dark"] .badge.github { background: #1f1f2e; color: #d4d4d8; border-color: #3f3f46; }

.article-points { font-size: 12px; color: var(--text-secondary); }
.article-points ul { padding-left: 18px; }
.article-points li { margin-bottom: 3px; }
.article-points li::marker { color: var(--primary-light); }

/* Empty state */
.empty-state {
    text-align: center; padding: 80px 20px; color: var(--text-muted);
}
.empty-state h2 { font-size: 24px; margin-bottom: 12px; color: var(--text-secondary); }
.empty-state p { font-size: 14px; }

/* Footer */
.page-footer {
    text-align: center; padding: 32px 32px 48px;
    font-size: 12px; color: var(--text-muted);
    border-top: 1px solid var(--border); margin-top: 20px;
}

/* Mobile */
@media (max-width: 768px) {
    :root { --sidebar-w: 0px; }
    .sidebar { display: none; }
    .main { margin-left: 0; }
    .article-grid { grid-template-columns: 1fr; }
    .topbar-inner { padding: 0 16px; }
    .content { padding: 0 16px 40px; }
}
"""

_FAVORITES_JS = r"""
(function() {
    var htmlEl = document.documentElement;
    var themeToggle = document.getElementById('theme-toggle');
    var savedTheme;
    try { savedTheme = localStorage.getItem('digest-theme'); } catch(e) {}
    if (!savedTheme) savedTheme = 'dark';
    htmlEl.setAttribute('data-theme', savedTheme);
    themeToggle.textContent = savedTheme === 'dark' ? '☀️' : '🌙';

    themeToggle.addEventListener('click', function() {
        var next = htmlEl.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        htmlEl.setAttribute('data-theme', next);
        themeToggle.textContent = next === 'dark' ? '☀️' : '🌙';
        try { localStorage.setItem('digest-theme', next); } catch(e) {}
    });

    // Sidebar link scroll to folder section
    var links = document.querySelectorAll('.sidebar-link[data-folder-id]');
    var sections = document.querySelectorAll('.folder-section');
    var backTop = document.getElementById('back-top');
    var topbar = document.querySelector('.topbar');

    links.forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            var folderId = this.getAttribute('data-folder-id');
            var section = document.querySelector('.folder-section[data-folder-id="' + folderId + '"]');
            if (section) {
                section.scrollIntoView({behavior: 'smooth', block: 'start'});
            }
        });
    });

    if (backTop) {
        backTop.addEventListener('click', function() {
            window.scrollTo({top: 0, behavior: 'smooth'});
        });
    }

    // Highlight active nav on scroll
    var ticking = false;
    function updateActiveNav() {
        var scrollY = window.scrollY + 100;
        var activeFolder = 'all';
        sections.forEach(function(section) {
            if (section.offsetTop <= scrollY) {
                activeFolder = section.getAttribute('data-folder-id');
            }
        });
        links.forEach(function(link) {
            var fid = link.getAttribute('data-folder-id');
            link.classList.toggle('active', fid === activeFolder);
        });
        topbar.classList.toggle('scrolled', window.scrollY > 20);
    }
    window.addEventListener('scroll', function() {
        if (!ticking) {
            requestAnimationFrame(function() { updateActiveNav(); ticking = false; });
            ticking = true;
        }
    });
    updateActiveNav();

    // Highlight ~15% of cards
    var allCards = document.querySelectorAll('.article-card');
    var hlCount = Math.round(allCards.length * 0.15);
    var indices = Array.from({length: allCards.length}, function(_, i) { return i; });
    for (var i = indices.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var t = indices[i]; indices[i] = indices[j]; indices[j] = t;
    }
    for (var k = 0; k < hlCount; k++) {
        if (allCards[indices[k]]) allCards[indices[k]].classList.add('highlight');
    }
})();
"""


class FavoritesWriter:
    def __init__(self, output_dir: str = "./output"):
        self.output_dir = output_dir

    def write_standalone_md(
        self,
        favorites_json_path: str,
        output_filename: str = "favorites.md",
        title: str = "My Digest Favorites"
    ) -> str:
        with open(favorites_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if "articles" not in data:
            raise ValueError("Invalid favorites JSON: missing 'articles' key")

        articles = data.get("articles", {})
        folders = data.get("folders", [])
        total = len(articles)

        generated_at = datetime.now()

        # Group articles by folder
        by_folder = {}
        uncategorized = []

        for url, article in articles.items():
            article["_url"] = url
            fid = article.get("folderId")
            if fid and any(f["id"] == fid for f in folders):
                by_folder.setdefault(fid, []).append(article)
            else:
                uncategorized.append(article)

        def sort_key(a):
            return a.get("favoritedAt", "")

        uncategorized.sort(key=sort_key, reverse=True)
        for fid in by_folder:
            by_folder[fid].sort(key=sort_key, reverse=True)

        lines = [
            f"# {title}",
            "",
            f"> 共 {total} 篇收藏 · 生成于 {generated_at.strftime('%Y-%m-%d %H:%M')}",
            "",
        ]

        # Folder index
        lines.append("## 目录")
        lines.append("")
        for fid in [None] + [f["id"] for f in folders]:
            if fid is None:
                folder_name = "未分类"
                count = len(uncategorized)
                anchor = "uncategorized"
            else:
                folder = next((f for f in folders if f["id"] == fid), None)
                if not folder:
                    continue
                folder_name = folder["name"]
                count = len(by_folder.get(fid, []))
                anchor = folder["id"]
            if count == 0:
                continue
            lines.append(f"- [{folder_name} ({count} 篇)](#{anchor})")
        lines.append("")

        # Render each folder
        for fid in [None] + [f["id"] for f in folders]:
            if fid is None:
                folder_name = "未分类"
                anchor = "uncategorized"
                arts = uncategorized
            else:
                folder = next((f for f in folders if f["id"] == fid), None)
                if not folder:
                    continue
                folder_name = folder["name"]
                anchor = folder["id"]
                arts = by_folder.get(fid, [])

            if not arts:
                continue

            lines.append(f"## {folder_name} {{#{anchor}}}")
            lines.append("")

            for article in arts:
                lines.append(self._render_article_md(article))
                lines.append("")

        # Footer
        lines.append("---")
        lines.append(f"*Generated at {generated_at.strftime('%Y-%m-%d %H:%M')} · {total} articles*")
        lines.append("")

        # Embed JSON data for reliable re-import
        clean_data = {"version": 1, "folders": data.get("folders", []), "articles": data.get("articles", {})}
        lines.append("<!-- digest-favorites-data")
        lines.append(json.dumps(clean_data, ensure_ascii=False))
        lines.append("-->")
        lines.append("")

        os.makedirs(self.output_dir, exist_ok=True)
        output_path = os.path.join(self.output_dir, output_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(lines))

        return output_path

    def _render_article_md(self, article: dict) -> str:
        title = article.get("title", "")
        url = article.get("url", article.get("_url", ""))
        source = article.get("source", "")
        summary = article.get("summary", "")
        key_points = article.get("keyPoints", [])
        arxiv_url = article.get("arxivUrl", "")
        github_url = article.get("githubUrl", "")
        subtype = article.get("subtype", "")
        favorited_at = article.get("favoritedAt", "")

        lines = [f"### [{title}]({url})", ""]
        meta_parts = [f"**来源**: {source}"]
        if subtype:
            meta_parts.append(f"**类型**: {subtype}")
        if favorited_at:
            dt = favorited_at[:10] if len(favorited_at) >= 10 else favorited_at
            meta_parts.append(f"**收藏于**: {dt}")
        lines.append(" · ".join(meta_parts))
        lines.append("")

        if summary:
            lines.append(summary)
            lines.append("")

        badges = []
        if arxiv_url:
            badges.append(f"[arXiv]({arxiv_url})")
        if github_url:
            badges.append(f"[GitHub]({github_url})")
        if badges:
            lines.append(" · ".join(badges))
            lines.append("")

        if key_points:
            for p in key_points:
                lines.append(f"- {p}")
            lines.append("")

        return "\n".join(lines)

    def write_standalone_html(
        self,
        favorites_json_path: str,
        output_filename: str = "favorites.html",
        title: str = "My Digest Favorites"
    ) -> str:
        with open(favorites_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if "articles" not in data:
            raise ValueError("Invalid favorites JSON: missing 'articles' key")

        articles = data.get("articles", {})
        folders = data.get("folders", [])
        total = len(articles)

        generated_at = datetime.now()

        # Group articles by folder
        by_folder = {}  # folderId -> [article_data]
        uncategorized = []

        for url, article in articles.items():
            article["_url"] = url
            fid = article.get("folderId")
            if fid and any(f["id"] == fid for f in folders):
                by_folder.setdefault(fid, []).append(article)
            else:
                uncategorized.append(article)

        # Sort each group by favoritedAt desc
        def sort_key(a):
            return a.get("favoritedAt", "")

        uncategorized.sort(key=sort_key, reverse=True)
        for fid in by_folder:
            by_folder[fid].sort(key=sort_key, reverse=True)

        parts = [
            "<!DOCTYPE html>",
            '<html lang="zh-CN" data-theme="dark">',
            "<head>",
            '<meta charset="UTF-8">',
            '<meta name="viewport" content="width=device-width,initial-scale=1">',
            f"<title>{html.escape(title)}</title>",
            "<style>",
            _FAVORITES_CSS,
            "</style>",
            "</head>",
            "<body>",
            # Sidebar
            '<aside class="sidebar">',
            '<div class="sidebar-brand">',
            '<div class="sidebar-logo">⭐</div>',
            f'<div class="sidebar-title"><span>收藏夹</span> {html.escape(title)}</div>',
            '</div>',
            '<nav class="sidebar-nav">',
            '<div class="sidebar-label">文件夹</div>',
            f'<a class="sidebar-link active" data-folder-id="all" href="#">全部<span class="sidebar-count">{total}</span></a>',
        ]

        for fid in [None] + [f["id"] for f in folders]:
            if fid is None:
                folder_name = "未分类"
                folder_id = "__uncategorized__"
                count = len(uncategorized)
                if count == 0:
                    continue
            else:
                folder = next((f for f in folders if f["id"] == fid), None)
                if not folder:
                    continue
                folder_name = folder["name"]
                folder_id = folder["id"]
                count = len(by_folder.get(fid, []))

            parts.append(
                f'<a class="sidebar-link" data-folder-id="{html.escape(folder_id)}" href="#">'
                f'{html.escape(folder_name)}'
                f'<span class="sidebar-count">{count}</span>'
                '</a>'
            )

        parts.append('</nav>')
        parts.append(
            '<div class="sidebar-footer">'
            f'共 {total} 篇 · {generated_at.strftime("%Y-%m-%d")}'
            '</div>'
        )
        parts.append('</aside>')

        # Main content
        parts.append('<div class="main">')
        # Topbar
        parts.append('<div class="topbar"><div class="topbar-inner">')
        parts.append(f'<div class="topbar-title">⭐ {html.escape(title)}</div>')
        parts.append(f'<span class="topbar-stats">{total} 篇文章</span>')
        parts.append('<button id="theme-toggle" class="topbar-btn" title="切换主题">☀️</button>')
        parts.append('<button id="back-top" class="topbar-btn" title="回到顶部">↑</button>')
        parts.append('</div></div>')

        # Content
        parts.append('<div class="content">')

        if total == 0:
            parts.append(
                '<div class="empty-state">'
                '<h2>暂无收藏</h2>'
                '<p>在日报中点击文章卡片右上角的 ☆ 按钮收藏文章，然后导出 JSON 在此查看。</p>'
                '</div>'
            )
        else:
            # Render each folder section
            for fid in [None] + [f["id"] for f in folders]:
                if fid is None:
                    folder_name = "未分类"
                    folder_id = "__uncategorized__"
                    arts = uncategorized
                else:
                    folder = next((f for f in folders if f["id"] == fid), None)
                    if not folder:
                        continue
                    folder_name = folder["name"]
                    folder_id = folder["id"]
                    arts = by_folder.get(fid, [])

                if not arts:
                    continue

                parts.append(
                    f'<section class="folder-section" data-folder-id="{html.escape(folder_id)}">'
                    f'<h2 class="folder-header">'
                    f'<span class="folder-dot"></span>'
                    f'{html.escape(folder_name)}'
                    f'</h2>'
                    f'<div class="article-grid">'
                )

                for article in arts:
                    parts.append(self._render_article_card(article))

                parts.append('</div></section>')

        parts.append('</div>')  # /.content
        parts.append(
            '<footer class="page-footer">'
            f'Generated at {generated_at.strftime("%Y-%m-%d %H:%M")}'
            f' · {total} articles'
            '</footer>'
        )
        parts.append('</div>')  # /.main

        parts.append("<script>")
        parts.append(_FAVORITES_JS)
        parts.append("</script>")
        parts.append("</body>")
        parts.append("</html>")

        os.makedirs(self.output_dir, exist_ok=True)
        output_path = os.path.join(self.output_dir, output_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(parts))

        return output_path

    def _render_article_card(self, article: dict) -> str:
        title = article.get("title", "")
        url = article.get("url", article.get("_url", ""))
        source = article.get("source", "")
        summary = article.get("summary", "")
        key_points = article.get("keyPoints", [])
        arxiv_url = article.get("arxivUrl", "")
        github_url = article.get("githubUrl", "")
        subtype = article.get("subtype", "")

        lines = [
            '<article class="article-card">',
            f'<div class="article-title"><a href="{html.escape(url)}" target="_blank" rel="noopener">{html.escape(title)}</a></div>',
            '<div class="article-meta">'
            f'<span class="article-source">{html.escape(source)}</span>',
        ]
        if subtype:
            lines.append(f'<span class="article-subtype">{html.escape(subtype)}</span>')
        lines.append('</div>')
        lines.append(f'<div class="article-summary">{html.escape(summary)}</div>')

        # Badges
        badges = []
        if arxiv_url:
            badges.append(
                f'<a href="{html.escape(arxiv_url)}" class="badge arxiv" target="_blank" rel="noopener">arXiv</a>'
            )
        if github_url:
            badges.append(
                f'<a href="{html.escape(github_url)}" class="badge github" target="_blank" rel="noopener">GitHub</a>'
            )
        if badges:
            lines.append(f'<div class="article-badges">{"".join(badges)}</div>')

        if key_points:
            points = "".join(f"<li>{html.escape(p)}</li>" for p in key_points)
            lines.append(f'<div class="article-points"><ul>{points}</ul></div>')

        lines.append("</article>")
        return "\n".join(lines)
