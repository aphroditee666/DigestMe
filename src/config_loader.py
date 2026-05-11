import os
import re
import yaml
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

SUBTYPE_TECH = "技术/算法"
SUBTYPE_PRODUCT = "产品/应用"


def _load_dotenv(path: str = ".env"):
    """Load KEY=VALUE pairs from a .env file into os.environ (no override)."""
    env_path = Path(path)
    if not env_path.is_file():
        return
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, _, value = line.partition("=")
            key, value = key.strip(), value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value

@dataclass
class RSSSource:
    name: str
    url: str
    category: str
    limit: int = 20
    enrich: bool = True
    subtype: str = ""

    def __post_init__(self):
        if not self.subtype:
            self.subtype = SUBTYPE_TECH if self.enrich else SUBTYPE_PRODUCT

@dataclass
class ClaudeConfig:
    api_key: str
    base_url: str
    model: str
    thinking: str = "disabled"

@dataclass
class OutputConfig:
    base_dir: str
    output_format: str = "both"  # "markdown" | "html" | "both"
    pages_url: str = ""  # GitHub Pages base URL, e.g. https://user.github.io/repo

@dataclass
class ScheduleConfig:
    days: List[str]
    time: str

@dataclass
class DigestConfig:
    recent_days: int = 3
    cache_path: str = ".cache/digest_me_cache.json"
    classification_batch_size: int = 30
    summarization_batch_size: int = 5
    enable_trend_summary: bool = True
    prompts_module: str = "prompts_ai_digest"
    enrich_content: bool = True
    enrich_min_chars: int = 500

@dataclass
class Config:
    rss_sources: List[RSSSource]
    claude: ClaudeConfig
    output: OutputConfig
    schedule: ScheduleConfig
    digest: DigestConfig = field(default_factory=DigestConfig)

class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path

    def _expand_env_vars(self, value: str) -> str:
        if isinstance(value, str):
            pattern = r'\$\{([^}]+)\}'
            matches = re.findall(pattern, value)
            for match in matches:
                env_value = os.environ.get(match, '')
                value = value.replace(f'${{{match}}}', env_value)
            return value
        return value

    def _parse_config(self, data: dict) -> Config:
        rss_sources = [
            RSSSource(
                name=src['name'],
                url=src['url'],
                category=src.get('category', '其它'),
                limit=src.get('limit', 10),
                enrich=src.get('enrich', True)
            )
            for src in data.get('rss_sources', [])
        ]

        claude_data = data.get('claude', {})
        claude = ClaudeConfig(
            api_key=self._expand_env_vars(claude_data.get('api_key', '')),
            base_url=claude_data.get('base_url', ''),
            model=claude_data.get('model', 'deepseek-v4-flash'),
            thinking=claude_data.get('thinking', 'disabled')
        )

        output_data = data.get('output', {})
        output = OutputConfig(
            base_dir=output_data.get('base_dir', './output'),
            pages_url=output_data.get('pages_url', ''),
            output_format=output_data.get('output_format', 'both')
        )

        schedule_data = data.get('schedule', {})
        schedule = ScheduleConfig(
            days=schedule_data.get('days', []),
            time=schedule_data.get('time', '09:00')
        )

        digest_data = data.get('digest', {})
        digest = DigestConfig(
            recent_days=digest_data.get('recent_days', 3),
            cache_path=digest_data.get('cache_path', '.cache/digest_me_cache.json'),
            classification_batch_size=digest_data.get('classification_batch_size', 30),
            summarization_batch_size=digest_data.get('summarization_batch_size', 5),
            enable_trend_summary=digest_data.get('enable_trend_summary', True),
            prompts_module=digest_data.get('prompts_module', 'prompts_ai_digest'),
            enrich_content=digest_data.get('enrich_content', False),
            enrich_min_chars=digest_data.get('enrich_min_chars', 500)
        )

        return Config(
            rss_sources=rss_sources,
            claude=claude,
            output=output,
            schedule=schedule,
            digest=digest
        )

    def load(self) -> Config:
        _load_dotenv()
        with open(self.config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return self._parse_config(data)
