from __future__ import annotations

import json
import logging

from pipeline import run_pipeline


def configure_logging() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    for noisy_logger in ("httpx", "httpcore", "google", "google_genai"):
        logging.getLogger(noisy_logger).setLevel(logging.WARNING)


def main() -> None:
    """CLI entrypoint for the one-shot scrape and upload job."""
    configure_logging()
    result = run_pipeline()
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
