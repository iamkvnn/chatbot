from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import tiktoken

from settings import ROOT

try:
    TOKEN_ENCODER = tiktoken.get_encoding("o200k_base")
except Exception:
    TOKEN_ENCODER = None


def now_iso() -> str:
    """Return a UTC timestamp suitable for run artefacts."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def token_count(text: str) -> int:
    """Estimate token count with tiktoken, falling back to word count."""
    if TOKEN_ENCODER:
        return len(TOKEN_ENCODER.encode(text))
    return len(text.split())


def sha256_text(text: str) -> str:
    """Create a stable content hash for delta detection."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_json(path: Path, default: dict[str, Any] | None = None) -> dict[str, Any]:
    """Read a JSON object, returning an empty/default object when missing."""
    if not path.exists():
        return default or {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    """Write a JSON artefact with pretty formatting."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def relative_path(path: Path) -> str:
    """Store workspace-relative paths in manifests for portability."""
    return path.relative_to(ROOT).as_posix()


def write_if_changed(path: Path, content: str) -> bool:
    """Write text only when content changed and return whether it changed."""
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True
