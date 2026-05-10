"""
Custom fetchers for sources without standard RSS feeds.
Each fetcher returns List[Article] compatible with RSSFetcher.

To add a new custom fetcher:
1. Implement a fetch_* function with signature (source_name, limit) -> List[Article]
2. Register it below with the URL pattern it should intercept
"""
import json
import re
import logging
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import URLError
from http.cookiejar import CookieJar

from dateutil import parser as date_parser

from .rss_fetcher import Article, RSSFetcher
from .full_text_fetcher import FullTextFetcher

logger = logging.getLogger(__name__)

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)


# ─── HTTP helpers ───────────────────────────────────────────────

def _http_get(url: str, headers: dict, cookiejar: CookieJar | None = None) -> str:
    req = Request(url, headers=headers)
    if cookiejar is not None:
        cookiejar.add_cookie_header(req)
    try:
        with urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
            if cookiejar is not None:
                cookiejar.extract_cookies(resp, req)
            return body
    except URLError as e:
        logger.error(f"HTTP GET failed for {url}: {e}")
        raise


def _http_post(url: str, headers: dict, data: dict, cookiejar: CookieJar | None = None) -> str:
    encoded = urlencode(data).encode("utf-8")
    headers["Content-Length"] = str(len(encoded))
    req = Request(url, data=encoded, headers=headers)
    if cookiejar is not None:
        cookiejar.add_cookie_header(req)
    try:
        with urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
            if cookiejar is not None:
                cookiejar.extract_cookies(resp, req)
            return body
    except URLError as e:
        logger.error(f"HTTP POST failed for {url}: {e}")
        raise


# ─── Meta AI Blog ───────────────────────────────────────────────
# Replicates RSSHub's /meta/ai/blog route.
# See: https://github.com/DIYgod/RSSHub/blob/master/lib/routes/meta/ai-blog.ts

META_AI_BLOG_URL = "https://ai.meta.com/blog/"
META_AI_GRAPHQL_URL = "https://ai.meta.com/api/graphql/"

META_AI_PAGE_HEADERS = {
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "User-Agent": USER_AGENT,
}


def _meta_ai_fetch_tokens(cookiejar: CookieJar) -> dict:
    html = _http_get(META_AI_BLOG_URL, META_AI_PAGE_HEADERS, cookiejar)
    tokens = {"LSD": {}, "SiteData": {}}

    lsd_match = re.search(r'"LSD",\[\],\{["\']token["\']:\s*["\']([^"\']+)', html)
    if lsd_match:
        tokens["LSD"]["token"] = lsd_match.group(1)

    spin_r_match = re.search(r'"__spin_r["\']:\s*(\d+)', html)
    spin_b_match = re.search(r'"__spin_b["\']:\s*["\']([^"\']+)', html)
    spin_t_match = re.search(r'"__spin_t["\']:\s*(\d+)', html)

    tokens["SiteData"]["__spin_r"] = int(spin_r_match.group(1)) if spin_r_match else 0
    tokens["SiteData"]["__spin_b"] = spin_b_match.group(1) if spin_b_match else "trunk"
    tokens["SiteData"]["__spin_t"] = (
        int(spin_t_match.group(1)) if spin_t_match
        else int(datetime.now().timestamp() * 1000)
    )
    return tokens


def _meta_ai_fetch_articles(cookiejar: CookieJar, tokens: dict, limit: int = 20) -> List[dict]:
    lsd_token = tokens.get("LSD", {}).get("token", "")
    site_data = tokens.get("SiteData", {})

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-asbd-id": "359341",
        "x-fb-friendly-name": "MetaAIBlogRecentPostSearchQuery",
        "x-fb-lsd": lsd_token,
        "User-Agent": USER_AGENT,
    }

    spin_t = site_data.get("__spin_t", int(datetime.now().timestamp() * 1000))
    spin_r = str(site_data.get("__spin_r", ""))

    body = {
        "av": "0",
        "__user": "0",
        "__a": "1",
        "__req": "1",
        "dpr": "1",
        "__ccg": "EXCELLENT",
        "__rev": spin_r,
        "lsd": lsd_token,
        "__spin_r": spin_r,
        "__spin_b": str(site_data.get("__spin_b", "trunk")),
        "__spin_t": str(spin_t),
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "MetaAIBlogRecentPostSearchQuery",
        "variables": json.dumps({
            "input": {
                "query": "",
                "from": 0,
                "limit": limit,
                "tags": [],
                "excludeObjectIDs": ["27568536916124137"],
            }
        }),
        "server_timestamps": "true",
        "doc_id": "9516719638450392",
    }

    text = _http_post(META_AI_GRAPHQL_URL, headers, body, cookiejar)
    if text.startswith("for (;;);"):
        text = text[len("for (;;);"):]
    data = json.loads(text)

    items = []
    for item in data.get("data", {}).get("query", []):
        items.append({
            "title": item.get("title", ""),
            "description": item.get("description", ""),
            "url": item.get("href", ""),
            "published": item.get("date", ""),
            "category": item.get("research_area", ""),
        })
    return items


def fetch_meta_ai_blog(source_name: str = "AI at Meta Blog", limit: int = 20) -> List[Article]:
    cookiejar = CookieJar()
    try:
        tokens = _meta_ai_fetch_tokens(cookiejar)
        items = _meta_ai_fetch_articles(cookiejar, tokens, limit=limit)

        articles = []
        for item in items:
            published = None
            if item.get("published"):
                try:
                    published = date_parser.parse(item["published"])
                except Exception:
                    pass

            articles.append(Article(
                title=item.get("title", "No Title"),
                url=item.get("url", ""),
                published=published,
                source=source_name,
                content=item.get("description", ""),
            ))

        logger.info(f"Meta AI Blog: fetched {len(articles)} articles")
        return articles

    except Exception as e:
        logger.error(f"Meta AI Blog fetch failed: {e}")
        return []


# ─── Meta AI Blog: single article page ──────────────────────────
# Used by FullTextFetcher to fetch full article HTML through the same
# cookie/token flow as the listing API.

# Simple module-level cache for tokens (TTL = 10 min)
_meta_token_cache: dict | None = None
_meta_token_cache_time: float = 0

def _meta_ai_get_token_cache(cookiejar: CookieJar) -> dict:
    global _meta_token_cache, _meta_token_cache_time
    now = datetime.now().timestamp()
    if _meta_token_cache is not None and (now - _meta_token_cache_time) < 600:
        return _meta_token_cache
    tokens = _meta_ai_fetch_tokens(cookiejar)
    _meta_token_cache = tokens
    _meta_token_cache_time = now
    return tokens


def _meta_ai_fetch_article_page(url: str) -> str | None:
    """Fetch a single Meta AI blog article page, returning full HTML."""
    cookiejar = CookieJar()
    try:
        _meta_ai_get_token_cache(cookiejar)
        return _http_get(url, META_AI_PAGE_HEADERS, cookiejar)
    except Exception as e:
        logger.error(f"Meta AI article page fetch failed for {url}: {e}")
        return None


# ─── arXiv API ───────────────────────────────────────────────────
# Replaces rss.arxiv.org RSS feeds (which return 0 entries on weekends)
# with the arXiv API that returns papers every weekday with full abstracts.

ARXIV_API_URL = "http://export.arxiv.org/api/query"
_ARXIV_LAST_CALL = 0.0

ARXIV_CATEGORY_MAP = {
    "AI": "cs.AI",
    "机器学习": "cs.LG",
    "计算机视觉": "cs.CV",
    "机器人": "cs.RO",
}


def fetch_arxiv_api(source_name: str, limit: int = 50) -> List[Article]:
    global _ARXIV_LAST_CALL

    cat = None
    for key, val in ARXIV_CATEGORY_MAP.items():
        if key in source_name:
            cat = val
            break
    if not cat:
        logger.warning(f"Cannot determine arXiv category for source: {source_name}")
        return []

    # Rate limit: at least 5s between arXiv API calls
    elapsed = time.time() - _ARXIV_LAST_CALL
    if elapsed < 5:
        time.sleep(5 - elapsed)

    params = {
        "search_query": f"cat:{cat}",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": str(limit),
    }
    url = f"{ARXIV_API_URL}?{urlencode(params)}"

    for attempt in range(3):
        try:
            req = Request(url, headers={"User-Agent": USER_AGENT})
            with urlopen(req, timeout=60) as resp:
                resp_text = resp.read().decode("utf-8", errors="replace")
            break
        except Exception as e:
            if attempt < 2:
                wait = (attempt + 1) * 5
                logger.warning(f"arXiv API failed ({cat}), retrying in {wait}s: {e}")
                time.sleep(wait)
            else:
                logger.error(f"arXiv API fetch failed for {cat}: {e}")
                return []

    root = ET.fromstring(resp_text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    articles = []
    for entry in root.findall("atom:entry", ns):
        title_el = entry.find("atom:title", ns)
        title = title_el.text.strip() if title_el is not None and title_el.text else "No Title"

        summary_el = entry.find("atom:summary", ns)
        summary = summary_el.text.strip() if summary_el is not None and summary_el.text else ""

        published_el = entry.find("atom:published", ns)
        published = None
        if published_el is not None and published_el.text:
            try:
                published = date_parser.parse(published_el.text)
            except Exception:
                pass

        id_el = entry.find("atom:id", ns)
        paper_url = id_el.text.strip() if id_el is not None and id_el.text else ""

        articles.append(Article(
            title=title,
            url=paper_url,
            published=published,
            source=source_name,
            content=summary,
        ))

    _ARXIV_LAST_CALL = time.time()
    logger.info(f"arXiv API ({cat}): fetched {len(articles)} articles")
    return articles


# ─── Registry ───────────────────────────────────────────────────

CUSTOM_FETCHERS = {
    "rsshub.app/meta/ai/blog": fetch_meta_ai_blog,
    "arxiv.org": fetch_arxiv_api,
}


def register_all():
    """Register every custom fetcher with the RSSFetcher dispatcher and FullTextFetcher."""
    for pattern, fn in CUSTOM_FETCHERS.items():
        RSSFetcher.register(pattern, fn)
    logger.info(f"Registered {len(CUSTOM_FETCHERS)} custom fetchers (RSSFetcher)")

    # Content enricher extensions: site-specific page fetchers that reuse auth logic
    FullTextFetcher.register("ai.meta.com/blog", _meta_ai_fetch_article_page)
    logger.info("Registered 1 content enricher extension")
