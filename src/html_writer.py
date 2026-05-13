import html
import os
from datetime import datetime
from typing import List, Optional
from src.summarizer import ArticleSummary, TrendSummary


_CSS = r"""
:root {
    --sidebar-w: 260px;
    --topbar-h: 56px;
    --primary: #6366f1;
    --primary-light: #818cf8;
    --primary-dark: #4f46e5;
    --primary-bg: #ede4d6;
    --accent: #8b5cf6;
    --accent-light: #f5efe3;
    --bg: #f5f0e5;
    --surface: #fefcf5;
    --border: #e5ddd0;
    --text: #2c2416;
    --text-secondary: #6b5d4e;
    --text-muted: #a09888;
    --shadow: 0 1px 3px rgba(0,0,0,.05);
    --shadow-hover: 0 8px 24px rgba(139,92,246,.10);
    --shadow-card: 0 2px 8px rgba(0,0,0,.04), 0 1px 2px rgba(0,0,0,.05);
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
    --primary-bg: #2a2744;
    --accent: #cba6f7;
    --accent-light: #2a2744;
    --bg: #1e1e2e;
    --surface: #313244;
    --border: #45475a;
    --text: #cdd6f4;
    --text-secondary: #a6adc8;
    --text-muted: #6c7086;
    --shadow: 0 1px 3px rgba(0,0,0,.4);
    --shadow-hover: 0 8px 24px rgba(203,166,247,.18);
    --shadow-card: 0 2px 8px rgba(0,0,0,.35);
    --card-hl: linear-gradient(135deg, #313244 0%, #2a2744 50%, #36304a 100%);
    --card-normal: linear-gradient(135deg, #313244 0%, #2d2f40 100%);
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

/* ===== SIDEBAR ===== */
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
    display: flex; align-items: center; gap: 10px;
    flex-shrink: 0;
}
.sidebar-logo {
    width: 36px; height: 36px; border-radius: 10px;
    background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
    flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
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
    transition: all .15s; cursor: pointer;
    margin-bottom: 2px;
}
.sidebar-link:hover { background: var(--primary-bg); color: var(--primary); }
.sidebar-link.active { background: var(--primary-bg); color: var(--primary); font-weight: 600; }
.sidebar-count {
    margin-left: auto; font-size: 12px; font-weight: 600;
    background: var(--primary-bg); color: var(--primary);
    padding: 1px 8px; border-radius: 10px; min-width: 24px; text-align: center;
}
.sidebar-link.active .sidebar-count { background: var(--primary); color: #fff; }

/* Sidebar Category Group (expandable) */
.sidebar-cat-group { margin-bottom: 2px; }
.sidebar-cat-header {
    display: flex; align-items: center; gap: 8px;
    padding: 10px 12px; border-radius: var(--radius-sm);
    color: var(--text-secondary);
    font-size: 14px; font-weight: 500;
    transition: all .15s; cursor: pointer;
    user-select: none;
}
.sidebar-cat-header:hover { background: var(--primary-bg); color: var(--primary); }
.sidebar-cat-header.active { background: var(--primary-bg); color: var(--primary); font-weight: 600; }
.sidebar-cat-header.active .sidebar-count { background: var(--primary); color: #fff; }

.sidebar-cat-arrow {
    width: 16px; height: 16px; flex-shrink: 0;
    transition: transform .2s;
    display: inline-block; position: relative;
}
.sidebar-cat-arrow::before {
    content: ""; position: absolute; top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 0; height: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 6px solid var(--text-muted);
    transition: transform .2s;
}
.sidebar-cat-group.open .sidebar-cat-arrow::before {
    transform: translate(-50%, -50%) rotate(0deg);
}
.sidebar-cat-group:not(.open) .sidebar-cat-arrow::before {
    transform: translate(-50%, -50%) rotate(-90deg);
}

.sidebar-sub-list {
    overflow: hidden;
    transition: max-height .3s ease, opacity .2s;
}
.sidebar-cat-group.open .sidebar-sub-list {
    max-height: 300px; opacity: 1;
}
.sidebar-cat-group:not(.open) .sidebar-sub-list {
    max-height: 0; opacity: 0;
}

.sidebar-sub-link {
    display: flex; align-items: center; gap: 10px;
    padding: 7px 12px 7px 36px;
    border-radius: var(--radius-sm);
    color: var(--text-secondary); text-decoration: none;
    font-size: 13px; font-weight: 400;
    transition: all .15s; cursor: pointer;
    margin-bottom: 1px;
}
.sidebar-sub-link:hover { background: var(--primary-bg); color: var(--primary); }
.sidebar-sub-link.active { background: var(--primary-bg); color: var(--primary); font-weight: 600; }
.sidebar-sub-link.active .sidebar-count { background: var(--primary); color: #fff; }

.sidebar-footer {
    padding: 12px 24px; border-top: 1px solid var(--border);
    font-size: 12px; color: var(--text-muted); flex-shrink: 0;
}

/* Sidebar resize handle */
.sidebar-resize {
    position: absolute; top: 0; right: 0; bottom: 0;
    width: 5px; cursor: col-resize; z-index: 10;
    background: transparent;
    transition: background .2s;
}
.sidebar-resize:hover,
.sidebar-resize.dragging {
    background: var(--primary);
}
.sidebar.resizing { user-select: none; pointer-events: none; }

/* Sidebar toggle for mobile */
.sidebar-toggle {
    display: none; position: fixed; top: 12px; left: 12px; z-index: 300;
    width: 40px; height: 40px; border-radius: var(--radius-sm);
    background: var(--surface); border: 1px solid var(--border);
    font-size: 20px; cursor: pointer; align-items: center; justify-content: center;
    box-shadow: var(--shadow);
}

/* ===== MAIN ===== */
.main {
    margin-left: var(--sidebar-w);
    min-height: 100vh;
}

/* ===== TOP BAR ===== */
.topbar {
    position: sticky; top: 0; z-index: 100;
    background: var(--bg); backdrop-filter: blur(12px);
    padding: 12px 0; border-bottom: 1px solid transparent;
}
.topbar.scrolled { border-bottom-color: var(--border); }
.topbar-inner {
    max-width: 1100px; margin: 0 auto; padding: 0 32px;
    display: flex; align-items: center; gap: 12px;
}
.topbar-search {
    flex: 1; position: relative;
}
.topbar-search input {
    width: 100%; padding: 10px 16px 10px 40px;
    border: 1px solid var(--border); border-radius: 24px;
    font-size: 14px; font-family: var(--font);
    background: var(--surface); color: var(--text);
    outline: none; transition: all .2s;
}
.topbar-search input:focus { border-color: var(--primary); box-shadow: 0 0 0 3px var(--primary-bg); }
.topbar-search-icon {
    position: absolute; left: 14px; top: 50%; transform: translateY(-50%);
    color: var(--text-muted); font-size: 16px; pointer-events: none;
}
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

/* ===== CONTENT AREA ===== */
.content { max-width: 1100px; margin: 0 auto; padding: 0 32px 60px; }

/* Category Section */
.category-section { margin-bottom: 48px; scroll-margin-top: 80px; }
.category-header {
    display: flex; align-items: center; gap: 12px;
    font-size: 22px; font-weight: 800; margin-bottom: 20px;
}
.category-dot {
    width: 10px; height: 10px; border-radius: 50%;
    background: var(--primary); flex-shrink: 0;
}
.category-count {
    font-size: 14px; font-weight: 500; color: var(--text-muted);
    margin-left: 4px;
}

/* Trend Card */
.trend-card {
    background: linear-gradient(135deg, #fef3c7 0%, #fef9c3 100%);
    border: 1px solid #fcd34d; border-radius: var(--radius);
    margin-bottom: 24px; overflow: hidden;
}
[data-theme="dark"] .trend-card { background: linear-gradient(135deg, #313244 0%, #2a2744 100%); border-color: #cba6f7; }
.trend-card summary {
    padding: 16px 24px; cursor: pointer; font-weight: 700; font-size: 15px;
    user-select: none; color: #92400e; list-style: none;
    display: flex; align-items: center; gap: 8px;
}
[data-theme="dark"] .trend-card summary { color: #f9e2af; }
.trend-card summary::-webkit-details-marker { display: none; }
.trend-card summary::before {
    content: ""; display: inline-block; width: 20px; height: 20px;
    background: #f59e0b; border-radius: 4px; flex-shrink: 0;
    mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M10 2a6 6 0 016 6v3l2 4H2l2-4V8a6 6 0 016-6z'/%3E%3C/svg%3E");
    -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M10 2a6 6 0 016 6v3l2 4H2l2-4V8a6 6 0 016-6z'/%3E%3C/svg%3E");
}
.trend-body { padding: 0 24px 20px; font-size: 14px; color: #78350f; line-height: 1.8; }
[data-theme="dark"] .trend-body { color: #cdd6f4; }
.trend-body ul { margin-top: 10px; padding-left: 20px; }
.trend-body li { margin-bottom: 6px; }

/* Subtype Section */
.subtype-section { margin-bottom: 28px; scroll-margin-top: 80px; }
.subtype-header {
    font-size: 14px; font-weight: 700; color: var(--text-muted);
    margin-bottom: 14px; text-transform: uppercase; letter-spacing: .04em;
    padding-left: 4px;
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
.article-card.hidden { display: none; }

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
.badge.arxiv:hover { background: #fef2f2; box-shadow: 0 0 0 2px #fecaca; }
.badge.github { background: #f0f0f5; color: #333; border: 1px solid #d4d4d8; }
.badge.github:hover { background: #e4e4e7; }
[data-theme="dark"] .badge.arxiv { background: #3b1111; color: #fca5a5; border-color: #7f1d1d; }
[data-theme="dark"] .badge.github { background: #1f1f2e; color: #d4d4d8; border-color: #3f3f46; }

.article-points { font-size: 12px; color: var(--text-muted); }
.article-points ul { padding-left: 18px; }
.article-points li { margin-bottom: 3px; }
.article-points li::marker { color: var(--primary-light); }

/* Footer */
.page-footer {
    text-align: center; padding: 32px 32px 48px;
    font-size: 12px; color: var(--text-muted);
    border-top: 1px solid var(--border); margin-top: 20px;
}
.page-footer span { margin: 0 6px; }

/* ===== MOBILE ===== */
@media (max-width: 768px) {
    :root { --sidebar-w: 0px; }
    .sidebar {
        transform: translateX(-100%);
        transition: transform .25s;
        box-shadow: 4px 0 20px rgba(0,0,0,.15);
    }
    .sidebar.open { transform: translateX(0); width: 280px; }
    .sidebar-toggle { display: flex; }
    .main { margin-left: 0; }
    .article-grid { grid-template-columns: 1fr; }
    .topbar-inner { padding: 0 16px; }
    .content { padding: 0 16px 40px; }
    .category-header { font-size: 18px; }
}

/* Sidebar overlay for mobile */
.sidebar-overlay {
    display: none; position: fixed; inset: 0; background: rgba(0,0,0,.4);
    z-index: 199;
}
.sidebar-overlay.visible { display: block; }
"""


_JS = r"""
(function() {
    // ---- Theme toggle ----
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

    var searchInput = document.getElementById('search');
    var cards = document.querySelectorAll('.article-card');
    var sections = document.querySelectorAll('.category-section');
    var topbar = document.querySelector('.topbar');
    var backTop = document.getElementById('back-top');
    var sidebar = document.querySelector('.sidebar');
    var sidebarToggle = document.getElementById('sidebar-toggle');
    var sidebarOverlay = document.querySelector('.sidebar-overlay');
    var MAIN = document.querySelector('.main');

    // Cached node lists
    var catHeaders = document.querySelectorAll('.sidebar-cat-header');
    var subLinks = document.querySelectorAll('.sidebar-sub-link');
    var allLink = document.querySelector('.sidebar-link[data-category="all"]');

    // Search filter
    function doSearch() {
        var query = searchInput.value.toLowerCase().trim();
        cards.forEach(function(card) {
            var text = (card.getAttribute('data-search-text') || '').toLowerCase();
            var match = !query || text.indexOf(query) !== -1;
            card.classList.toggle('hidden', !match);
        });
        updateVisibility();
    }
    searchInput.addEventListener('input', doSearch);

    // ---- Sidebar category header toggle ----
    catHeaders.forEach(function(header) {
        header.addEventListener('click', function(e) {
            var group = this.parentElement;
            group.classList.toggle('open');
        });
    });

    // ---- Sidebar sub-link click -> scroll to subtype section ----
    subLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            var cat = this.getAttribute('data-category');
            var subtype = this.getAttribute('data-subtype');
            var target = document.querySelector(
                '.subtype-section[data-category="' + cat + '"][data-subtype="' + subtype + '"]'
            );
            if (target) {
                target.scrollIntoView({behavior: 'smooth', block: 'start'});
            }
            if (window.innerWidth <= 768) {
                sidebar.classList.remove('open');
                sidebarOverlay.classList.remove('visible');
            }
        });
    });

    // ---- "全部" link -> scroll to top ----
    if (allLink) {
        allLink.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({top: 0, behavior: 'smooth'});
            if (window.innerWidth <= 768) {
                sidebar.classList.remove('open');
                sidebarOverlay.classList.remove('visible');
            }
        });
    }

    // ---- Highlight active sidebar items on scroll ----
    var ticking = false;
    function updateActiveNav() {
        var scrollY = window.scrollY + 100;
        var activeCat = 'all';
        var activeSub = null;

        sections.forEach(function(section) {
            if (section.offsetTop <= scrollY) {
                activeCat = section.getAttribute('data-category');
                var subSecs = section.querySelectorAll('.subtype-section');
                subSecs.forEach(function(ss) {
                    if (ss.offsetTop <= scrollY) {
                        activeSub = ss.getAttribute('data-subtype');
                    }
                });
            }
        });

        // Highlight category headers & auto-expand active
        catHeaders.forEach(function(header) {
            var cat = header.getAttribute('data-category');
            var isActive = cat === activeCat;
            header.classList.toggle('active', isActive);
            if (isActive) {
                header.parentElement.classList.add('open');
            }
        });

        // Highlight subtype sub-links
        subLinks.forEach(function(link) {
            var cat = link.getAttribute('data-category');
            var sub = link.getAttribute('data-subtype');
            link.classList.toggle('active', cat === activeCat && sub === activeSub);
        });

        // "全部" link active when at top
        if (allLink) {
            allLink.classList.toggle('active', activeCat === 'all');
        }

        // Topbar shadow
        topbar.classList.toggle('scrolled', window.scrollY > 20);
    }
    window.addEventListener('scroll', function() {
        if (!ticking) {
            requestAnimationFrame(function() {
                updateActiveNav();
                ticking = false;
            });
            ticking = true;
        }
    });

    // Back to top
    backTop.addEventListener('click', function() {
        window.scrollTo({top: 0, behavior: 'smooth'});
    });

    // Mobile sidebar toggle
    sidebarToggle.addEventListener('click', function() {
        sidebar.classList.toggle('open');
        sidebarOverlay.classList.toggle('visible');
    });
    sidebarOverlay.addEventListener('click', function() {
        sidebar.classList.remove('open');
        sidebarOverlay.classList.remove('visible');
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        if (e.key === '/' && document.activeElement !== searchInput) {
            e.preventDefault();
            searchInput.focus();
        }
        if (e.key === 'Escape') {
            searchInput.blur();
            sidebar.classList.remove('open');
            sidebarOverlay.classList.remove('visible');
        }
    });

    function updateVisibility() {
        sections.forEach(function(section) {
            var vis = section.querySelectorAll('.article-card:not(.hidden)');
            section.style.display = vis.length > 0 ? '' : 'none';
            var subSecs = section.querySelectorAll('.subtype-section');
            subSecs.forEach(function(ss) {
                var sv = ss.querySelectorAll('.article-card:not(.hidden)');
                ss.style.display = sv.length > 0 ? '' : 'none';
            });
        });
    }

    // Sidebar resize
    var resizeHandle = document.getElementById('sidebar-resize');
    var resizeSidebar = document.getElementById('sidebar');
    var isResizing = false;
    var startX, startW;
    var MIN_W = 180, MAX_W = 500;

    resizeHandle.addEventListener('mousedown', function(e) {
        isResizing = true;
        startX = e.clientX;
        startW = resizeSidebar.offsetWidth;
        resizeSidebar.classList.add('resizing');
        resizeHandle.classList.add('dragging');
        document.body.style.cursor = 'col-resize';
        e.preventDefault();
    });

    document.addEventListener('mousemove', function(e) {
        if (!isResizing) return;
        var dx = e.clientX - startX;
        var newW = Math.max(MIN_W, Math.min(MAX_W, startW + dx));
        resizeSidebar.style.width = newW + 'px';
        MAIN.style.marginLeft = newW + 'px';
    });

    document.addEventListener('mouseup', function() {
        if (!isResizing) return;
        isResizing = false;
        resizeSidebar.classList.remove('resizing');
        resizeHandle.classList.remove('dragging');
        document.body.style.cursor = '';
        try { localStorage.setItem('digest-sidebar-w', resizeSidebar.offsetWidth); } catch(e) {}
    });

    // Restore sidebar width
    try {
        var savedW = parseInt(localStorage.getItem('digest-sidebar-w'));
        if (savedW >= MIN_W && savedW <= MAX_W) {
            resizeSidebar.style.width = savedW + 'px';
            MAIN.style.marginLeft = savedW + 'px';
        }
    } catch(e) {}

    // Highlight ~15% of cards for visual variety
    var allCards = document.querySelectorAll('.article-card');
    var hlCount = Math.round(allCards.length * 0.15);
    var indices = Array.from({length: allCards.length}, function(_, i) { return i; });
    for (var i = indices.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var t = indices[i]; indices[i] = indices[j]; indices[j] = t;
    }
    for (var k = 0; k < hlCount; k++) {
        if (allCards[indices[k]]) {
            allCards[indices[k]].classList.add('highlight');
        }
    }

    updateActiveNav();
})();
"""


class HTMLWriter:
    def __init__(self, base_dir: str, pages_url: str = ""):
        self.base_dir = base_dir
        self.pages_url = pages_url.rstrip("/") if pages_url else ""

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
        total_articles = sum(cat_counts.values())

        # Compute subtype counts per category for sidebar
        subtype_counts = {}
        for cat in all_categories:
            subtypes = articles_by_category.get(cat, {})
            subtype_counts[cat] = {sub: len(articles) for sub, articles in subtypes.items() if articles}

        parts = [
            "<!DOCTYPE html>",
            '<html lang="zh-CN" data-theme="dark">',
            "<head>",
            '<meta charset="UTF-8">',
            '<meta name="viewport" content="width=device-width,initial-scale=1">',
            f"<title>Clyde's Digest — {date_str}</title>",
            "<style>",
            _CSS,
            "</style>",
            "</head>",
            "<body>",
            # Mobile sidebar toggle
            '<button id="sidebar-toggle" class="sidebar-toggle" aria-label="菜单">☰</button>',
            '<div class="sidebar-overlay" id="sidebar-overlay"></div>',
            # ---- Sidebar ----
            '<aside class="sidebar" id="sidebar">',
            '<div class="sidebar-brand">',
            '<div class="sidebar-logo">D</div>',
            '<div class="sidebar-title"><span>Clyde\'s</span> Digest</div>',
            '</div>',
            '<nav class="sidebar-nav">',
            '<div class="sidebar-label">分类目录</div>',
            f'<a class="sidebar-link" data-category="all" href="#">全部<span class="sidebar-count">{total_articles}</span></a>',
        ]

        for cat in all_categories:
            count = cat_counts.get(cat, 0)
            if count == 0:
                continue
            sub_counts = subtype_counts.get(cat, {})
            parts.append(f'<div class="sidebar-cat-group open">')
            parts.append(
                f'<div class="sidebar-cat-header" data-category="{html.escape(cat)}" role="button" tabindex="0">'
                f'<span class="sidebar-cat-arrow"></span>'
                f'<span class="sidebar-cat-label">{html.escape(cat)}</span>'
                f'<span class="sidebar-count">{count}</span>'
                f'</div>'
            )
            parts.append(f'<div class="sidebar-sub-list">')
            for subtype, sub_count in sub_counts.items():
                parts.append(
                    f'<a class="sidebar-sub-link" data-category="{html.escape(cat)}" '
                    f'data-subtype="{html.escape(subtype)}" href="#">'
                    f'{html.escape(subtype)}'
                    f'<span class="sidebar-count">{sub_count}</span>'
                    f'</a>'
                )
            parts.append('</div>')
            parts.append('</div>')
        parts.append('</nav>')
        parts.append('<div class="sidebar-resize" id="sidebar-resize"></div>')
        parts.append(
            '<div class="sidebar-footer">'
            f'{generated_at.strftime("%Y-%m-%d %H:%M")}<br>'
            f'共 {total_articles} 篇 · {stats.get("token_total", 0):,} tokens'
            '</div>'
        )
        parts.append('</aside>')

        # ---- Main Content ----
        parts.append('<div class="main">')
        # Top bar
        parts.append('<div class="topbar"><div class="topbar-inner">')
        parts.append(
            '<div class="topbar-search">'
            '<span class="topbar-search-icon">🔍</span>'
            '<input type="text" id="search" placeholder="搜索标题、来源、摘要... (按 / 聚焦)">'
            '</div>'
        )
        parts.append(
            f'<span class="topbar-stats">{total_articles} 篇 · {stats.get("token_total", 0):,} tokens</span>'
        )
        parts.append(
            '<button id="theme-toggle" class="topbar-btn" title="切换主题">☀️</button>'
        )
        parts.append(
            '<button id="back-top" class="topbar-btn" title="回到顶部">↑</button>'
        )
        parts.append('</div></div>')

        # Content
        parts.append('<div class="content">')

        for category in all_categories:
            subtypes = articles_by_category.get(category, {})
            total_in_cat = sum(len(v) for v in subtypes.values())
            if total_in_cat == 0:
                continue
            parts.append(f'<section class="category-section" id="cat-{html.escape(category)}" data-category="{html.escape(category)}">')
            parts.append(
                f'<h2 class="category-header">'
                f'<span class="category-dot"></span>'
                f'{html.escape(category)}'
                f'<span class="category-count">· {total_in_cat} 篇</span>'
                f'</h2>'
            )

            trend = trends_by_category.get(category)
            if trend:
                parts.append(self._render_trend_card(trend))

            for subtype, articles in subtypes.items():
                if not articles:
                    continue
                parts.append(
                    f'<div class="subtype-section" data-category="{html.escape(category)}" '
                    f'data-subtype="{html.escape(subtype)}">'
                )
                parts.append(f'<h3 class="subtype-header">{html.escape(subtype)}</h3>')
                parts.append('<div class="article-grid">')
                for article in articles:
                    parts.append(self._render_article_card(article))
                parts.append('</div>')
                parts.append('</div>')

            parts.append('</section>')

        parts.append('</div>')
        parts.append(self._render_footer(generated_at, stats))
        parts.append('</div>')  # /.main

        parts.append("<script>")
        parts.append(_JS)
        parts.append("</script>")
        parts.append("</body>")
        parts.append("</html>")

        os.makedirs(self.base_dir, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(parts))

        return filepath

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
        pages_rel = f"{self.pages_url}/{rel_path}" if self.pages_url else rel_path

        total = stats.get("articles_summarized", 0)
        entry = (f"- [{time_str} HTML — {filename}]({pages_rel})"
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
