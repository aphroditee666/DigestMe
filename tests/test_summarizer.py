# tests/test_summarizer.py
import pytest
from unittest.mock import Mock, patch
from src.summarizer import Summarizer, ArticleSummary
from src.claude_client import ClaudeConfig
from src.prompts_ai_digest import clean_content

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


class TestCleanContent:
    def test_empty_input(self):
        assert clean_content("") == ""
        assert clean_content("   ") == ""
        assert clean_content(None) == ""

    def test_plain_text_passthrough(self):
        assert clean_content("这是一段纯文本内容") == "这是一段纯文本内容"

    def test_html_tag_stripping(self):
        result = clean_content("<p>Hello <b>world</b></p>")
        assert result == "Hello world"

    def test_entity_decoding(self):
        result = clean_content("A &amp; B &lt; C &gt; D")
        assert result == "A & B < C > D"

    def test_script_removal(self):
        result = clean_content("<script>alert('xss')</script><p>正文内容</p>")
        assert result == "正文内容"
        assert "alert" not in result

    def test_whitespace_collapse(self):
        result = clean_content("第一段\n\n  第二段\t\t第三段")
        assert result == "第一段 第二段 第三段"

    def test_truncate_at_cjk_punctuation(self):
        # 构造文本：前150个'B' + "。结尾句。" + 后100个'C'
        # 在truncated[:200]中，最后的"。"在位置155，155 > 100 (50%)，应在此截断
        text = "B" * 150 + "。结尾句。" + "C" * 100
        result = clean_content(text, max_len=200)
        assert result.endswith("。...")
        assert len(result) <= 203

    def test_truncate_no_boundary_falls_back_to_hard_cut(self):
        # 200字符内没有任何。！？，应硬截断
        text = "A" * 250
        result = clean_content(text, max_len=200)
        assert result.endswith("A...")
        assert len(result) == 203

    def test_short_text_no_truncation(self):
        result = clean_content("hi", max_len=2000)
        assert result == "hi"

    def test_whitespace_after_cleaning_is_empty(self):
        result = clean_content("<p>   </p><div></div>")
        assert result == ""

    def test_chinese_text_preserved(self):
        result = clean_content("<p>大语言模型在2024年取得重大突破</p>")
        assert "大语言模型" in result
        assert "2024" in result