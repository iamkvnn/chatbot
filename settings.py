from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
ARTICLES_DIR = DATA_DIR / "articles"
CHUNKS_DIR = DATA_DIR / "chunks"

MANIFEST_PATH = DATA_DIR / "manifest.json"
LAST_RUN_PATH = DATA_DIR / "last_run.json"

HELP_CENTER_API_URL = "https://support.optisigns.com/api/v2/help_center/articles.json"
HELP_CENTER_DOMAIN = "support.optisigns.com"

ARTICLE_LIMIT = 30
REQUEST_TIMEOUT_SECONDS = 30

ARTICLE_CHUNK_TOKENS = 430
ARTICLE_CHUNK_OVERLAP = 40

GEMINI_STORE_DISPLAY_NAME = "chatbot-support-docs"
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_TOP_K = 5
GEMINI_UPLOAD_CHUNK_TOKENS = 512
GEMINI_UPLOAD_CHUNK_OVERLAP = 50
GEMINI_OPERATION_POLL_SECONDS = 5
GEMINI_OPERATION_TIMEOUT_SECONDS = 900

ASSISTANT_PROMPT = """You are OptiBot, the customer-support bot for OptiSigns.com.
- Tone: helpful, factual, concise.
- Only answer using the uploaded docs.
- Max 5 bullet points; else link to the doc.
- Cite up to 3 "Article URL:" lines per reply."""
