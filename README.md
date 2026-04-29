# 微信公众号咨询汇总系统

从微信公众号订阅号抓取 AI/自动驾驶相关文章，AI 分类并生成摘要，输出 Markdown。

## 安装

```bash
pip install -r requirements.txt
```

## 配置

编辑 `config.yaml` 添加 RSS 源和 API 配置。

## 运行

```bash
# 设置 API Key
export CLAUDE_API_KEY="your-api-key"

# 单次运行
python main.py

# 查看帮助
python main.py --help
```
