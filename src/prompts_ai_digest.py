# src/prompts_ai_digest.py
import re

SUBTYPE_TECH = "技术/算法"
SUBTYPE_PRODUCT = "产品/应用"

CATEGORIES = {
    "AIGC视觉生成": "图像生成、图像编辑、视频生成、视频编辑、扩散模型相关的SFT/强化学习/LoRA/持续学习等训练策略、3D生成与重建",
    "多模态大模型/大语言模型": "多模态大模型、大语言模型相关",
    "自动驾驶": "VLA/端到端/世界模型/驾驶仿真等自动驾驶相关",
    "Coding Agent": "编码Agent相关各类信息(如Claude Code、Codex、Cursor等), 以及Agent Skill、编码Agent在各类应用中的落地（如PPT生成、AI研究、自动化工作流等等）",
    "学术论文": "来自arXiv、学术会议（NeurIPS/ICML/ICLR/CVPR/ICCV/ECCV/AAAI/IJCAI/ICRA/CoRL/RSS）、学术期刊（TPAMI/IJCV/JMLR/TNNLS/NMI）的AI/ML/CV/RO领域论文",
    "其它": "不属于以上类别的内容"
}

CATEGORIES_TO_OUTPUT = [
    "AIGC视觉生成",
    "多模态大模型/大语言模型",
    "自动驾驶",
    "Coding Agent",
    "学术论文"
]


def build_classification_system_prompt() -> str:
    """System prompt for classification — cached by API, not repeated per article."""
    defs = "\n".join(f"- {name}: {desc}" for name, desc in CATEGORIES.items())
    return f"""你是一个文章分类助手。根据以下分类定义判断文章属于哪个类别和子类型（subtype）。

分类定义：
{defs}

子类型（subtype）定义：
- 技术/算法：内容侧重技术原理、算法设计、模型架构、训练方法、数学推导、系统设计等技术深度内容
- 产品/应用：内容侧重产品发布、应用案例、行业动态、工具使用、商业合作、教程科普等应用层面内容

重要规则：
1. 对于学术论文（来源为arXiv等学术渠道或会议/期刊名称），统一归入「学术论文」类别，不再按内容细分到AIGC视觉生成等类别
2. 批量分类时输出JSON数组，每项包含 "index"、"category"、"subtype" 三个字段
3. 单篇分类时输出JSON对象，包含 "category" 和 "subtype" 两个字段"""


def build_summarization_system_prompt() -> str:
    """System prompt for summarization — cached by API, not repeated per article."""
    return """你是一个专业的技术文章摘要助手。请按以下格式输出：

### 摘要
[150-400字的摘要，涵盖背景/问题、核心方法/技术方案、关键结果/结论]

### 关键要点
- [要点1：15-50字，必须有实质信息]
- [要点2]
- [要点3]
- [要点4（可选）]
- [要点5（可选）]

### arXiv
[arXiv完整链接或"无"]

### GitHub
[GitHub完整链接或"无"]

要求：
1. 摘要150-400字，必须涵盖：背景/问题、核心方法/技术方案、关键结果/结论
2. 提供2-5个关键要点，每条15-50字，必须有实质信息（数字、方法名、技术名称等），切忌空洞概括
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


# ---- Batch summarization ----
BATCH_SUMMARIZATION_SYSTEM = """你是一个专业的技术文章摘要助手。下面有多篇文章，请为每篇生成摘要。
严格输出 JSON 数组，每个元素包含以下字段：

{
  "index": 序号(整数),
  "summary": "150-400字的摘要，涵盖背景/问题、核心方法/技术方案、关键结果/结论",
  "key_points": ["要点1", "要点2", ...],  // 2-5个，每条15-50字，必须有实质信息
  "arxiv_url": "arXiv完整链接或空字符串",
  "github_url": "GitHub完整链接或空字符串"
}

要求：
1. 摘要150-400字，必须涵盖：背景/问题、核心方法/技术方案、关键结果/结论
2. 提供2-5个关键要点，每条15-50字，必须有实质信息（数字、方法名、技术名称等），切忌空洞概括
3. 如果文章提到具体模型名、数据集、性能指标、开源地址，务必写入摘要或要点
4. 用中文输出
5. 正文可能被截断（最长约2000字符），请基于标题和正文开头提炼关键信息
6. 涉及论文在 arxiv_url 提供 arXiv 完整链接（如 https://arxiv.org/abs/xxxx.xxxxx），否则空字符串
7. 涉及 GitHub 开源仓库在 github_url 提供 GitHub 完整链接（如 https://github.com/user/repo），否则空字符串
8. 只输出 JSON 数组，不要输出其他内容"""


def get_batch_summarization_prompt(articles: list) -> str:
    """articles: [{"index": int, "title": str, "source": str, "url": str, "content": str}]"""
    blocks = []
    for a in articles:
        cleaned = clean_content(a.get("content", ""))
        if cleaned:
            content_section = f"正文：\n{cleaned}\n"
        else:
            content_section = ""
        blocks.append(
            f'{a["index"]}. 标题：{a["title"]}\n'
            f'   来源：{a["source"]}\n'
            f'   链接：{a["url"]}\n'
            f'   {content_section}'
        )
    return "\n---\n".join(blocks)


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
- {trend_4}（可选）
- {trend_5}（可选）

要求：
1. 总结 200-400 字，必须提炼共性，不要逐篇罗列
2. 提供2-5个关键趋势
3. 如果多篇文章指向同一趋势，合并表述
4. 每个趋势表述要具体，包含实质信息（模型名、方法名、指标等），切忌空泛概括
5. 用中文输出
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
