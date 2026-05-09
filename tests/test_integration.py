# tests/test_integration.py
import os
import tempfile
from unittest.mock import Mock, patch
from src.config_loader import ConfigLoader
from src.rss_fetcher import RSSFetcher
from src.summarizer import Summarizer
from src.markdown_writer import MarkdownWriter
from src.claude_client import ClaudeConfig

class MockFeed:
    """Mock feed object that mimics feedparser.parse() return value"""
    def __init__(self, entries):
        self.entries = entries

def test_full_pipeline():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Use forward slashes to avoid YAML escape sequence issues on Windows
        config_content = f'''
rss_sources:
  - name: "TestChannel"
    url: "https://example.com/rss"
    category: "Multimodal"

claude:
  api_key: "test-key"
  base_url: ""
  model: "test-model"

output:
  base_dir: "{tmpdir.replace(chr(92), "/")}"

schedule:
  days: []
  time: "09:00"
'''
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
            f.write(config_content)
            config_path = f.name

        mock_entry = Mock()
        mock_entry.title = 'Test Article'
        mock_entry.link = 'https://example.com/article'
        mock_entry.published = 'Mon, 01 Jan 2026 10:00:00 GMT'

        mock_classify_response = "多模态大模型/大语言模型"

        mock_summary_response = """### Summary
This is test summary content.

### Key Points
- Point 1: Introduce test content
- Point 2: Analyze test results
- Point 3: Summarize test findings"""

        with patch('feedparser.parse') as mock_parse, \
             patch('anthropic.Anthropic') as mock_anthropic:

            mock_parse.return_value = MockFeed(entries=[mock_entry])

            mock_client = Mock()
            mock_response1 = Mock()
            mock_response1.content = [Mock(text=mock_classify_response)]
            mock_response2 = Mock()
            mock_response2.content = [Mock(text=mock_summary_response)]
            mock_client.messages.create.side_effect = [mock_response1, mock_response2]
            mock_anthropic.return_value = mock_client

            loader = ConfigLoader(config_path)
            config = loader.load()

            fetcher = RSSFetcher()
            articles = fetcher.fetch("TestChannel", "https://example.com/rss")

            summarizer = Summarizer(config.claude)
            writer = MarkdownWriter(config.output.base_dir)

            category = summarizer.classify_only(articles[0].title, articles[0].source)
            assert category == "多模态大模型/大语言模型"

            os.unlink(config_path)