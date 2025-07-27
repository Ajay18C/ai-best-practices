from typing import Literal
from pydantic import BaseModel, Field
from llm_factory.llm_factory.model.llm_client import LLMClient
from llm_factory.llm_factory.llm_factory import LLMFactory


def do_completion():
    class CompletionModel(BaseModel):
        request_type: Literal["question", "command", "greet", "abuse"] = Field(
            description="The type of the request from the user")
        response: str = Field(description="The response to the user")
        response_type: Literal["question", "greet", "answer"] = Field(
            description="The type of the response to the user")

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "wtf",
        },
    ]

    llm = LLMFactory(LLMClient.OPENAI)
    completion = llm.create_completion(messages=messages, response_model=CompletionModel)
    assert isinstance(completion, CompletionModel)
    print(f"Response: {completion.response}")
    print(f"Request Type: {completion.request_type}")
    print(f"Response Type: {completion.response_type}")


if __name__ == "__main__":
    do_completion()
