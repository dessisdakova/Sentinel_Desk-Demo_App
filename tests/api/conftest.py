from typing import Literal

import httpx
import pytest

from tests.conftest import API_TIMEOUT_SEC
from tests.data.auth_seed import SEED_USERS, SEED_PASSWORD


@pytest.fixture(scope="session")
def analyst_token(api_client) -> str:
    """Logs in as an analyst and returns the token, email, and role."""
    user = next((u for u in SEED_USERS if u["role"] == "ANALYST"), None)
    if user is None:
        raise ValueError("No seeded analyst user.")

    response = api_client.post(
        "/api/v1/auth/login",
        json={"email": user["email"], "password": SEED_PASSWORD},
        timeout=API_TIMEOUT_SEC,
    )

    if response.status_code != 200:
        raise ValueError(f"Failed to login as analyst: {response.json()}")
    return response.json()["access_token"]
