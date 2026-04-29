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
    mock_response.content = [Mock(text="测试回复")]
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