import os

from .llm_provider_settings import LLMProviderSettings


class AnthropicSettings(LLMProviderSettings):
    api_key: str = os.getenv("ANTHROPIC_API_KEY")
    default_model: str = os.getenv("ANTHROPIC_DEFAULT_MODEL")
    max_tokens: int = 1024
