from typing import List
from src.claude_client import ClaudeClient, ClaudeConfig
from src.prompts import get_classification_prompt, CATEGORIES

class ContentFilter:
    VALID_CATEGORIES = [
        "AIGC视觉生成",
        "多模态大模型/大语言模型",
        "自动驾驶",
        "其他AI/深度学习领域相关",
        "其它"
    ]

    def __init__(self, config: ClaudeConfig):
        self.client = ClaudeClient(config)

    def classify(self, title: str, source: str) -> str:
        prompt = get_classification_prompt(
            title=title,
            source=source,
            categories=self.VALID_CATEGORIES
        )

        response = self.client.send_message(prompt)
        response = response.strip()

        for category in self.VALID_CATEGORIES:
            if category in response:
                return category

        return "其它"