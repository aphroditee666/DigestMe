import time
from dataclasses import dataclass
from typing import Optional
import anthropic

@dataclass
class ClaudeConfig:
    api_key: str
    base_url: str
    model: str
    thinking: str = "disabled"

@dataclass
class TokenStats:
    input_tokens: int = 0
    output_tokens: int = 0
    call_count: int = 0
    total_time_ms: float = 0

class ClaudeClient:
    def __init__(self, config: ClaudeConfig):
        self.config = config
        self._client = None
        self.stats = TokenStats()

    def _get_client(self):
        if self._client is None:
            if self.config.base_url:
                self._client = anthropic.Anthropic(
                    api_key=self.config.api_key,
                    base_url=self.config.base_url
                )
            else:
                self._client = anthropic.Anthropic(
                    api_key=self.config.api_key
                )
        return self._client

    def send_message(self, message: str, system: Optional[str] = None, max_tokens: int = 1024) -> str:
        client = self._get_client()

        params = {
            "model": self.config.model,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": message}]
        }

        if system:
            params["system"] = system

        if self.config.thinking == "disabled":
            params["thinking"] = {"type": "disabled"}

        t0 = time.perf_counter()
        response = client.messages.create(**params)
        elapsed_ms = (time.perf_counter() - t0) * 1000

        usage = response.usage
        self.stats.input_tokens += usage.input_tokens
        self.stats.output_tokens += usage.output_tokens
        self.stats.call_count += 1
        self.stats.total_time_ms += elapsed_ms

        for block in response.content:
            if hasattr(block, 'text'):
                return block.text
        # Fallback: DeepSeek sometimes returns only ThinkingBlock w/o TextBlock
        for block in response.content:
            if hasattr(block, 'thinking'):
                return block.thinking
        raise ValueError(f"No text or thinking block found in response")
