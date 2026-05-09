# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Single run (fetches RSS → classifies → summarizes → writes markdown)
python main.py --once

# Run with custom config
python main.py --config path/to/config.yaml

# Run with persistent scheduler (weekly, per config.yaml schedule section)
python main.py

# Run all tests
pytest

# Run a single test file
pytest tests/test_rss_fetcher.py
```

## Architecture

Pipeline: `main.py` orchestrates **RSSFetcher → classification → Summarizer → MarkdownWriter**.

1. **`main.py`** — Entry point. Iterates RSS sources, skips urls that are empty strings. Dynamically loads prompts module specified by `digest.prompts_module` in config, passes it to Summarizer/TrendSummarizer.

2. **`src/config_loader.py`** — Parses `config.yaml`. Supports `${ENV_VAR}` expansion in config values. Defines `Config`, `RSSSource`, `ClaudeConfig`, `OutputConfig`, `ScheduleConfig` dataclasses.

3. **`src/rss_fetcher.py`** — Wraps `feedparser`. Extracts article content from `entry.content[0].value` (list), falls back to `entry.summary` (str), then `entry.description` (str). Returns `Article` dataclass with title/url/published/source/content.

4. **`src/summarizer.py`** — Calls Claude API for classification (single + batch) and summarization. Parses response into `ArticleSummary` with summary text, key points list, and optional arXiv URL. Accepts a prompts module via constructor (defaults to `prompts_ai_digest`).

5. **`src/prompts_ai_digest.py`** — Prompt templates (`CLASSIFICATION_PROMPT`, `SUMMARIZATION_PROMPT`) and category definitions (`CATEGORIES`, `CATEGORIES_TO_OUTPUT`). This is the current domain module; switch domain by changing `digest.prompts_module` in config and providing a new `prompts_<domain>.py`.

6. **`src/claude_client.py`** — Thin wrapper around `anthropic.Anthropic` SDK client. Lazy-initializes the client. `send_message()` takes a single user message and optional system prompt, returns the text response.

7. **`src/markdown_writer.py`** — Writes one markdown file per category to `output/<category>/YYYY-MM-DD-<category_slug>-digest.md`. Renders article titles as clickable links, includes arXiv URLs when present.

8. **`src/scheduler.py`** — Wraps the `schedule` library. `schedule_weekly()` registers per-day jobs, `run()` loops with `schedule.run_pending()` + 60s sleep.

## Configuration

The domain/focus is entirely determined by the RSS sources and categories in the config file. No domain logic is hardcoded — swap the config and you have a different digest (finance, tech, academia, etc.).

To add a new domain:
1. Create `src/prompts_<domain>.py` with `CATEGORIES`, `CATEGORIES_TO_OUTPUT`, and prompt functions
2. Set `digest.prompts_module: "prompts_<domain>"` in your config YAML

Claude API is configured to use DeepSeek's Anthropic-compatible endpoint (`https://api.deepseek.com/anthropic`).

## Output structure

```
output/
  2026-05-06-digest.md
  AI前沿/2026-05-06-AI前沿-digest.md
  基础研究/2026-05-06-基础研究-digest.md
```

## Notes

- `ClaudeConfig` dataclass is duplicated in both `config_loader.py:14` and `claude_client.py:6` — they should be kept in sync.
- Sources with empty `url: ""` in config.yaml are silently skipped at runtime.
- Tests use `unittest.mock` to patch the Anthropic client; integration tests expect mocked API responses.
- On Windows, set `PYTHONIOENCODING=utf-8` to avoid GBK encoding crashes with emoji/Chinese in output.
