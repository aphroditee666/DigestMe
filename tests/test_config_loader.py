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
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
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
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
        f.write(config_content)
        f.flush()
        loader = ConfigLoader(f.name)
        config = loader.load()

    assert config.claude.api_key == "env-key"
    os.unlink(f.name)
    del os.environ['TEST_API_KEY']