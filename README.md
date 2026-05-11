# DigestMe — RSS 资讯聚合摘要

[![DigestMe](https://github.com/aphroditee666/DigestMe/actions/workflows/digest.yml/badge.svg)](https://github.com/aphroditee666/DigestMe/actions/workflows/digest.yml)

📋 [查看AI摘要索引 →](output/README.md)

从 RSS 源抓取文章，AI 分类并生成摘要，输出 Markdown 日报。订阅什么领域完全由配置文件决定 — 财经、科技、学术、产品……你配什么源，它就推送什么。

## 安装

```bash
pip install -r requirements.txt
```

## 配置

编辑 `config.yaml`，配置 RSS 订阅源、分类体系、LLM API。

```yaml
# 订阅源：任何 RSS/Atom feed
rss_sources:
  - name: "来源名称"
    url: "https://example.com/feed.xml"

# LLM API（兼容 Anthropic 协议）
claude:
  api_key: "${YOUR_API_KEY}"     # 支持 ${ENV_VAR}，不硬编码密钥
  base_url: "https://api.deepseek.com/anthropic"
  model: "deepseek-v4-flash"
  thinking: "disabled"

# 摘要设置
digest:
  recent_days: 3
  cache_path: ".cache/digest_me_cache.json"

# 定时调度
schedule:
  days: ["monday", "thursday"]
  time: "09:00"
```

## 运行

```bash
python main.py --once                      # 单次运行
python main.py --once --config config/ci.yaml  # 指定配置
python main.py                             # 定时调度模式
```

## GitHub Actions 自动运行

每周一、三上午 10:00（北京时间）自动抓取、分类、摘要，结果推回仓库。

### 手动触发

1. 打开 [Actions 页面](https://github.com/aphroditee666/DigestMe/actions/workflows/digest.yml)
2. 点击 **Run workflow** → **Run workflow**

### 环境变量

在仓库 Settings → Secrets and variables → Actions 中配置：

| Secret | 说明 |
|---|---|
| `DEEPSEEK_API_KEY` | DeepSeek API 密钥 |
