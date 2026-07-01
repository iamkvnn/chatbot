# Chatbot Clone

This project scrapes 30 Zendesk Help Center articles, converts them to clean Markdown, chunks the content, and uploads only changed chunks to a Gemini File Search Store.

## Setup

```bash
git clone https://github.com/iamkvnn/chatbot.git
cd chatbot

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:

```env
GEMINI_API_KEY=your_key_here

# Optional public last-run artefact on DigitalOcean Spaces
DO_SPACES_KEY=your_spaces_access_key
DO_SPACES_SECRET=your_spaces_secret_key
DO_SPACES_BUCKET=your_bucket_name
DO_SPACES_REGION=sgp1
DO_SPACES_PREFIX=chatbot
DO_SPACES_PUBLIC_BASE_URL=https://your_bucket_name.sgp1.digitaloceanspaces.com
```

If the DigitalOcean Spaces variables are set, each `python main.py` run uploads `data/last_run.json` to:

```text
https://<bucket>.<region>.digitaloceanspaces.com/<prefix>/last_run.json
```

## Run Locally

Run the full scraper and uploader:

```bash
python main.py
```

Run once with Docker:

```bash
docker build -t chatbot .
docker run --rm -e GEMINI_API_KEY="your_key_here" chatbot
```

The Docker container runs `python main.py` once and exits with code `0` when successful.

Run a quick assistant test:

```bash
python test_assistant.py "How do I add a YouTube video?"
```

## Chunking Strategy

- Articles are fetched from the Zendesk Help Center API with `per_page=30`.
- HTML is cleaned and converted to Markdown.
- Internal support links are preserved as relative links.
- Each chunk prepends the article title, `Article URL`, source file, and chunk number so retrieved context can still cite the source.
- Chunks are split on Markdown blocks, with fenced code blocks preserved and oversized prose blocks split by sentence.
- Local chunk target: `430` content tokens.
- Local overlap: `40` tokens.
- Gemini upload chunk limit: `512` tokens.
- Gemini upload overlap: `50` tokens.

Local chunking is kept intentionally instead of uploading whole articles only:

- It lets the job upload, skip, delete, or replace only changed chunks instead of re-uploading whole articles.
- It repeats `Article URL` in every uploaded chunk, which makes source citation more reliable.
- The `430` token local target leaves room for the chunk header and stays under Gemini's `512` token upload chunk size in normal cases. Gemini's `512`/`50` `chunking_config` remains as a safety guard if an uploaded chunk is still too large.

Delta upload is stateless. The job compares local `chunk_hash` values with chunk metadata already stored in Gemini:

- Same hash: skip.
- New chunk: upload.
- Changed chunk: delete old chunk document, then upload the new one.
- Removed chunk: delete the old Gemini document.

## Last Run Log

```text
https://chatbottest.sgp1.digitaloceanspaces.com/chatbot/last_run.json
```

## Assistant Screenshots

Sample question:

```text
How do I add a YouTube video?
```

![Assistant sample answer](screenshots/test_assistant.png)

Some more test questions:
```text
How to re-encode video files?
```
![Assistant re-encode video answer](screenshots/test_assistant-How%20to%20re-encode%20video%20files.png)
```text
How Can I Remove, Delete Uploaded Files or Assets?
```
![Assistant remove uploaded files answer](<screenshots/test_assistant - How Can I Remove, Delete Uploaded Files or Assets.png>)
