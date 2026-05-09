# src/prompts_ai_digest.py
import re

CATEGORIES = {
    "AIGC视觉生成": "图像生成/编辑、视频生成与编辑、3D生成与重建、扩散模型相关的SFT/强化学习/LoRA/持续学习等训练策略",
    "多模态大模型/大语言模型": "多模态大模型、大语言模型相关",
    "自动驾驶": "VLA/端到端/世界模型/驾驶仿真等自动驾驶相关",
    "小样本学习/强化学习": "小样本学习、强化学习相关",
    "其它": "不属于以上四类的内容"
}

CATEGORIES_TO_OUTPUT = [
    "AIGC视觉生成",
    "多模态大模型/大语言模型",
    "自动驾驶",
    "小样本学习/强化学习"
]


def build_classification_system_prompt() -> str:
    """System prompt for classification — cached by API, not repeated per article."""
    defs = "\n".join(f"- {name}: {desc}" for name, desc in CATEGORIES.items())
    return f"""你是一个文章分类助手。根据以下分类定义判断文章属于哪个类别，只输出分类名称，不要输出其他内容。

分类定义：
{defs}

重要规则：对于学术论文（来源为"arXiv AI"等学术渠道），仅当论文主题与「AIGC视觉生成」或「自动驾驶」相关时，才归入对应类别；其余学术论文一律归入「其它」。"""


def build_summarization_system_prompt() -> str:
    """System prompt for summarization — cached by API, not repeated per article."""
    return """你是一个专业的技术文章摘要助手。请按以下格式输出：

### 摘要
[200-400字的摘要，涵盖背景/问题、核心方法/技术方案、关键结果/结论]

### 关键要点
- [要点1：15-50字，必须有实质信息]
- [要点2]
- [要点3]
- [要点4]
- [要点5]

### arXiv
[arXiv完整链接或"无"]

### GitHub
[GitHub完整链接或"无"]

要求：
1. 摘要200-400字，必须涵盖：背景/问题、核心方法/技术方案、关键结果/结论
2. 提供5个关键要点，每条15-50字，必须有实质信息（数字、方法名、技术名称等），切忌空洞概括
3. 如果文章提到具体模型名、数据集、性能指标、开源地址，务必写入摘要或要点
4. 用中文输出
5. 正文可能被截断（最长约2000字符），请基于标题和正文开头提炼关键信息
6. 涉及论文务必在「### arXiv」后提供arXiv完整链接（如https://arxiv.org/abs/xxxx.xxxxx）；不涉及则输出「无」
7. 涉及GitHub开源仓库务必在「### GitHub」后提供GitHub完整链接（如https://github.com/user/repo）；不涉及则输出「无」"""


# Lightweight classification — no article body, no format instructions (moved to system)
CLASSIFICATION_PROMPT = """标题：{title}
来源：{source}
"""

# Summarization prompt — only article-specific info, format instructions in system
SUMMARIZATION_PROMPT = """标题：{title}
来源：{source}
链接：{url}
{content_section}"""


def get_classification_prompt(title: str, source: str) -> str:
    return CLASSIFICATION_PROMPT.format(title=title, source=source)


def clean_content(html_text: str, max_len: int = 2000) -> str:
    """去除HTML标签、解码实体、合并空白、按句末标点截断。"""
    if not html_text or not html_text.strip():
        return ""

    # 移除 script/style 块（连同内容）
    text = re.sub(
        r'<(script|style|noscript)\b[^>]*>.*?</\1>',
        '', html_text, flags=re.DOTALL | re.IGNORECASE
    )
    # 剥离其余 HTML 标签（替换为空格，避免词语黏连）
    text = re.sub(r'<[^>]+>', ' ', text)
    # 解码常见 HTML 实体
    text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    text = text.replace('&quot;', '"').replace('&#39;', "'").replace('&nbsp;', ' ')
    # 合并空白字符
    text = re.sub(r'\s+', ' ', text).strip()

    if len(text) > max_len:
        truncated = text[:max_len]
        # 在 max_len 范围内找最后一个句末标点
        boundary = max(truncated.rfind('。'), truncated.rfind('！'), truncated.rfind('？'))
        if boundary > max_len * 0.5:
            text = truncated[:boundary + 1] + '...'
        else:
            text = truncated + '...'
    return text


def get_summarization_prompt(title: str, source: str, url: str, content: str = "") -> str:
    cleaned = clean_content(content)
    if cleaned:
        content_section = f"正文：\n{cleaned}\n"
    else:
        content_section = ""
    return SUMMARIZATION_PROMPT.format(
        title=title, source=source, url=url, content_section=content_section
    )


TREND_SUMMARY_PROMPT = """你是一个专业的技术趋势分析助手。请根据本周收集的以下文章，生成一份「进展与趋势总结」。

类别：{category_name}
本周文章数量：{article_count}

本周文章列表（包含标题和关键要点）：

{article_list}

请按以下格式输出：

### 进展与趋势总结
{summary_hint}

### 关键趋势
- {trend_1}
- {trend_2}
- {trend_3}
- {trend_4}
- {trend_5}

要求：
1. 总结 200-400 字，必须提炼共性，不要逐篇罗列
2. 如果多篇文章指向同一趋势，合并表述
3. 每个趋势表述要具体，包含实质信息（模型名、方法名、指标等），切忌空泛概括
4. 用中文输出
"""


def get_trend_summary_prompt(category_name: str, articles: list) -> str:
    article_items = []
    for i, a in enumerate(articles, 1):
        points = "\n".join(f"  - {p}" for p in a.key_points)
        article_items.append(f"{i}. {a.title}\n{points}")
    article_list = "\n\n".join(article_items)

    return TREND_SUMMARY_PROMPT.format(
        category_name=category_name,
        article_count=len(articles),
        article_list=article_list,
        summary_hint="[一段200-400字的综合性趋势总结]",
        trend_1="[趋势1：具体的技术或产业趋势]",
        trend_2="[趋势2]",
        trend_3="[趋势3]",
        trend_4="[趋势4]",
        trend_5="[趋势5]",
    )
