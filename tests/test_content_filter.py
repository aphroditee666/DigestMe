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

    with patch('anthropic.Anthropic') as mock_anthropic:
        mock_client = Mock()
        mock_response = Mock()
        mock_content = Mock()
        mock_content.text = "多模态大模型/大语言模型"
        mock_response.content = [mock_content]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        filter = ContentFilter(config)
        result = filter.classify(
            title="测试文章",
            source="测试来源"
        )

    assert result in ["AIGC视觉生成", "多模态大模型/大语言模型", "自动驾驶", "其他AI/深度学习领域相关", "其它"]