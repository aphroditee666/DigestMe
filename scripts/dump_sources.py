"""Parse merged_feeds.md and dump recent articles per source to output/tmp-check/."""
import sys
import os
import re
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rss_fetcher import RSSFetcher


def parse_merged_feeds(filepath: str) -> list[tuple[str, str, str]]:
    """Parse merged_feeds.md, return list of (category, name, url)."""
    sources = []
    current_category = ""
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            # Category headers: "## AI专题 (64)"
            m = re.match(r'^## (.+?) \(\d+\)', line)
            if m:
                current_category = m.group(1)
                continue
            # Source lines: "- [Name](url)"
            m = re.match(r'^- \[(.+?)\]\((.+?)\)', line)
            if m:
                name = m.group(1).strip()
                url = m.group(2).strip()
                sources.append((current_category, name, url))
    return sources


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    merged_path = os.path.join(project_dir, "docs", "RSS源", "ai_digest", "RSS订阅源", "merged_feeds.md")
    out_dir = os.path.join(project_dir, "output", "tmp-check")
    os.makedirs(out_dir, exist_ok=True)

    sources = parse_merged_feeds(merged_path)
    print(f"Parsed {len(sources)} sources")

    fetcher = RSSFetcher()
    cutoff = datetime.now() - timedelta(days=7)

    total_recent = 0
    success = 0
    failed = 0

    for category, name, url in sources:
        try:
            print(f"[{category}] {name} ...", end=" ", flush=True)
            articles = fetcher.fetch(name, url, limit=30)

            recent = []
            for a in articles:
                if a.published and a.published.replace(tzinfo=None) < cutoff:
                    continue
                recent.append(a)

            total_recent += len(recent)

            safe = re.sub(r'[\\/:*?"<>|]', '_', name)
            filename = f"{safe}.md"
            filepath = os.path.join(out_dir, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {name}\n\n")
                f.write(f"> 分类: {category}\n")
                f.write(f"> URL: {url}\n")
                f.write(f"> 近一周: {len(recent)} 篇 / 抓取: {len(articles)} 篇\n\n---\n\n")

                if not recent:
                    f.write("*(近一周无文章)*\n")
                else:
                    for i, a in enumerate(recent, 1):
                        pub_str = a.published.strftime("%Y-%m-%d %H:%M") if a.published else "未知"
                        f.write(f"## {i}. {a.title}\n\n")
                        f.write(f"- 日期: {pub_str}\n")
                        f.write(f"- 链接: {a.url}\n\n")
                        preview = a.content[:600] if a.content else "(无正文)"
                        f.write(f"```\n{preview}\n```\n\n---\n\n")

            print(f"{len(recent)} recent")
            success += 1

        except Exception as e:
            print(f"FAILED: {e}")
            # Write error file
            safe = re.sub(r'[\\/:*?"<>|]', '_', name)
            filepath = os.path.join(out_dir, f"{safe}.md")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {name}\n\n> 分类: {category}\n> URL: {url}\n\n**抓取失败:** {e}\n")
            failed += 1

    print(f"\nDone. success={success}, failed={failed}, total_recent={total_recent}")


if __name__ == "__main__":
    main()
