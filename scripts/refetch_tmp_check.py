"""
Re-fetch all sources in output/tmp-check/ and enrich short articles.
Pure HTTP + trafilatura — zero LLM calls, zero token consumption.

Usage: python -X utf8 scripts/refetch_tmp_check.py
"""
import sys
import io
import re
from pathlib import Path

# Fix Windows GBK encoding issues
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Ensure project root is in path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.rss_fetcher import RSSFetcher, Article
from src.full_text_fetcher import FullTextFetcher
from src.custom_fetcher import register_all

register_all()

TMP_CHECK = Path(__file__).resolve().parent.parent / "output" / "tmp-check"

# Matches: > URL: <url>
_URL_RE = re.compile(r'^>\s*URL:\s*(.+)$', re.MULTILINE)
# Matches: > 分类: <category>
_CAT_RE = re.compile(r'^>\s*分类:\s*(.+)$', re.MULTILINE)
# Matches: > 近一周: \d+ 篇 / 抓取: (\d+) 篇
_LIMIT_RE = re.compile(r'抓取:\s*(\d+)\s*篇')


def parse_md_header(filepath: Path) -> dict:
    """Extract source metadata from markdown header."""
    text = filepath.read_text(encoding='utf-8')

    url_match = _URL_RE.search(text)
    cat_match = _CAT_RE.search(text)
    limit_match = _LIMIT_RE.search(text)

    source_name = filepath.stem
    url = url_match.group(1).strip() if url_match else ""
    category = cat_match.group(1).strip() if cat_match else "其它"
    limit = int(limit_match.group(1)) if limit_match else 20

    return {
        "source_name": source_name,
        "url": url,
        "category": category,
        "limit": limit,
    }


def write_md(filepath: Path, meta: dict, articles: list[Article]):
    """Write fetched articles back to markdown file."""
    lines = []
    lines.append(f"# {meta['source_name']}")
    lines.append("")
    lines.append(f"> 分类: {meta['category']}")
    lines.append(f"> URL: {meta['url']}")
    lines.append(f"> 抓取: {len(articles)} 篇")
    lines.append("")
    lines.append("---")
    lines.append("")

    if not articles:
        lines.append("*(无文章)*")
        lines.append("")
        filepath.write_text("\n".join(lines), encoding='utf-8')
        return

    for i, article in enumerate(articles, 1):
        date_str = ""
        if article.published:
            from datetime import datetime
            if hasattr(article.published, 'strftime'):
                date_str = article.published.strftime("%Y-%m-%d %H:%M")
            else:
                date_str = str(article.published)

        lines.append(f"## {i}. {article.title}")
        lines.append("")
        if date_str:
            lines.append(f"- 日期: {date_str}")
        if article.url:
            lines.append(f"- 链接: {article.url}")
        lines.append("")
        lines.append("```")
        content = article.content if article.content else "(无正文)"
        lines.append(content)
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")

    filepath.write_text("\n".join(lines), encoding='utf-8')


def main():
    fetcher = RSSFetcher()
    enricher = FullTextFetcher(min_content_length=500)

    md_files = sorted(TMP_CHECK.glob("*.md"))
    total = len(md_files)
    enriched_count = 0
    total_articles = 0
    enriched_articles = 0

    for idx, md_file in enumerate(md_files, 1):
        try:
            meta = parse_md_header(md_file)
        except Exception as e:
            print(f"[{idx}/{total}] SKIP {md_file.name} — parse error: {e}")
            continue

        if not meta["url"]:
            print(f"[{idx}/{total}] SKIP {md_file.name} — no URL in header")
            continue

        source_name = meta['source_name']
        print(f"[{idx}/{total}] {source_name} ...", end=" ", flush=True)

        try:
            articles = fetcher.fetch(
                source_name, meta["url"], limit=meta["limit"]
            )
        except Exception as e:
            print(f"FETCH FAILED: {e}")
            continue

        total_articles += len(articles)

        # Enrich short articles
        src_enriched = 0
        for article in articles:
            before_len = len(article.content) if article.content else 0
            enriched = enricher.enrich(article)
            after_len = len(enriched.content) if enriched.content else 0
            if after_len > before_len:
                src_enriched += 1
        enriched_articles += src_enriched

        write_md(md_file, meta, articles)
        print(f"{len(articles)} articles, {src_enriched} enriched -> {md_file.name}")

    print(f"\nDone. {total} sources, {total_articles} articles, {enriched_articles} enriched.")


if __name__ == "__main__":
    main()
