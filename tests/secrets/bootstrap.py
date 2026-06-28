"""Seed the LocalStack Secrets Manager from ``seed_data.json``.

The LocalStack init hook (``tests/secrets/init/01-seed-secrets.sh``) seeds these
automatically on ``docker compose up``. Run this module manually only to re-seed
a already-running container without restarting it:

    python -m tests.secrets.bootstrap
"""

import json
import os
from pathlib import Path

import boto3

SEED_DATA_FILE = Path(__file__).parent / "seed_data.json"


def _put_secret(client, name: str, secret_string: str) -> None:
    """Create a secret, or overwrite it if it already exists."""
    try:
        client.create_secret(Name=name, SecretString=secret_string)
        print(f"created secret {name}")
    except client.exceptions.ResourceExistsException:
        client.put_secret_value(SecretId=name, SecretString=secret_string)
        print(f"updated secret {name}")


def main() -> None:
    """Seed every secret defined in ``seed_data.json`` into Secrets Manager."""
    client = boto3.client(
        "secretsmanager",
        endpoint_url=os.getenv("AWS_ENDPOINT_URL", "http://localhost:4566"),
        region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", "test"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", "test"),
    )
    secrets = json.loads(SEED_DATA_FILE.read_text(encoding="utf-8"))
    for name, payload in secrets.items():
        _put_secret(client, name, json.dumps(payload))


if __name__ == "__main__":
    main()
