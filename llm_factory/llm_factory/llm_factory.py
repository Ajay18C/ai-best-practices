from typing import Any, Dict, List, Type
import instructor
from anthropic import Anthropic
from openai import OpenAI
from pydantic import BaseModel
from llm_factory.config.settings import get_settings
from llm_factory.model.llm_client import LLMClient


class LLMFactory:
    def __init__(self, provider: LLMClient):
        self._provider: LLMClient = provider
        self._settings = getattr(get_settings(), provider.value)
        self._client = self._initialize_client()

    def _initialize_client(self) -> Any:
        client_initializers = {
            LLMClient.OPENAI: lambda s: instructor.from_openai(OpenAI(base_url=s.base_url, api_key=s.api_key)),
            LLMClient.ANTHROPIC: lambda s: instructor.from_anthropic(Anthropic(base_url=s.base_url, api_key=s.api_key)),
            LLMClient.LLAMA: lambda s: instructor.from_openai(OpenAI(base_url=s.base_url, api_key=s.api_key),
                                                              mode=instructor.Mode.JSON),
        }
        initializer = client_initializers.get(self._provider)
        if initializer:
            return initializer(self._settings)
        raise ValueError(f"Unsupported LLM provider: {self._provider}")

    def create_completion(self, response_model: Type[BaseModel], messages: List[Dict[str, str]], **kwargs) -> Any:
        completion_params = {
            "model": kwargs.get("model", self._settings.default_model),
            "temperature": kwargs.get("temperature", self._settings.temperature),
            "max_retries": kwargs.get("max_retries", self._settings.max_retries),
            "max_tokens": kwargs.get("max_tokens",self._settings.max_tokens),
            "response_model": response_model,
            "messages": messages,
        }

        return self._client.chat.completions.create(**completion_params)
