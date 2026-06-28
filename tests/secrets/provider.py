import json
import os
from functools import lru_cache

import boto3


def _secretsmanager_client():
    """Build a Secrets Manager client.

    Uses ``AWS_ENDPOINT_URL`` to target LocalStack when set.

    :return: A configured boto3 Secrets Manager client.
    """
    return boto3.client(
        "secretsmanager",
        endpoint_url=os.getenv("AWS_ENDPOINT_URL") or None,
        region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1"),
    )


@lru_cache(maxsize=None)
def get_secret(secret_name: str) -> dict[str, str]:
    """Fetch a JSON secret by name and parse it into a dict.

    Cached per secret name so each secret is fetched once per test session.

    :param secret_name: Secrets Manager secret id (e.g. ``sentineldesk/seed-users``).
    :return: Parsed secret payload as a dictionary.
    """
    response = _secretsmanager_client().get_secret_value(SecretId=secret_name)
    return json.loads(response["SecretString"])


def get_user_secret(user_key: str) -> dict[str, str]:
    """Fetch a seed user's {email, password} bundle by logical key.

    :param user_key: Logical user key (e.g. "analyst", "inactive").
    :return: Dict with "email" and "password".
    """
    prefix = os.getenv("SEED_SECRET_PREFIX", "sentineldesk/users")
    return get_secret(f"{prefix}/{user_key}")


def get_jwt_secret() -> str:
    """Fetch the JWT signing key from Secrets Manager.

    :return: The HS256 signing key string (must match the API's JWT_SECRET).
    """
    name = os.getenv("JWT_SECRET_NAME", "sentineldesk/jwt")
    return get_secret(name)["secret"]
