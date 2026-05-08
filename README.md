# 微信公众号资讯汇总系统

[![AI Digest](https://github.com/aphroditee666/ResearchFromWechat/actions/workflows/digest.yml/badge.svg)](https://github.com/aphroditee666/ResearchFromWechat/actions/workflows/digest.yml)

从微信公众号等 RSS 源抓取 AI 相关文章，AI 分类并生成摘要，输出 Markdown。

## 安装

```bash
pip install -r requirements.txt
```

## 配置

编辑 `config.yaml` 添加 RSS 源和 API 配置。

```yaml
claude:
  api_key: "${DEEPSEEK_API_KEY}"   # 支持环境变量，不硬编码密钥
  base_url: "https://api.deepseek.com/anthropic"
  model: "deepseek-v4-pro"
```

## 运行

```bash
# 单次运行（默认配置）
python main.py --once

# 指定配置文件
python main.py --once --config config/ci.yaml

# 定时调度模式（按 config 中 schedule 配置运行）
python main.py
```

## GitHub Actions 自动运行

每周一、三上午 10:00（北京时间）自动抓取、分类、摘要，结果推回仓库。

### 手动触发

1. 打开 [Actions 页面](https://github.com/aphroditee666/ResearchFromWechat/actions/workflows/digest.yml)
2. 点击 **Run workflow** → **Run workflow**

### 环境变量

在仓库 Settings → Secrets and variables → Actions 中配置：

| Secret | 说明 |
|---|---|
| `DEEPSEEK_API_KEY` | DeepSeek API 密钥 |

> workflow 文件：[`.github/workflows/digest.yml`](.github/workflows/digest.yml)
