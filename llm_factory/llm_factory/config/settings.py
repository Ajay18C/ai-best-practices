from functools import lru_cache

from pydantic.v1 import BaseSettings

from llm_factory.config.anthropic_settings import AnthropicSettings
from llm_factory.config.openai_settings import OpenAISettings


class Settings(BaseSettings):
    app_name: str = "LLM Factory Template"
    openai: OpenAISettings = OpenAISettings()
    anthropic: AnthropicSettings = AnthropicSettings()


@lru_cache(maxsize=128)
def get_settings() -> Settings:
    return Settings()
