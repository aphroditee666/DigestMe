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

    with patch('anthropic.Anthropic') as mock_anthropic:
        mock_client = Mock()
        mock_response = Mock()
        mock_response.content = [Mock(text=summary_response)]
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