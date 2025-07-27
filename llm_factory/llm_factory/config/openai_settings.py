from .llm_provider_settings import LLMProviderSettings
import os
from dotenv import load_dotenv

load_dotenv()


class OpenAISettings(LLMProviderSettings):
    api_key: str = os.getenv("OPENAI_API_KEY")
    default_model: str = os.getenv("OPENAI_DEFAULT_MODEL")
