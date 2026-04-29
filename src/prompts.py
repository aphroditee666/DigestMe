# src/prompts.py

CATEGORIES = {
    "AIGC视觉生成": "图像生成/编辑、视频生成与编辑、3D生成与重建、SFT/强化学习/LORA等训练策略相关",
    "多模态大模型/大语言模型": "多模态大模型、大语言模型相关",
    "自动驾驶": "VLA/端到端/世界模型等自动驾驶相关",
    "其他AI/深度学习领域相关": "不属于前三类的AI/深度学习相关（如强化学习研究方向、NLP其他方向、AI安全等）",
    "其它": "不属于以上四类的内容"
}

CLASSIFICATION_PROMPT = """你是一个文章分类助手。请根据以下分类定义，判断文章属于哪个类别。

分类定义：
{category_definitions}

文章信息：
标题：{title}
来源：{source}

请只输出一个分类名称，不要输出其他内容。
输出选项：{category_list}
"""

SUMMARIZATION_PROMPT = """你是一个文章摘要助手。请为以下文章生成摘要和关键要点。

文章信息：
标题：{title}
来源：{source}
链接：{url}

请按以下格式输出：

### 摘要
{summary_text}

### 关键要点
- {key_point_1}
- {key_point_2}
- {key_point_3}

要求：
1. 摘要长度 50-150 字
2. 提供 3 个关键要点
3. 要点简洁，每条不超过 30 字
4. 用中文输出
"""

def get_classification_prompt(title: str, source: str, categories: list) -> str:
    category_definitions = "\n".join([
        f"- {name}: {desc}" for name, desc in CATEGORIES.items() if name != "其它"
    ])
    category_list = ", ".join([f'"{name}"' for name in categories])

    return CLASSIFICATION_PROMPT.format(
        category_definitions=category_definitions,
        title=title,
        source=source,
        category_list=category_list
    )

def get_summarization_prompt(title: str, source: str, url: str) -> str:
    return SUMMARIZATION_PROMPT.format(
        title=title,
        source=source,
        url=url,
        summary_text="[摘要内容]",
        key_point_1="[要点1]",
        key_point_2="[要点2]",
        key_point_3="[要点3]"
    )