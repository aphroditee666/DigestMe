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


def test_write_all_adds_number_suffix_when_file_exists():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        existing_path = f.name
    base_dir = os.path.dirname(existing_path)
    generated_at = datetime(2026, 5, 9, 9, 0)
    first_path = os.path.join(base_dir, "2026-05-09-digest.md")
    second_path = os.path.join(base_dir, "2026-05-09-digest-1.md")
    try:
        os.replace(existing_path, first_path)
        writer = MarkdownWriter(base_dir)

        output_path = writer.write_all({}, {}, generated_at)

        assert output_path == second_path
        assert os.path.exists(first_path)
        assert os.path.exists(second_path)
    finally:
        for path in [first_path, second_path, existing_path]:
            if os.path.exists(path):
                os.unlink(path)


def test_write_adds_number_suffix_when_file_exists():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        existing_path = f.name
    base_dir = os.path.dirname(existing_path)
    category = "Category"
    category_dir = os.path.join(base_dir, category)
    os.makedirs(category_dir, exist_ok=True)
    generated_at = datetime(2026, 5, 9, 9, 0)
    first_path = os.path.join(category_dir, "2026-05-09-Category-digest.md")
    second_path = os.path.join(category_dir, "2026-05-09-Category-digest-1.md")
    try:
        os.replace(existing_path, first_path)
        writer = MarkdownWriter(base_dir)

        output_path = writer.write(category, [], generated_at)

        assert output_path == second_path
        assert os.path.exists(first_path)
        assert os.path.exists(second_path)
    finally:
        for path in [first_path, second_path, existing_path]:
            if os.path.exists(path):
                os.unlink(path)
        if os.path.exists(category_dir):
            os.rmdir(category_dir)
