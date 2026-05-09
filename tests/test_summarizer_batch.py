from unittest.mock import Mock, patch

from src.claude_client import ClaudeConfig
from src.summarizer import Summarizer


def test_summarize_sends_cleaned_truncated_content():
    config = ClaudeConfig(api_key="test-key", base_url="", model="test-model")
    long_content = "<p>" + ("A" * 2500) + "</p>"

    with patch('anthropic.Anthropic') as mock_anthropic:
        mock_client = Mock()
        mock_response = Mock()
        mock_response.content = [Mock(text="""### 鎽樿
Summary
### 鍏抽敭瑕佺偣
- Point""")]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        Summarizer(config).summarize(
            title="Title",
            source="Source",
            url="https://example.com/article",
            content=long_content
        )

    message = mock_client.messages.create.call_args.kwargs["messages"][0]["content"]
    assert "<p>" not in message
    assert "A" * 2000 in message
    assert "A" * 2100 not in message


def test_classify_batch_uses_single_call_and_parses_json():
    config = ClaudeConfig(api_key="test-key", base_url="", model="test-model")

    with patch('anthropic.Anthropic') as mock_anthropic:
        mock_client = Mock()
        mock_response = Mock()
        mock_response.content = [Mock(text='[{"index": 1, "category": "A"}, {"index": 2, "category": "B"}]')]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        result = Summarizer(config).classify_batch([
            {"index": 1, "title": "Title 1", "source": "Source"},
            {"index": 2, "title": "Title 2", "source": "Source"},
        ])

    assert result == {1: "A", 2: "B"}
    mock_client.messages.create.assert_called_once()


def test_classify_batch_extracts_json_array_from_wrapped_response():
    config = ClaudeConfig(api_key="test-key", base_url="", model="test-model")

    with patch('anthropic.Anthropic') as mock_anthropic:
        mock_client = Mock()
        mock_response = Mock()
        mock_response.content = [Mock(text='Here is the result:\n```json\n[{"index": 1, "category": "A"}]\n```')]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        result = Summarizer(config).classify_batch([
            {"index": 1, "title": "Title 1", "source": "Source"},
        ])

    assert result == {1: "A"}
