from __future__ import annotations

from typing import Any

from gemini_uploader import upload_manifest_delta
from scraper import scrape_articles
from settings import LAST_RUN_PATH
from storage import now_iso, write_json


def run_pipeline() -> dict[str, Any]:
    """Run scrape then upload, write last_run.json, and return the summary."""
    scrape_log = scrape_articles()
    upload_log = upload_manifest_delta()
    run_log = {
        "generated_at": now_iso(),
        "scrape": {
            "files_scraped": scrape_log.get("files_scraped", 0),
            "chunks_created": scrape_log.get("chunks_created", 0),
            "counts": scrape_log.get("counts", {}),
        },
        "upload": upload_log,
    }
    write_json(LAST_RUN_PATH, run_log)
    return run_log
