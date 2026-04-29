# 微信公众号咨询汇总系统

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 从微信公众号订阅号抓取 AI/ML 和自动驾驶相关文章，通过 AI 过滤和摘要生成，定期汇总为本地 Markdown 文件（按五类分类：AIGC视觉生成/多模态大模型/自动驾驶/其他AI_深度学习/其它）

**Architecture:**
- 定时任务触发 RSS 抓取
- Claude API 判断内容相关性并生成摘要/要点
- Markdown 文件按五个主题分类输出（AIGC视觉生成 / 多模态大模型 / 自动驾驶 / 其他AI_深度学习 / 其它）

**内容分类定义：**
1. **AIGC 视觉生成**：图像生成/编辑、视频生成与编辑、3D生成与重建、SFT/强化学习/LORA等训练策略相关
2. **多模态大模型/大语言模型**
3. **自动驾驶**：VLA/端到端/世界模型等
4. **其他AI/深度学习领域相关**：不属于前三类的 AI/深度学习相关（如强化学习研究方向、NLP 其他方向、AI 安全等）
5. **其它**：不属于以上四类的内容（不输出）

**Tech Stack:** Python 3, feedparser, Anthropic Claude API, Windows Task Scheduler

---

## 1. 功能范围

### 做
- 定期抓取配置的公众号 RSS Feed
- 用 AI 判断文章归属分类（AIGC视觉生成/多模态大模型/自动驾驶/其他AI/深度学习/其它）
- 生成摘要 + 关键要点
- 输出格式化的 Markdown 文件
- 按主题自动分类（AIGC视觉生成 / 多模态大模型 / 自动驾驶 / 其他AI/深度学习）
- "其它"分类文章跳过（不输出）

### 不做
- 微信公众号账号登录和自动化操作
- 公众号发现和推荐
- 前端界面（纯命令行工具）
- 多用户支持

---

## 2. 数据流

```
RSS Feed (公众号列表)
       │
       ▼
┌──────────────┐
│  RSS 抓取器  │  (feedparser)
│  获取最新文章 │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  内容过滤器  │  (Claude API)
│  五分类判断  │  → 其它 → 跳过
└──────┬───────┘
       │  AIGC视觉生成 / 多模态大模型 / 自动驾驶 / 其他AI/深度学习
       ▼
┌──────────────┐
│  摘要生成器  │  (Claude API)
│  生成摘要+要点│
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Markdown   │
│  文件输出    │
└──────────────┘
```

---

## 3. 配置项

### 配置文件: `config.yaml`

```yaml
rss_sources:
  - name: "机器之心"
    url: "https://rsshub.app/wechat/mp/name/jiqizhixin"
    category: "多模态大模型"  # 默认分类，可被 AI 修正
  - name: "自动驾驶之心"
    url: "https://rsshub.app/wechat/mp/name/xxx"
    category: "自动驾驶"
  # 可按需添加更多公众号

# 内容分类（由 AI 自动判断）
categories:
  - "AIGC视觉生成"
  - "多模态大模型/大语言模型"
  - "自动驾驶"
  - "其他AI/深度学习领域相关"
  - "其它"  # 不输出的分类

claude:
  api_key: "sk-958751f8ea15e4f9d9f7581d78d73e3a"  # 从环境变量读取
  base_url: "https://v2.aicodee.com"  # 第三方中转地址，留空则使用官方 API
  model: "MiniMax-M2.7-highspeed"

output:
  base_dir: "./output"
  format: "按主题分类"

schedule:
  frequency: "weekly"  # 每周 2-3 次
  days: ["monday", "wednesday"]
  time: "09:00"
```

---

## 4. 输出格式

### Markdown 文件结构

**输出文件:** `output/多模态大模型/YYYY-MM-DD-multimodal-llm-digest.md`

```markdown
# 多模态大模型资讯汇总

> 生成时间: 2026-04-29 09:00

---

## [文章标题](https://example.com/article)

**来源:** 机器之心 | **发布日期:** 2026-04-28

### 摘要
文章的简要描述...

### 关键要点
- 要点 1
- 要点 2
- 要点 3

---

## [另一篇文章](...)

...
```

**注意：** "其它" 分类的文章不输出到文件，只在日志中记录。

---

## 5. 核心模块

### 5.1 RSS 抓取器 (`rss_fetcher.py`)
- 读取配置中的 RSS 源列表
- 抓取每个源的最新文章（限制最近 N 篇，避免重复）
- 返回文章列表: `{title, url, published, source}`

### 5.2 内容过滤器 (`content_filter.py`)
- 调用 Claude API 判断文章归属分类
- Prompt 设计：给出五个分类的定义，要求判断归属
- 返回: `{category: "AIGC视觉生成"|"多模态大模型"|"自动驾驶"|"其他AI/深度学习"|"其它"}`
- 只有前四类会生成摘要并输出，"其它"跳过

### 5.3 摘要生成器 (`summarizer.py`)
- 对相关文章调用 Claude API 生成摘要和要点
- 提取标题、链接、来源、摘要、要点
- 返回结构化数据

### 5.4 Markdown 输出器 (`markdown_writer.py`)
- 读取结构化数据
- 按主题渲染 Markdown
- 写入文件

### 5.5 调度器 (`scheduler.py`)
- 读取 schedule 配置
- 触发主程序执行
- Windows 环境使用 Task Scheduler 或 `schedule` 库

### 5.6 主程序 (`main.py`)
- 串联各模块
- 统一配置管理
- 错误处理和日志

---

## 6. 错误处理

| 场景 | 处理方式 |
|------|----------|
| RSS 获取失败 | 跳过该源，记录日志，继续其他源 |
| Claude API 调用失败 | 重试 2 次，失败后跳过该文章 |
| 文章内容无法访问 | 跳过，记录日志 |
| 环境变量未设置 | 启动时检查，报错退出 |

---

## 7. 项目结构

```
wechat-digest/
├── config.yaml              # 配置文件
├── main.py                  # 主入口
├── rss_fetcher.py           # RSS 抓取
├── content_filter.py        # AI 过滤 + 分类
├── summarizer.py            # 摘要生成
├── markdown_writer.py       # Markdown 输出
├── scheduler.py             # 调度器
├── prompts.py               # Claude Prompt 模板
├── output/                  # Markdown 输出目录
│   ├── AIGC视觉生成/
│   ├── 多模态大模型/
│   ├── 自动驾驶/
│   └── 其他AI_深度学习领域相关/
├── logs/                    # 日志目录
├── requirements.txt
└── README.md
```

---

## 8. 依赖

```
feedparser>=6.0.0
anthropic>=0.20.0
pyyaml>=6.0
python-dateutil>=2.8.0
```

---

## 9. 验收标准

- [ ] 可以配置多个公众号 RSS 源
- [ ] 每周 2-3 次自动执行
- [ ] 文章正确分类到五个类别（AIGC视觉生成/多模态大模型/自动驾驶/其他AI_深度学习/其它）
- [ ] 只有前四类文章生成摘要并输出，"其它"分类跳过
- [ ] Markdown 包含：标题、链接、来源、日期、摘要、要点
- [ ] 输出文件格式统一、可读性好
- [ ] Windows 本地可正常运行
- [ ] API 密钥从环境变量读取，不硬编码
- [ ] 错误不影响整体运行（部分失败不影响其他）
