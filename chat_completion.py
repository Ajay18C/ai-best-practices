from llm_factory.llm_factory.model.completion_model import CompletionModel
from llm_factory.llm_factory.model.llm_client import LLMClient
from llm_factory.llm_factory.llm_factory import LLMFactory


def do_completion():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "If it takes 2 hours to dry 1 shirt out in the sun, how long it will take for 5 shirts ?"
        },
    ]

    llm = LLMFactory(LLMClient.OPENAI)
    completion = llm.create_completion(messages=messages, response_model=CompletionModel)
    assert isinstance(completion, CompletionModel)
    print(f"Response: {completion.response}")
    print(f"Reasoning: {completion.reasoning}")


if __name__ == "__main__":
    do_completion()
