from enum import Enum, auto


class LLMClient(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    LLAMA = "llama"
