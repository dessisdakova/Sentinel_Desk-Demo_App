"""Seed the LocalStack Secrets Manager with baseline test user secrets.

Run once after ``docker compose up -d`` (and again any time the LocalStack
container is recreated):

    python -m tests.secrets.bootstrap
"""

import json
import os

import boto3

SEED_USER_SECRETS: dict[str, dict[str, str]] = {
    "analyst": {"email": "analyst@demo.local", "password": "DemoPass123!"},
    "lead": {"email": "lead@demo.local", "password": "DemoPass123!"},
    "admin": {"email": "admin@demo.local", "password": "DemoPass123!"},
    "inactive": {"email": "inactive@demo.local", "password": "DemoPass123!"},
}

SECRET_NAME_PREFIX = "sentineldesk/users"

# App-level JWT signing key. Must match the API's JWT_SECRET (root .env), or
# tokens minted in tests will be rejected as invalid-signature instead of expired.
JWT_SECRET_NAME = "sentineldesk/jwt"
JWT_SECRET_VALUE = {
    "secret": "39e559a98f4543ba17661c92fa30b75810988677ab6d684a6b5c63957dbc41e4",
}


def _put_secret(client, name: str, value: dict[str, str]) -> None:
    """Create a secret, or overwrite it if it already exists."""
    payload = json.dumps(value)
    try:
        client.create_secret(Name=name, SecretString=payload)
        print(f"created secret {name}")
    except client.exceptions.ResourceExistsException:
        client.put_secret_value(SecretId=name, SecretString=payload)
        print(f"updated secret {name}")


def main() -> None:
    """Seed one secret per baseline user into Secrets Manager."""
    client = boto3.client(
        "secretsmanager",
        endpoint_url=os.getenv("AWS_ENDPOINT_URL", "http://localhost:4566"),
        region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", "test"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", "test"),
    )
    for key, value in SEED_USER_SECRETS.items():
        _put_secret(client, f"{SECRET_NAME_PREFIX}/{key}", value)
    _put_secret(client, JWT_SECRET_NAME, JWT_SECRET_VALUE)


if __name__ == "__main__":
    main()
