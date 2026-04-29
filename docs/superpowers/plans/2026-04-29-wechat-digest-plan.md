# 微信公众号咨询汇总系统实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 实现从微信公众号 RSS 源抓取文章，通过 Claude API 分类并生成摘要，输出分类 Markdown 文件的定时任务工具

**Architecture:**
- 模块化设计：配置加载 → RSS 抓取 → AI 分类 → AI 摘要 → Markdown 输出
- 使用 feedparser 抓取 RSS
- 使用 Anthropic Claude API（第三方中转）进行内容分类和摘要生成
- Windows 本地运行，定时调度通过 schedule 库实现

**Tech Stack:** Python 3, feedparser, anthropic, pyyaml, python-dateutil, schedule

---

## 文件结构

```
wechat-digest/
├── config.yaml              # 配置文件
├── main.py                  # 主入口
├── src/
│   ├── __init__.py
│   ├── config_loader.py     # 配置加载
│   ├── rss_fetcher.py       # RSS 抓取
│   ├── content_filter.py     # AI 分类
│   ├── summarizer.py         # 摘要生成
│   ├── markdown_writer.py    # Markdown 输出
│   ├── scheduler.py          # 调度器
│   └── prompts.py           # Claude Prompt 模板
├── output/                  # Markdown 输出目录
│   ├── AIGC视觉生成/
│   ├── 多模态大模型/
│   ├── 自动驾驶/
│   └── 其他AI_深度学习领域相关/
├── logs/                    # 日志目录
├── tests/                   # 测试目录
│   ├── __init__.py
│   ├── test_config_loader.py
│   ├── test_rss_fetcher.py
│   ├── test_content_filter.py
│   ├── test_summarizer.py
│   └── test_markdown_writer.py
├── requirements.txt
└── README.md
```

---

## Task 1: 项目初始化

**Files:**
- Create: `wechat-digest/requirements.txt`
- Create: `wechat-digest/config.yaml`
- Create: `wechat-digest/README.md`
- Create: `wechat-digest/src/__init__.py`
- Create: `wechat-digest/tests/__init__.py`
- Create: `wechat-digest/output/.gitkeep`
- Create: `wechat-digest/logs/.gitkeep`

- [ ] **Step 1: 创建 requirements.txt**

```txt
feedparser>=6.0.0
anthropic>=0.20.0
pyyaml>=6.0
python-dateutil>=2.8.0
schedule>=1.2.0
```

- [ ] **Step 2: 创建 config.yaml**

```yaml
rss_sources:
  - name: "机器之心"
    url: "https://rsshub.app/wechat/mp/name/jiqizhixin"
    category: "多模态大模型"
  - name: "自动驾驶之心"
    url: "https://rsshub.app/wechat/mp/name/xxx"
    category: "自动驾驶"

categories:
  - "AIGC视觉生成"
  - "多模态大模型/大语言模型"
  - "自动驾驶"
  - "其他AI/深度学习领域相关"
  - "其它"

claude:
  api_key: "${CLAUDE_API_KEY}"
  base_url: "https://v2.aicodee.com"
  model: "MiniMax-M2.7-highspeed"

output:
  base_dir: "./output"

schedule:
  days: ["monday", "wednesday"]
  time: "09:00"
```

- [ ] **Step 3: 创建目录结构和 .gitkeep**

- [ ] **Step 4: 创建 README.md**

```markdown
# 微信公众号咨询汇总系统

从微信公众号订阅号抓取 AI/自动驾驶相关文章，AI 分类并生成摘要，输出 Markdown。

## 安装

```bash
pip install -r requirements.txt
```

## 配置

编辑 `config.yaml` 添加 RSS 源和 API 配置。

## 运行

```bash
# 设置 API Key
export CLAUDE_API_KEY="your-api-key"

# 单次运行
python main.py

# 查看帮助
python main.py --help
```
```

- [ ] **Step 5: 提交**

```bash
cd wechat-digest
git init
git add requirements.txt config.yaml README.md src/__init__.py tests/__init__.py output/.gitkeep logs/.gitkeep
git commit -m "feat: project scaffolding"
```

---

## Task 2: 配置加载器

**Files:**
- Create: `wechat-digest/src/config_loader.py`
- Create: `wechat-digest/tests/test_config_loader.py`

- [ ] **Step 1: 编写测试**

```python
# tests/test_config_loader.py
import os
import tempfile
from pathlib import Path
from src.config_loader import ConfigLoader

def test_load_config():
    config_content = """
rss_sources:
  - name: "测试号"
    url: "https://example.com/rss"
    category: "多模态大模型"

claude:
  api_key: "test-key"
  base_url: "https://api.test.com"
  model: "test-model"

output:
  base_dir: "./output"

schedule:
  days: ["monday"]
  time: "09:00"
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write(config_content)
        f.flush()
        loader = ConfigLoader(f.name)
        config = loader.load()

    assert len(config.rss_sources) == 1
    assert config.rss_sources[0].name == "测试号"
    assert config.claude.api_key == "test-key"
    assert config.claude.base_url == "https://api.test.com"
    os.unlink(f.name)

def test_expand_env_vars():
    os.environ['TEST_API_KEY'] = 'env-key'
    config_content = """
rss_sources: []
claude:
  api_key: "${TEST_API_KEY}"
  base_url: ""
  model: "test"
output:
  base_dir: "./output"
schedule:
  days: []
  time: "09:00"
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write(config_content)
        f.flush()
        loader = ConfigLoader(f.name)
        config = loader.load()

    assert config.claude.api_key == "env-key"
    os.unlink(f.name)
    del os.environ['TEST_API_KEY']
```

- [ ] **Step 2: 运行测试验证失败**

Run: `cd wechat-digest && pytest tests/test_config_loader.py -v`
Expected: FAIL - ConfigLoader not defined

- [ ] **Step 3: 实现配置加载器**

```python
# src/config_loader.py
import os
import re
import yaml
from dataclasses import dataclass, field
from typing import List

@dataclass
class RSSSource:
    name: str
    url: str
    category: str

@dataclass
class ClaudeConfig:
    api_key: str
    base_url: str
    model: str

@dataclass
class OutputConfig:
    base_dir: str

@dataclass
class ScheduleConfig:
    days: List[str]
    time: str

@dataclass
class Config:
    rss_sources: List[RSSSource]
    claude: ClaudeConfig
    output: OutputConfig
    schedule: ScheduleConfig

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
                category=src.get('category', '其它')
            )
            for src in data.get('rss_sources', [])
        ]

        claude_data = data.get('claude', {})
        claude = ClaudeConfig(
            api_key=self._expand_env_vars(claude_data.get('api_key', '')),
            base_url=claude_data.get('base_url', ''),
            model=claude_data.get('model', 'claude-sonnet-4-7')
        )

        output_data = data.get('output', {})
        output = OutputConfig(
            base_dir=output_data.get('base_dir', './output')
        )

        schedule_data = data.get('schedule', {})
        schedule = ScheduleConfig(
            days=schedule_data.get('days', []),
            time=schedule_data.get('time', '09:00')
        )

        return Config(
            rss_sources=rss_sources,
            claude=claude,
            output=output,
            schedule=schedule
        )

    def load(self) -> Config:
        with open(self.config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return self._parse_config(data)
```

- [ ] **Step 4: 运行测试验证通过**

Run: `cd wechat-digest && pytest tests/test_config_loader.py -v`
Expected: PASS

- [ ] **Step 5: 提交**

```bash
cd wechat-digest
git add src/config_loader.py tests/test_config_loader.py
git commit -m "feat: add config loader with env var expansion"
```

---

## Task 3: RSS 抓取器

**Files:**
- Create: `wechat-digest/src/rss_fetcher.py`
- Create: `wechat-digest/tests/test_rss_fetcher.py`

- [ ] **Step 1: 编写测试**

```python
# tests/test_rss_fetcher.py
import pytest
from unittest.mock import Mock, patch
from src.rss_fetcher import RSSFetcher, Article

def test_fetch_single_source():
    mock_feed = {
        'entries': [
            {
                'title': 'Test Article 1',
                'link': 'https://example.com/article1',
                'published': 'Mon, 01 Jan 2026 10:00:00 GMT'
            },
            {
                'title': 'Test Article 2',
                'link': 'https://example.com/article2',
                'published': 'Sun, 31 Dec 2025 10:00:00 GMT'
            }
        ]
    }

    with patch('feedparser.parse') as mock_parse:
        mock_parse.return_value = mock_feed
        fetcher = RSSFetcher()
        articles = fetcher.fetch('测试号', 'https://example.com/rss', limit=10)

    assert len(articles) == 2
    assert articles[0].title == 'Test Article 1'
    assert articles[0].url == 'https://example.com/article1'
    assert articles[0].source == '测试号'
    mock_parse.assert_called_once_with('https://example.com/rss')

def test_fetch_with_limit():
    mock_feed = {
        'entries': [
            {'title': f'Article {i}', 'link': f'https://example.com/{i}', 'published': 'Mon, 01 Jan 2026 10:00:00 GMT'}
            for i in range(20)
        ]
    }

    with patch('feedparser.parse') as mock_parse:
        mock_parse.return_value = mock_feed
        fetcher = RSSFetcher()
        articles = fetcher.fetch('测试号', 'https://example.com/rss', limit=5)

    assert len(articles) == 5

def test_fetch_empty_feed():
    mock_feed = {'entries': []}

    with patch('feedparser.parse') as mock_parse:
        mock_parse.return_value = mock_feed
        fetcher = RSSFetcher()
        articles = fetcher.fetch('测试号', 'https://example.com/rss')

    assert len(articles) == 0
```

- [ ] **Step 2: 运行测试验证失败**

Run: `cd wechat-digest && pytest tests/test_rss_fetcher.py -v`
Expected: FAIL - RSSFetcher not defined

- [ ] **Step 3: 实现 RSS 抓取器**

```python
# src/rss_fetcher.py
import feedparser
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from dateutil import parser as date_parser

@dataclass
class Article:
    title: str
    url: str
    published: Optional[datetime]
    source: str

    def to_dict(self):
        return {
            'title': self.title,
            'url': self.url,
            'published': self.published.isoformat() if self.published else None,
            'source': self.source
        }

class RSSFetcher:
    def fetch(self, source_name: str, url: str, limit: int = 10) -> List[Article]:
        feed = feedparser.parse(url)
        articles = []

        for entry in feed.entries[:limit]:
            title = entry.get('title', 'No Title')
            link = entry.get('link', '')
            published_str = entry.get('published', None)

            published = None
            if published_str:
                try:
                    published = date_parser.parse(published_str)
                except Exception:
                    published = None

            articles.append(Article(
                title=title,
                url=link,
                published=published,
                source=source_name
            ))

        return articles
```

- [ ] **Step 4: 运行测试验证通过**

Run: `cd wechat-digest && pytest tests/test_rss_fetcher.py -v`
Expected: PASS

- [ ] **Step 5: 提交**

```bash
cd wechat-digest
git add src/rss_fetcher.py tests/test_rss_fetcher.py
git commit -m "feat: add RSS fetcher"
```

---

## Task 4: Prompt 模板

**Files:**
- Create: `wechat-digest/src/prompts.py`

- [ ] **Step 1: 创建 Prompt 模板**

```python
# src/prompts.py

CATEGORIES = {
    "AIGC视觉生成": "图像生成/编辑、视频生成与编辑、3D生成与重建、SFT/强化学习/LORA等训练策略相关",
    "多模态大模型/大语言模型": "多模态大模型、大语言模型相关",
    "自动驾驶": "VLA/端到端/世界模型等自动驾驶相关",
    "其他AI/深度学习领域相关": "不属于前三类的AI/深度学习相关（如强化学习研究方向、NLP其他方向、AI安全等）",
    "其它": "不属于以上四类的内容"
}

CLASSIFICATION_PROMPT = """你是一个文章分类助手。请根据以下分类定义，判断文章属于哪个类别。

分类定义：
{category_definitions}

文章信息：
标题：{title}
来源：{source}

请只输出一个分类名称，不要输出其他内容。
输出选项：{category_list}
"""

SUMMARIZATION_PROMPT = """你是一个文章摘要助手。请为以下文章生成摘要和关键要点。

文章信息：
标题：{title}
来源：{source}
链接：{url}

请按以下格式输出：

### 摘要
{summary_text}

### 关键要点
- {key_point_1}
- {key_point_2}
- {key_point_3}

要求：
1. 摘要长度 50-150 字
2. 提供 3 个关键要点
3. 要点简洁，每条不超过 30 字
4. 用中文输出
"""

def get_classification_prompt(title: str, source: str, categories: list) -> str:
    category_definitions = "\n".join([
        f"- {name}: {desc}" for name, desc in CATEGORIES.items() if name != "其它"
    ])
    category_list = ", ".join([f'"{name}"' for name in categories])

    return CLASSIFICATION_PROMPT.format(
        category_definitions=category_definitions,
        title=title,
        source=source,
        category_list=category_list
    )

def get_summarization_prompt(title: str, source: str, url: str) -> str:
    return SUMMARIZATION_PROMPT.format(
        title=title,
        source=source,
        url=url,
        summary_text="[摘要内容]",
        key_point_1="[要点1]",
        key_point_2="[要点2]",
        key_point_3="[要点3]"
    )
```

- [ ] **Step 2: 提交**

```bash
cd wechat-digest
git add src/prompts.py
git commit -m "feat: add prompt templates for classification and summarization"
```

---

## Task 5: Claude API 客户端

**Files:**
- Create: `wechat-digest/src/claude_client.py`
- Create: `wechat-digest/tests/test_claude_client.py`

- [ ] **Step 1: 编写测试**

```python
# tests/test_claude_client.py
import pytest
from unittest.mock import Mock, patch
from src.claude_client import ClaudeClient, ClaudeConfig

def test_client_initialization():
    config = ClaudeConfig(
        api_key="test-key",
        base_url="https://api.test.com",
        model="test-model"
    )
    client = ClaudeClient(config)
    assert client.config.api_key == "test-key"
    assert client.config.base_url == "https://api.test.com"

def test_client_with_empty_base_url():
    config = ClaudeConfig(
        api_key="test-key",
        base_url="",
        model="test-model"
    )
    client = ClaudeClient(config)
    assert client.config.base_url == ""

@patch('anthropic.Anthropic')
def test_send_message(mock_anthropic):
    mock_client = Mock()
    mock_response = Mock()
    mock_response.content[0].text = "测试回复"
    mock_client.messages.create.return_value = mock_response
    mock_anthropic.return_value = mock_client

    config = ClaudeConfig(
        api_key="test-key",
        base_url="",
        model="test-model"
    )
    client = ClaudeClient(config)
    response = client.send_message("Hello")

    assert response == "测试回复"
    mock_client.messages.create.assert_called_once()
```

- [ ] **Step 2: 运行测试验证失败**

Run: `cd wechat-digest && pytest tests/test_claude_client.py -v`
Expected: FAIL - ClaudeClient not defined

- [ ] **Step 3: 实现 Claude 客户端**

```python
# src/claude_client.py
from dataclasses import dataclass
from typing import Optional
import anthropic

@dataclass
class ClaudeConfig:
    api_key: str
    base_url: str
    model: str

class ClaudeClient:
    def __init__(self, config: ClaudeConfig):
        self.config = config
        self._client = None

    def _get_client(self):
        if self._client is None:
            if self.config.base_url:
                self._client = anthropic.Anthropic(
                    api_key=self.config.api_key,
                    base_url=self.config.base_url
                )
            else:
                self._client = anthropic.Anthropic(
                    api_key=self.config.api_key
                )
        return self._client

    def send_message(self, message: str, system: Optional[str] = None) -> str:
        client = self._get_client()

        params = {
            "model": self.config.model,
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": message}]
        }

        if system:
            params["system"] = system

        response = client.messages.create(**params)
        return response.content[0].text
```

- [ ] **Step 4: 运行测试验证通过**

Run: `cd wechat-digest && pytest tests/test_claude_client.py -v`
Expected: PASS

- [ ] **Step 5: 提交**

```bash
cd wechat-digest
git add src/claude_client.py tests/test_claude_client.py
git commit -m "feat: add Claude API client"
```

---

## Task 6: 内容过滤器（分类）

**Files:**
- Create: `wechat-digest/src/content_filter.py`
- Create: `wechat-digest/tests/test_content_filter.py`

- [ ] **Step 1: 编写测试**

```python
# tests/test_content_filter.py
import pytest
from unittest.mock import Mock, patch
from src.content_filter import ContentFilter
from src.claude_client import ClaudeConfig

def test_filter_returns_category():
    config = ClaudeConfig(
        api_key="test-key",
        base_url="",
        model="test-model"
    )

    with patch('src.claude_client.Anthropic') as mock_anthropic:
        mock_client = Mock()
        mock_response = Mock()
        mock_response.content[0].text = "多模态大模型/大语言模型"
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        filter = ContentFilter(config)
        result = filter.classify(
            title="测试文章",
            source="测试来源"
        )

    assert result in ["AIGC视觉生成", "多模态大模型/大语言模型", "自动驾驶", "其他AI/深度学习领域相关", "其它"]
```

- [ ] **Step 2: 运行测试验证失败**

Run: `cd wechat-digest && pytest tests/test_content_filter.py -v`
Expected: FAIL - ContentFilter not defined

- [ ] **Step 3: 实现内容过滤器**

```python
# src/content_filter.py
from typing import List
from src.claude_client import ClaudeClient, ClaudeConfig
from src.prompts import get_classification_prompt, CATEGORIES

class ContentFilter:
    VALID_CATEGORIES = [
        "AIGC视觉生成",
        "多模态大模型/大语言模型",
        "自动驾驶",
        "其他AI/深度学习领域相关",
        "其它"
    ]

    def __init__(self, config: ClaudeConfig):
        self.client = ClaudeClient(config)

    def classify(self, title: str, source: str) -> str:
        prompt = get_classification_prompt(
            title=title,
            source=source,
            categories=self.VALID_CATEGORIES
        )

        response = self.client.send_message(prompt)
        response = response.strip()

        for category in self.VALID_CATEGORIES:
            if category in response:
                return category

        return "其它"
```

- [ ] **Step 4: 运行测试验证通过**

Run: `cd wechat-digest && pytest tests/test_content_filter.py -v`
Expected: PASS

- [ ] **Step 5: 提交**

```bash
cd wechat-digest
git add src/content_filter.py tests/test_content_filter.py
git commit -m "feat: add content filter for article classification"
```

---

## Task 7: 摘要生成器

**Files:**
- Create: `wechat-digest/src/summarizer.py`
- Create: `wechat-digest/tests/test_summarizer.py`

- [ ] **Step 1: 编写测试**

```python
# tests/test_summarizer.py
import pytest
from unittest.mock import Mock, patch
from src.summarizer import Summarizer, ArticleSummary
from src.claude_client import ClaudeConfig

def test_generate_summary():
    config = ClaudeConfig(
        api_key="test-key",
        base_url="",
        model="test-model"
    )

    summary_response = """### 摘要
这是一篇关于大语言模型的测试文章。

### 关键要点
- 要点1：介绍了大语言模型的基本概念
- 要点2：讨论了最新的研究进展
- 要点3：展望了未来的发展方向"""

    with patch('src.claude_client.Anthropic') as mock_anthropic:
        mock_client = Mock()
        mock_response = Mock()
        mock_response.content[0].text = summary_response
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        summarizer = Summarizer(config)
        result = summarizer.summarize(
            title="测试文章",
            source="测试来源",
            url="https://example.com/article"
        )

    assert isinstance(result, ArticleSummary)
    assert result.summary.startswith("这是一篇")
    assert len(result.key_points) == 3
```

- [ ] **Step 2: 运行测试验证失败**

Run: `cd wechat-digest && pytest tests/test_summarizer.py -v`
Expected: FAIL - Summarizer not defined

- [ ] **Step 3: 实现摘要生成器**

```python
# src/summarizer.py
import re
from dataclasses import dataclass
from typing import List
from src.claude_client import ClaudeClient, ClaudeConfig
from src.prompts import get_summarization_prompt

@dataclass
class ArticleSummary:
    title: str
    url: str
    source: str
    summary: str
    key_points: List[str]

class Summarizer:
    def __init__(self, config: ClaudeConfig):
        self.client = ClaudeClient(config)

    def summarize(self, title: str, source: str, url: str) -> ArticleSummary:
        prompt = get_summarization_prompt(
            title=title,
            source=source,
            url=url
        )

        response = self.client.send_message(prompt)

        summary_match = re.search(r'### 摘要\s*\n(.+?)(?=### 关键要点|$)', response, re.DOTALL)
        summary = summary_match.group(1).strip() if summary_match else ""

        key_points = []
        points_match = re.findall(r'- (.+)', response)
        key_points = [p.strip() for p in points_match[:3]]

        return ArticleSummary(
            title=title,
            url=url,
            source=source,
            summary=summary,
            key_points=key_points
        )
```

- [ ] **Step 4: 运行测试验证通过**

Run: `cd wechat-digest && pytest tests/test_summarizer.py -v`
Expected: PASS

- [ ] **Step 5: 提交**

```bash
cd wechat-digest
git add src/summarizer.py tests/test_summarizer.py
git commit -m "feat: add summarizer for article summarization"
```

---

## Task 8: Markdown 输出器

**Files:**
- Create: `wechat-digest/src/markdown_writer.py`
- Create: `wechat-digest/tests/test_markdown_writer.py`

- [ ] **Step 1: 编写测试**

```python
# tests/test_markdown_writer.py
import os
import tempfile
from datetime import datetime
from src.markdown_writer import MarkdownWriter, ArticleSummary

def test_write_single_article():
    with tempfile.TemporaryDirectory() as tmpdir:
        writer = MarkdownWriter(tmpdir)

        article = ArticleSummary(
            title="测试文章",
            url="https://example.com/article",
            source="测试来源",
            summary="这是测试摘要。",
            key_points=["要点1", "要点2", "要点3"]
        )

        output_path = writer.write(
            category="多模态大模型",
            articles=[article],
            generated_at=datetime(2026, 4, 29, 9, 0)
        )

        assert os.path.exists(output_path)
        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()

        assert "测试文章" in content
        assert "https://example.com/article" in content
        assert "这是测试摘要" in content
        assert "要点1" in content

def test_create_category_directories():
    with tempfile.TemporaryDirectory() as tmpdir:
        writer = MarkdownWriter(tmpdir)

        writer.write(
            category="AIGC视觉生成",
            articles=[],
            generated_at=datetime.now()
        )

        category_dir = os.path.join(tmpdir, "AIGC视觉生成")
        assert os.path.exists(category_dir)
```

- [ ] **Step 2: 运行测试验证失败**

Run: `cd wechat-digest && pytest tests/test_markdown_writer.py -v`
Expected: FAIL - MarkdownWriter not defined

- [ ] **Step 3: 实现 Markdown 输出器**

```python
# src/markdown_writer.py
import os
from datetime import datetime
from typing import List
from src.summarizer import ArticleSummary

class MarkdownWriter:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir

    def _format_date(self, dt: datetime) -> str:
        return dt.strftime("%Y-%m-%d %H:%M")

    def _get_filename(self, category: str, dt: datetime) -> str:
        date_str = dt.strftime("%Y-%m-%d")
        category_slug = category.replace("/", "_").replace(" ", "_")
        return f"{date_str}-{category_slug}-digest.md"

    def _render_article(self, article: ArticleSummary) -> str:
        lines = [
            f"## [{article.title}]({article.url})",
            "",
            f"**来源:** {article.source}",
            "",
            "### 摘要",
            article.summary,
            "",
            "### 关键要点",
        ]

        for point in article.key_points:
            lines.append(f"- {point}")

        lines.append("")
        return "\n".join(lines)

    def write(self, category: str, articles: List[ArticleSummary], generated_at: datetime) -> str:
        category_dir = os.path.join(self.base_dir, category)
        os.makedirs(category_dir, exist_ok=True)

        filename = self._get_filename(category, generated_at)
        filepath = os.path.join(category_dir, filename)

        lines = [
            f"# {category}资讯汇总",
            "",
            f"> 生成时间: {self._format_date(generated_at)}",
            "",
            "---",
            ""
        ]

        for article in articles:
            lines.append(self._render_article(article))
            lines.append("---")
            lines.append("")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(lines))

        return filepath
```

- [ ] **Step 4: 运行测试验证通过**

Run: `cd wechat-digest && pytest tests/test_markdown_writer.py -v`
Expected: PASS

- [ ] **Step 5: 提交**

```bash
cd wechat-digest
git add src/markdown_writer.py tests/test_markdown_writer.py
git commit -m "feat: add markdown writer for output generation"
```

---

## Task 9: 调度器

**Files:**
- Create: `wechat-digest/src/scheduler.py`

- [ ] **Step 1: 实现调度器**

```python
# src/scheduler.py
import schedule
import time
from typing import Callable

class Scheduler:
    def __init__(self):
        self.jobs = []

    def _schedule_job(self, day: str, time_str: str, job_func: Callable):
        time_parts = time_str.split(":")
        hour = int(time_parts[0])
        minute = int(time_parts[1])

        if day == "monday":
            job = schedule.every().monday.at(f"{hour:02d}:{minute:02d}").do(job_func)
        elif day == "tuesday":
            job = schedule.every().tuesday.at(f"{hour:02d}:{minute:02d}").do(job_func)
        elif day == "wednesday":
            job = schedule.every().wednesday.at(f"{hour:02d}:{minute:02d}").do(job_func)
        elif day == "thursday":
            job = schedule.every().thursday.at(f"{hour:02d}:{minute:02d}").do(job_func)
        elif day == "friday":
            job = schedule.every().friday.at(f"{hour:02d}:{minute:02d}").do(job_func)
        elif day == "saturday":
            job = schedule.every().saturday.at(f"{hour:02d}:{minute:02d}").do(job_func)
        elif day == "sunday":
            job = schedule.every().sunday.at(f"{hour:02d}:{minute:02d}").do(job_func)

        self.jobs.append(job)

    def schedule_weekly(self, days: list, time_str: str, job_func: Callable):
        for day in days:
            self._schedule_job(day.lower(), time_str, job_func)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(60)
```

- [ ] **Step 2: 提交**

```bash
cd wechat-digest
git add src/scheduler.py
git commit -m "feat: add scheduler for periodic execution"
```

---

## Task 10: 主程序

**Files:**
- Create: `wechat-digest/main.py`

- [ ] **Step 1: 实现主程序**

```python
# main.py
import os
import sys
import argparse
import logging
from datetime import datetime
from pathlib import Path

from src.config_loader import ConfigLoader
from src.rss_fetcher import RSSFetcher
from src.content_filter import ContentFilter
from src.summarizer import Summarizer
from src.markdown_writer import MarkdownWriter
from src.scheduler import Scheduler

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

CATEGORIES_TO_OUTPUT = [
    "AIGC视觉生成",
    "多模态大模型/大语言模型",
    "自动驾驶",
    "其他AI/深度学习领域相关"
]

def run_once(config_path: str):
    loader = ConfigLoader(config_path)
    config = loader.load()

    logger.info(f"开始抓取 {len(config.rss_sources)} 个 RSS 源")

    fetcher = RSSFetcher()
    filter = ContentFilter(config.claude)
    summarizer = Summarizer(config.claude)
    writer = MarkdownWriter(config.output.base_dir)

    articles_by_category = {cat: [] for cat in CATEGORIES_TO_OUTPUT}

    for source in config.rss_sources:
        try:
            logger.info(f"抓取: {source.name}")
            articles = fetcher.fetch(source.name, source.url)

            for article in articles:
                try:
                    category = filter.classify(article.title, article.source)

                    if category in CATEGORIES_TO_OUTPUT:
                        logger.info(f"  分类为 {category}: {article.title}")

                        summary = summarizer.summarize(
                            title=article.title,
                            source=article.source,
                            url=article.url
                        )

                        articles_by_category[category].append(summary)
                    else:
                        logger.info(f"  跳过（{category}）: {article.title}")

                except Exception as e:
                    logger.error(f"  处理文章失败: {article.title}, 错误: {e}")
                    continue

        except Exception as e:
            logger.error(f"  抓取源失败: {source.name}, 错误: {e}")
            continue

    generated_at = datetime.now()
    for category, articles in articles_by_category.items():
        if articles:
            output_path = writer.write(category, articles, generated_at)
            logger.info(f"写入 {category} 文档: {output_path}")

    logger.info("完成")

def main():
    parser = argparse.ArgumentParser(description='微信公众号咨询汇总系统')
    parser.add_argument('--config', default='config.yaml', help='配置文件路径')
    parser.add_argument('--once', action='store_true', help='单次运行（不调度）')
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        logger.error(f"配置文件不存在: {config_path}")
        sys.exit(1)

    if args.once:
        run_once(str(config_path))
    else:
        loader = ConfigLoader(str(config_path))
        config = loader.load()

        scheduler = Scheduler()
        scheduler.schedule_weekly(
            config.schedule.days,
            config.schedule.time,
            lambda: run_once(str(config_path))
        )

        logger.info(f"调度已设置: 每周 {', '.join(config.schedule.days)} {config.schedule.time}")
        scheduler.run()

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: 提交**

```bash
cd wechat-digest
git add main.py
git commit -m "feat: add main program"
```

---

## Task 11: 集成测试

**Files:**
- Create: `wechat-digest/tests/test_integration.py`

- [ ] **Step 1: 编写集成测试**

```python
# tests/test_integration.py
import os
import tempfile
from unittest.mock import Mock, patch
from src.config_loader import ConfigLoader
from src.rss_fetcher import RSSFetcher
from src.content_filter import ContentFilter
from src.summarizer import Summarizer
from src.markdown_writer import MarkdownWriter
from src.claude_client import ClaudeConfig

def test_full_pipeline():
    with tempfile.TemporaryDirectory() as tmpdir:
        config_content = f"""
rss_sources:
  - name: "测试号"
    url: "https://example.com/rss"
    category: "多模态大模型"

claude:
  api_key: "test-key"
  base_url: ""
  model: "test-model"

output:
  base_dir: "{tmpdir.replace('\\\\', '\\\\\\\\')}"

schedule:
  days: []
  time: "09:00"
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(config_content)
            config_path = f.name

        mock_feed = {
            'entries': [
                {
                    'title': '测试文章',
                    'link': 'https://example.com/article',
                    'published': 'Mon, 01 Jan 2026 10:00:00 GMT'
                }
            ]
        }

        mock_classify_response = "多模态大模型/大语言模型"

        mock_summary_response = """### 摘要
这是测试摘要内容。

### 关键要点
- 要点1：介绍测试内容
- 要点2：分析测试结果
- 要点3：总结测试发现"""

        with patch('feedparser.parse') as mock_parse, \
             patch('anthropic.Anthropic') as mock_anthropic:

            mock_parse.return_value = mock_feed

            mock_client = Mock()
            mock_response1 = Mock()
            mock_response1.content[0].text = mock_classify_response
            mock_response2 = Mock()
            mock_response2.content[0].text = mock_summary_response
            mock_client.messages.create.side_effect = [mock_response1, mock_response2]
            mock_anthropic.return_value = mock_client

            loader = ConfigLoader(config_path)
            config = loader.load()

            fetcher = RSSFetcher()
            articles = fetcher.fetch("测试号", "https://example.com/rss")

            filter = ContentFilter(config.claude)
            summarizer = Summarizer(config.claude)
            writer = MarkdownWriter(config.output.base_dir)

            category = filter.classify(articles[0].title, articles[0].source)
            assert category == "多模态大模型/大语言模型"

            os.unlink(config_path)
```

- [ ] **Step 2: 运行集成测试**

Run: `cd wechat-digest && pytest tests/test_integration.py -v`
Expected: PASS

- [ ] **Step 3: 提交**

```bash
cd wechat-digest
git add tests/test_integration.py
git commit -m "test: add integration test"
```

---

## Task 12: 最终验证

- [ ] **Step 1: 运行所有测试**

Run: `cd wechat-digest && pytest tests/ -v`
Expected: 全部 PASS

- [ ] **Step 2: 验证项目结构**

```
wechat-digest/
├── config.yaml
├── main.py
├── src/
│   ├── __init__.py
│   ├── config_loader.py
│   ├── rss_fetcher.py
│   ├── content_filter.py
│   ├── summarizer.py
│   ├── markdown_writer.py
│   ├── scheduler.py
│   ├── prompts.py
│   └── claude_client.py
├── tests/
├── output/
├── logs/
├── requirements.txt
└── README.md
```

- [ ] **Step 3: 提交**

```bash
cd wechat-digest
git add -A
git commit -m "feat: complete wechat digest system"
```
