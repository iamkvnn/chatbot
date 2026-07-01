from __future__ import annotations

import logging
import os
import time
from typing import Any

from dotenv import load_dotenv
from google import genai

from settings import (
    GEMINI_OPERATION_POLL_SECONDS,
    GEMINI_OPERATION_TIMEOUT_SECONDS,
    GEMINI_STORE_DISPLAY_NAME,
    GEMINI_UPLOAD_CHUNK_OVERLAP,
    GEMINI_UPLOAD_CHUNK_TOKENS,
    MANIFEST_PATH,
    ROOT,
)
from storage import load_json, now_iso


def upload_manifest_delta() -> dict[str, Any]:
    """Upload only new/changed chunks from the manifest and return run counts."""
    manifest = load_json(MANIFEST_PATH)
    if not manifest:
        raise RuntimeError("No manifest found. Run the scraper first.")

    client = require_client()
    store_name = resolve_store(client, create_if_missing=True)
    remote_chunks = load_remote_chunks(client, store_name)

    counts = {
        "added": 0,
        "updated": 0,
        "skipped": 0,
        "deleted_documents": 0,
        "added_chunks": 0,
        "updated_chunks": 0,
        "skipped_chunks": 0,
        "removed_chunks": 0,
    }
    article_logs: list[dict[str, Any]] = []

    for article in manifest.get("articles", []):
        article_id = str(article["id"])
        previous_chunks = remote_chunks.get(article_id, {})
        current_chunks = article.get("chunks", [])
        current_files = {chunk.get("file") for chunk in current_chunks}

        if not previous_chunks:
            status = "added"
        elif chunk_state_changed(current_chunks, previous_chunks):
            status = "updated"
        else:
            status = "skipped"

        counts[status] += 1
        article_counts = {
            "added_chunks": 0,
            "updated_chunks": 0,
            "skipped_chunks": 0,
            "removed_chunks": 0,
            "deleted_documents": 0,
        }

        for remote_file, remote_chunk in previous_chunks.items():
            if remote_file not in current_files:
                article_counts["deleted_documents"] += delete_document(client, remote_chunk.get("document_name"))
                article_counts["removed_chunks"] += 1

        for chunk in current_chunks:
            chunk_file = chunk.get("file")
            previous_chunk = previous_chunks.get(chunk_file)
            if previous_chunk and previous_chunk.get("hash") == chunk.get("hash"):
                article_counts["skipped_chunks"] += 1
                continue

            if previous_chunk:
                article_counts["deleted_documents"] += delete_document(client, previous_chunk.get("document_name"))
                article_counts["updated_chunks"] += 1
            else:
                article_counts["added_chunks"] += 1

            chunk_path = ROOT / chunk["file"]
            if not chunk_path.exists():
                raise FileNotFoundError(f"Chunk file missing: {chunk_path}")

            logging.info("Uploading %s", chunk_path.name)
            upload_chunk_file(client, store_name, chunk_path, article, chunk)

        counts["deleted_documents"] += article_counts["deleted_documents"]
        counts["added_chunks"] += article_counts["added_chunks"]
        counts["updated_chunks"] += article_counts["updated_chunks"]
        counts["skipped_chunks"] += article_counts["skipped_chunks"]
        counts["removed_chunks"] += article_counts["removed_chunks"]

        article_logs.append(
            {
                "id": article_id,
                "title": article.get("title"),
                "status": status,
                "chunks": len(current_chunks),
                "added_chunks": article_counts["added_chunks"],
                "updated_chunks": article_counts["updated_chunks"],
                "skipped_chunks": article_counts["skipped_chunks"],
                "removed_chunks": article_counts["removed_chunks"],
            }
        )

    upload_log = {
        "generated_at": now_iso(),
        "provider": "Google Gemini",
        "file_search_store_name": store_name,
        "source_article_files": manifest.get("files_scraped", 0),
        "manual_chunks_available": manifest.get("chunks_created", 0),
        "counts": counts,
        "articles": article_logs,
    }
    return upload_log


def chunk_state_changed(current_chunks: list[dict[str, Any]], previous_chunks: dict[str, dict[str, Any]]) -> bool:
    """Return True when local chunk files or hashes differ from Gemini metadata."""
    current_files = {chunk.get("file") for chunk in current_chunks}
    if current_files != set(previous_chunks):
        return True

    for chunk in current_chunks:
        previous_chunk = previous_chunks.get(chunk.get("file"))
        if not previous_chunk or previous_chunk.get("hash") != chunk.get("hash"):
            return True

    return False


def require_client():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing. Add it to .env or the job environment.")
    return genai.Client(api_key=api_key)


def resolve_store(client: Any, create_if_missing: bool = False) -> str:
    for store in client.file_search_stores.list():
        if getattr(store, "display_name", None) == GEMINI_STORE_DISPLAY_NAME:
            return store.name

    if not create_if_missing:
        raise RuntimeError(
            f"Gemini File Search Store '{GEMINI_STORE_DISPLAY_NAME}' was not found. Run main.py first."
        )

    store = client.file_search_stores.create(config={"display_name": GEMINI_STORE_DISPLAY_NAME})
    return store.name


def metadata_value(metadata: list[Any] | None, key: str) -> str | None:
    for item in metadata or []:
        if getattr(item, "key", None) == key:
            return getattr(item, "string_value", None)
    return None


def load_remote_chunks(client: Any, store_name: str) -> dict[str, dict[str, dict[str, Any]]]:
    """Load existing Gemini documents as article_id -> chunk_file -> metadata."""
    remote_chunks: dict[str, dict[str, dict[str, Any]]] = {}
    for document in client.file_search_stores.documents.list(parent=store_name):
        metadata = getattr(document, "custom_metadata", None)
        article_id = metadata_value(metadata, "article_id")
        chunk_file = metadata_value(metadata, "chunk_file")
        if not article_id or not chunk_file:
            continue

        remote_chunks.setdefault(article_id, {})[chunk_file] = {
            "document_name": document.name,
            "hash": metadata_value(metadata, "chunk_hash"),
        }

    return remote_chunks


def delete_document(client: Any, document_name: str | None) -> int:
    if not document_name:
        return 0

    client.file_search_stores.documents.delete(name=document_name, config={"force": True})
    return 1


def upload_chunk_file(
    client: Any,
    store_name: str,
    chunk_path,
    article: dict[str, Any],
    chunk: dict[str, Any],
) -> str:
    """Upload one Markdown chunk file to Gemini File Search and return its document name."""
    operation = client.file_search_stores.upload_to_file_search_store(
        file_search_store_name=store_name,
        file=str(chunk_path),
        config={
            "display_name": chunk_path.name,
            "mime_type": "text/markdown",
            "custom_metadata": [
                {"key": "article_id", "string_value": str(article["id"])},
                {"key": "chunk_file", "string_value": str(chunk.get("file") or "")},
                {"key": "chunk_hash", "string_value": str(chunk.get("hash") or "")},
            ],
            "chunking_config": {
                "white_space_config": {
                    "max_tokens_per_chunk": GEMINI_UPLOAD_CHUNK_TOKENS,
                    "max_overlap_tokens": GEMINI_UPLOAD_CHUNK_OVERLAP,
                }
            },
        },
    )
    operation = wait_for_operation(client, operation)
    response = getattr(operation, "response", None)
    document_name = getattr(response, "document_name", None)
    if not document_name:
        raise RuntimeError(f"Upload completed but no document_name was returned for {chunk_path.name}.")
    return document_name


def wait_for_operation(client: Any, operation: Any) -> Any:
    started_at = time.monotonic()
    while not operation.done:
        if time.monotonic() - started_at > GEMINI_OPERATION_TIMEOUT_SECONDS:
            raise TimeoutError(f"Gemini operation timed out after {GEMINI_OPERATION_TIMEOUT_SECONDS}s.")
        time.sleep(GEMINI_OPERATION_POLL_SECONDS)
        operation = client.operations.get(operation)
    return operation
