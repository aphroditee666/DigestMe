# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Single run (fetch → classify → summarize → write MD+HTML)
python main.py --once --config config/ai_digest/config_ai_digest_outer_rss_merge_v0.yaml

# Re-render MD/HTML from cache only (no fetch, no LLM calls except trends)
python main.py --render-only --config path/to/config.yaml

# Run with persistent weekly scheduler
python main.py

# Run tests (uses unittest.mock for LLM calls)
pytest
```

On Windows, set `PYTHONIOENCODING=utf-8` to avoid GBK encoding crashes.

## Architecture

Pipeline in `main.py`:

```
RSS fetch → AI classify (batch) → filter by source type → full-text enrich → AI summarize (batch) → trend summaries → write MD + HTML
```

**Phase 1**: Fetch all RSS sources, dedup by URL (`seen_urls`), populate cache for previously seen articles, queue unseen for batch AI classification.

**Phase 2**: Filter classified articles by source type. Two kinds of sources:
- **Academic** (`category: "学术论文"` in config) — AI classifies freely, then only AIGC视觉生成 + 自动驾驶 are kept; rest discarded.
- **Non-academic** (category in CATEGORIES_TO_OUTPUT) — all 4 output categories kept; "其它" discarded.

**Phase 2.5**: Enrich short RSS content with full article body via `FullTextFetcher` (trafilatura-based).

**Phase 3**: Batch summarize pending articles. Single-article fallback if batch fails.

**Phase 4**: Trend summaries per category, then write MD + HTML. Output files named `YYYY-MM-DD-digest-N.md/.html` where N auto-increments.

### Key modules

| File | Purpose |
|------|---------|
| `main.py` | Orchestrator. `run_once()` for single run, `render_only()` for cache-only re-render. |
| `src/config_loader.py` | YAML config parsing. `${ENV_VAR}` expansion. `RSSSource.subtype` defaults to `SUBTYPE_TECH` when `enrich: true`. |
| `src/rss_fetcher.py` | `feedparser` wrapper. Supports custom fetcher registration per URL pattern. Returns `Article` dataclass. |
| `src/custom_fetcher.py` | Custom fetchers: arXiv API (replaces broken weekend RSS), Meta AI Blog (GraphQL auth flow). Registered via `register_all()`. |
| `src/summarizer.py` | `Summarizer` (classify + summarize) and `TrendSummarizer`. Batch and single-article modes. Parses JSON/structured text responses. |
| `src/prompts_ai_digest.py` | `CATEGORIES`, `CATEGORIES_TO_OUTPUT`, system prompts, and prompt templates. Domain-swappable via `digest.prompts_module` in config. |
| `src/claude_client.py` | Thin Anthropic SDK wrapper. Lazy init. Tracks token usage and call count via `client.stats`. |
| `src/digest_cache.py` | JSON file cache keyed by article URL. Stores category, subtype, summary, key_points, arxiv_url, github_url. |
| `src/full_text_fetcher.py` | Fetches full article HTML → trafilatura extract → replaces short RSS content. Supports custom site-specific fetchers. |
| `src/html_writer.py` | HTML output with sidebar nav, search, gradient cards, dark mode, resizable sidebar. |
| `src/markdown_writer.py` | Per-category markdown output. |
| `src/scheduler.py` | `schedule` library wrapper. Weekly jobs with day + time config. |

## Configuration

Domain determined entirely by `digest.prompts_module` + RSS sources in config. Key config fields:

```yaml
rss_sources:
  - name: "Source Name"
    url: "https://..."
    category: "AIGC视觉生成"   # "学术论文" = academic → filtered differently
    limit: 15
    enrich: true                # true → Tier 1 (full-text enrich + SUBTYPE_TECH)
    subtype: ""                 # auto: enrich=true → 技术/算法, false → 产品/应用
claude:
  api_key: "${DEEPSEEK_API_KEY}"
  base_url: "https://api.deepseek.com/anthropic"
digest:
  recent_days: 4
  classification_batch_size: 30
  summarization_batch_size: 5
  enable_trend_summary: true
  enrich_content: true
output:
  output_format: "both"  # "markdown", "html", or "both"
```

## Notes

- `ClaudeConfig` is duplicated in `config_loader.py` and `claude_client.py` — keep in sync.
- Sources with empty `url: ""` are silently skipped.
- Dedup is URL-based: `seen_urls` in `run_once()`, cache key in `render_only()`.
- arXiv API rate limit: 5s between calls, 3 retries on failure.
- Cache key priority: URL > `source::title` fallback.
