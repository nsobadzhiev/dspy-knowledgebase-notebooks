from typing import Any


def summarize_usage(history_item: dict[str, Any]):
    response = history_item['response']
    usage = response['usage']
    response_id = response['id']
    print(f"LLM usage for {response_id}: {usage['prompt_tokens']} prompt, {usage['completion_tokens']} completion, {usage['total_tokens']} total")


def summarize_usages(items: list[dict[str, Any]]):
    for item in items:
        summarize_usage(item)
