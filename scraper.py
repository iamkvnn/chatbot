from __future__ import annotations

import re
from typing import Any
from urllib.parse import unquote, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as to_markdown
from requests.adapters import HTTPAdapter
from slugify import slugify
from urllib3.util.retry import Retry

from settings import (
    ARTICLE_CHUNK_OVERLAP,
    ARTICLE_CHUNK_TOKENS,
    ARTICLE_LIMIT,
    ARTICLES_DIR,
    CHUNKS_DIR,
    HELP_CENTER_API_URL,
    HELP_CENTER_DOMAIN,
    MANIFEST_PATH,
    REQUEST_TIMEOUT_SECONDS
)
from storage import now_iso, relative_path, sha256_text, token_count, write_if_changed, write_json


def scrape_articles() -> dict[str, Any]:
    """Scrape articles, write Markdown/chunk files, and return the manifest payload."""
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    clear_generated_markdown()

    articles = fetch_articles()
    article_records: list[dict[str, Any]] = []
    chunk_records: list[dict[str, Any]] = []

    for article in articles:
        article_id = str(article["id"])
        article_path = ARTICLES_DIR / article_filename(article)
        content = build_article_markdown(article)
        content_hash = sha256_text(content)

        write_if_changed(article_path, content)
        chunks = chunk_article_file(article_path)

        record = {
            "id": article_id,
            "title": str(article.get("title") or "").strip(),
            "url": article.get("html_url"),
            "updated_at": article.get("updated_at"),
            "file": relative_path(article_path),
            "tokens": token_count(content),
            "hash": content_hash,
            "status": "scraped",
            "chunks_count": len(chunks),
            "chunks": chunks,
        }
        article_records.append(record)
        chunk_records.extend(chunks)

    manifest = {
        "generated_at": now_iso(),
        "source": HELP_CENTER_API_URL,
        "files_scraped": len(article_records),
        "chunks_created": len(chunk_records),
        "counts": {"scraped": len(article_records)},
        "chunking": {
            "strategy": "Markdown block chunks with code-block preservation and overlap.",
            "max_tokens_per_chunk": ARTICLE_CHUNK_TOKENS,
            "overlap_tokens": ARTICLE_CHUNK_OVERLAP,
        },
        "articles": article_records,
        "chunks": chunk_records,
    }

    write_json(MANIFEST_PATH, manifest)
    return manifest


def clear_generated_markdown() -> None:
    """Remove generated Markdown files so each run reflects only the latest scrape."""
    for directory in (ARTICLES_DIR, CHUNKS_DIR):
        for path in directory.glob("*.md"):
            path.unlink(missing_ok=True)


def build_session() -> requests.Session:
    """Create a retrying HTTP session for Zendesk API requests."""
    session = requests.Session()
    retries = Retry(
        total=3,
        connect=3,
        read=3,
        backoff_factor=1,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)
    return session


def fetch_articles() -> list[dict[str, Any]]:
    """Fetch the newest published articles from the Help Center API."""
    session = build_session()
    params = {
        "per_page": ARTICLE_LIMIT,
        "sort_by": "updated_at",
        "sort_order": "desc",
    }

    response = session.get(HELP_CENTER_API_URL, params=params, timeout=REQUEST_TIMEOUT_SECONDS)
    response.raise_for_status()
    payload = response.json()
    return [article for article in payload.get("articles", []) if not article.get("draft")]


def normalize_internal_links(soup: BeautifulSoup) -> None:
    """Convert same-domain article and asset URLs to relative links."""
    for tag in soup.find_all(["a", "img"]):
        attr = "href" if tag.name == "a" else "src"
        value = tag.get(attr)
        if not value:
            continue

        parsed = urlparse(value)
        if parsed.netloc == HELP_CENTER_DOMAIN:
            tag[attr] = urlunparse(("", "", parsed.path, "", parsed.query, parsed.fragment))


def clean_html_to_markdown(html: str) -> str:
    """Strip noisy HTML and convert the article body to clean Markdown."""
    soup = BeautifulSoup(html or "", "html.parser")
    for bad in soup.select("script, style, noscript, form, button, iframe"):
        bad.decompose()

    normalize_internal_links(soup)
    markdown = to_markdown(str(soup), heading_style="ATX", bullets="-", strip=["span"])
    markdown = re.sub(r"\r\n?", "\n", markdown)
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip()


def article_filename(article: dict[str, Any]) -> str:
    """Build a stable Markdown filename from the Zendesk article URL."""
    article_url = str(article.get("html_url") or "")
    url_slug = unquote(urlparse(article_url).path.strip("/").split("/")[-1])
    safe_url_slug = re.sub(r"[^A-Za-z0-9._-]+", "-", url_slug).strip(".-_")
    if safe_url_slug:
        return f"{safe_url_slug[:140]}.md"

    title = str(article.get("title") or "").strip()
    article_id = str(article["id"])
    slug = slugify(title)[:90] or article_id
    return f"{slug}-{article_id}.md"


def build_article_markdown(article: dict[str, Any]) -> str:
    """Create the full Markdown document for one Zendesk article."""
    title = str(article.get("title") or f"Article {article['id']}").strip()
    body_markdown = clean_html_to_markdown(str(article.get("body") or ""))
    return "\n".join(
        [
            f"# {title}",
            "",
            f"Article URL: {article.get('html_url') or ''}",
            f"Article ID: {article.get('id')}",
            "",
            body_markdown,
            "",
        ]
    )


def split_blocks_preserve_code(text: str) -> list[str]:
    """Split Markdown into blocks without breaking fenced code blocks."""
    blocks: list[str] = []
    current: list[str] = []
    in_code = False

    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            current.append(line)
            continue

        if not in_code and not line.strip():
            if current:
                blocks.append("\n".join(current).strip())
                current = []
            continue

        current.append(line)

    if current:
        blocks.append("\n".join(current).strip())

    return [block for block in blocks if block]


def split_large_block(block: str) -> list[str]:
    """Split oversized prose blocks while keeping code blocks intact."""
    if token_count(block) <= ARTICLE_CHUNK_TOKENS or block.lstrip().startswith("```"):
        return [block]

    parts: list[str] = []
    current: list[str] = []
    for sentence in re.split(r"(?<=[.!?])\s+", block):
        candidate = " ".join(current + [sentence]).strip()
        if current and token_count(candidate) > ARTICLE_CHUNK_TOKENS:
            parts.append(" ".join(current).strip())
            current = [sentence]
        else:
            current.append(sentence)

    if current:
        parts.append(" ".join(current).strip())
    return [part for part in parts if part]


def chunk_text(text: str) -> list[list[str]]:
    """Group Markdown blocks into overlapping chunks for retrieval."""
    blocks: list[str] = []
    for block in split_blocks_preserve_code(text):
        blocks.extend(split_large_block(block))

    chunks: list[list[str]] = []
    current: list[str] = []
    current_tokens = 0

    for block in blocks:
        block_tokens = token_count(block)
        if current and current_tokens + block_tokens > ARTICLE_CHUNK_TOKENS:
            chunks.append(current)
            overlap: list[str] = []
            overlap_count = 0
            for previous in reversed(current):
                previous_tokens = token_count(previous)
                if overlap_count + previous_tokens > ARTICLE_CHUNK_OVERLAP:
                    break
                overlap.insert(0, previous)
                overlap_count += previous_tokens
            current = overlap + [block]
            current_tokens = sum(token_count(item) for item in current)
        else:
            current.append(block)
            current_tokens += block_tokens

    if current:
        chunks.append(current)

    return chunks


def article_body_for_chunking(text: str) -> str:
    """Remove the article-level header before creating per-chunk files."""
    lines = text.splitlines()
    index = 0

    if index < len(lines) and lines[index].startswith("# "):
        index += 1
    if index < len(lines) and not lines[index].strip():
        index += 1

    while index < len(lines) and re.match(r"^(Article URL|Article ID|Updated At):", lines[index]):
        index += 1
    if index < len(lines) and not lines[index].strip():
        index += 1

    return "\n".join(lines[index:]).strip()


def chunk_article_file(article_path) -> list[dict[str, Any]]:
    """Write chunk Markdown files for one article and return chunk metadata."""
    text = article_path.read_text(encoding="utf-8")
    title_match = re.search(r"^# .+$", text, flags=re.MULTILINE)
    url_match = re.search(r"^Article URL: .+$", text, flags=re.MULTILINE)
    title_line = title_match.group(0) if title_match else f"# {article_path.stem}"
    url_line = url_match.group(0) if url_match else "Article URL: UNKNOWN"
    chunks = chunk_text(article_body_for_chunking(text))

    records: list[dict[str, Any]] = []
    for index, chunk_blocks in enumerate(chunks, start=1):
        chunk_path = CHUNKS_DIR / f"{article_path.stem}__chunk_{index:03d}.md"
        chunk_content = "\n".join(
            [
                title_line,
                "",
                url_line,
                f"Source File: {article_path.name}",
                f"Chunk: {index}/{len(chunks)}",
                "",
                "\n\n".join(chunk_blocks),
                "",
            ]
        )
        write_if_changed(chunk_path, chunk_content)
        records.append(
            {
                "file": relative_path(chunk_path),
                "tokens": token_count(chunk_content),
                "hash": sha256_text(chunk_content),
                "chunk_index": index,
                "chunk_count": len(chunks),
            }
        )

    return records
