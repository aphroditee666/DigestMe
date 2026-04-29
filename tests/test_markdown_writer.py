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