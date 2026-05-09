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


def test_digest_and_thinking_defaults():
    config_content = """
rss_sources: []
claude:
  api_key: "test-key"
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

    assert config.digest.recent_days == 3
    assert config.digest.cache_path == ".cache/digest_me_cache.json"
    assert config.digest.classification_batch_size == 30
    assert config.digest.prompts_module == "prompts_ai_digest"
    assert config.claude.thinking == "disabled"
    os.unlink(f.name)


def test_digest_and_thinking_overrides():
    config_content = """
rss_sources: []
claude:
  api_key: "test-key"
  base_url: ""
  model: "test"
  thinking: "enabled"
digest:
  recent_days: 5
  cache_path: ".cache/custom.json"
  classification_batch_size: 10
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

    assert config.digest.recent_days == 5
    assert config.digest.cache_path == ".cache/custom.json"
    assert config.digest.classification_batch_size == 10
    assert config.digest.prompts_module == "prompts_ai_digest"
    assert config.claude.thinking == "enabled"
    os.unlink(f.name)


def test_deepseek_model_name_is_configurable():
    config_content = """
rss_sources: []
claude:
  api_key: "test-key"
  base_url: "https://api.deepseek.com/anthropic"
  model: "deepseek-v4-flash"
  thinking: "disabled"
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

    assert config.claude.model == "deepseek-v4-flash"
    os.unlink(f.name)


def test_default_model_is_deepseek_flash():
    config_content = """
rss_sources: []
claude:
  api_key: "test-key"
  base_url: "https://api.deepseek.com/anthropic"
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

    assert config.claude.model == "deepseek-v4-flash"
    os.unlink(f.name)
