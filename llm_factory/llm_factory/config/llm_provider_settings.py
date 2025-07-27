from typing import Optional

from pydantic.v1 import BaseSettings


class LLMProviderSettings(BaseSettings):
    temperature: float = 0.0
    max_tokens: Optional[int] = None
    max_retries: int = 3
    base_url: Optional[str] = None
