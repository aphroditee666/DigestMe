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


@patch('anthropic.Anthropic')
def test_send_message_disables_thinking_by_default(mock_anthropic):
    mock_client = Mock()
    mock_response = Mock()
    mock_response.content = [Mock(text="ok")]
    mock_client.messages.create.return_value = mock_response
    mock_anthropic.return_value = mock_client

    client = ClaudeClient(ClaudeConfig(api_key="test-key", base_url="", model="test-model"))
    client.send_message("Hello")

    params = mock_client.messages.create.call_args.kwargs
    assert params["thinking"] == {"type": "disabled"}


@patch('anthropic.Anthropic')
def test_send_message_does_not_force_disabled_thinking(mock_anthropic):
    mock_client = Mock()
    mock_response = Mock()
    mock_response.content = [Mock(text="ok")]
    mock_client.messages.create.return_value = mock_response
    mock_anthropic.return_value = mock_client

    config = ClaudeConfig(
        api_key="test-key",
        base_url="",
        model="test-model",
        thinking="enabled"
    )
    client = ClaudeClient(config)
    client.send_message("Hello")

    params = mock_client.messages.create.call_args.kwargs
    assert "thinking" not in params


@patch('anthropic.Anthropic')
def test_send_message_prefers_text_and_falls_back_to_thinking(mock_anthropic):
    mock_client = Mock()
    text_response = Mock()
    text_response.content = [Mock(text="text-value", thinking="thinking-value")]
    thinking_block = Mock()
    del thinking_block.text
    thinking_block.thinking = "thinking-only"
    thinking_response = Mock()
    thinking_response.content = [thinking_block]
    mock_client.messages.create.side_effect = [text_response, thinking_response]
    mock_anthropic.return_value = mock_client

    client = ClaudeClient(ClaudeConfig(api_key="test-key", base_url="", model="test-model"))

    assert client.send_message("Hello") == "text-value"
    assert client.send_message("Hello again") == "thinking-only"
