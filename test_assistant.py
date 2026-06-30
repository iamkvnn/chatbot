from __future__ import annotations

import sys

from gemini_uploader import require_client, resolve_store
from settings import ASSISTANT_PROMPT, GEMINI_MODEL, GEMINI_TOP_K

DEFAULT_QUESTION = "How do I add a YouTube video?"


def ask_assistant(question: str) -> str:
    client = require_client()
    store_name = resolve_store(client, create_if_missing=False)
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=question,
        config={
            "system_instruction": ASSISTANT_PROMPT,
            "temperature": 0.2,
            "max_output_tokens": 700,
            "tools": [{"file_search": {"file_search_store_names": [store_name], "top_k": GEMINI_TOP_K}}],
        },
    )
    return response.text or ""


def main() -> None:
    question = " ".join(sys.argv[1:]).strip() or DEFAULT_QUESTION
    print(ask_assistant(question))


if __name__ == "__main__":
    main()
