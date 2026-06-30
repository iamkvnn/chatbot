from __future__ import annotations

import os
from pathlib import Path

import boto3
from dotenv import load_dotenv


def upload_last_run_artifact(path: Path) -> str | None:
    """Upload last_run.json to DigitalOcean Spaces and return its public URL."""
    load_dotenv()
    config = spaces_config()
    if not config:
        return None

    key = object_key(path.name, config["prefix"])
    client = boto3.client(
        "s3",
        endpoint_url=config["endpoint"],
        region_name=config["region"],
        aws_access_key_id=config["access_key"],
        aws_secret_access_key=config["secret_key"],
    )
    client.upload_file(
        str(path),
        config["bucket"],
        key,
        ExtraArgs={
            "ACL": "public-read",
            "CacheControl": "no-cache",
            "ContentType": "application/json",
        },
    )
    return public_url(config, key)


def last_run_artifact_url(path: Path) -> str | None:
    """Return the public Spaces URL that will be used for last_run.json."""
    load_dotenv()
    config = spaces_config()
    if not config:
        return None
    return public_url(config, object_key(path.name, config["prefix"]))


def spaces_config() -> dict[str, str] | None:
    """Read optional DigitalOcean Spaces settings from environment variables."""
    access_key = os.environ.get("DO_SPACES_KEY")
    secret_key = os.environ.get("DO_SPACES_SECRET")
    bucket = os.environ.get("DO_SPACES_BUCKET")
    region = os.environ.get("DO_SPACES_REGION")
    if not all((access_key, secret_key, bucket, region)):
        return None

    return {
        "access_key": str(access_key),
        "secret_key": str(secret_key),
        "bucket": str(bucket),
        "region": str(region),
        "prefix": os.environ.get("DO_SPACES_PREFIX", "chatbot").strip("/"),
        "endpoint": os.environ.get("DO_SPACES_ENDPOINT", f"https://{region}.digitaloceanspaces.com"),
        "public_base_url": os.environ.get(
            "DO_SPACES_PUBLIC_BASE_URL",
            f"https://{bucket}.{region}.digitaloceanspaces.com",
        ).rstrip("/"),
    }


def object_key(filename: str, prefix: str) -> str:
    """Build the object key used for the public run artefact."""
    return f"{prefix}/{filename}" if prefix else filename


def public_url(config: dict[str, str], key: str) -> str:
    """Build the public URL for an uploaded Spaces object."""
    return f"{config['public_base_url']}/{key}"
