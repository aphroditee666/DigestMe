# DigestMe — RSS 智能聚合摘要

[![DigestMe](https://github.com/aphroditee666/DigestMe/actions/workflows/digest.yml/badge.svg)](https://github.com/aphroditee666/DigestMe/actions/workflows/digest.yml)

从 RSS 源抓取文章，AI 自动分类 + 双层摘要，输出 Markdown + 可交互 HTML 日报。支持暗色/亮色切换、全文搜索、侧边栏分类导航。

![screenshot](docs/screenshot.png)

📋 [最新摘要索引 →](output/README.md)

## 安装

```bash
pip install -r requirements.txt
```

## 运行

```bash
python main.py --once                          # 单次抓取+摘要
python main.py --once --config config/xxx.yaml  # 指定配置
python main.py --render-only --config config/xxx.yaml  # 仅从缓存渲染
python main.py                                  # 定时调度模式
```

## 工作流程

```
RSS 抓取 → 标题粗分类(Phase1) → 缓存分流(Phase2) → 正文补全 → 批量摘要+正文精筛(Phase3) → 趋势总结 → 输出 MD + HTML
```

## 配置示例

```yaml
rss_sources:
  - name: "机器之心"
    url: "https://rsshub.app/wechat/sogou/almosthuman2014"
    category: "AIGC视觉生成"
    limit: 15
    enrich: true           # 正文补全开关

claude:                    # 兼容 Anthropic 协议的 LLM
  api_key: "${DEEPSEEK_API_KEY}"
  base_url: "https://api.deepseek.com/anthropic"
  model: "deepseek-v4-flash"

output:
  base_dir: "./output"
  output_format: "both"   # markdown | html | both
  pages_url: "https://xxx.github.io/repo/output"

schedule:
  days: ["monday", "thursday"]
  time: "09:00"
```

## GitHub Actions

每周一、三上午 10:00（北京时间）自动运行。需配置 Secrets：`DEEPSEEK_API_KEY`。
