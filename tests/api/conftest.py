
import pytest

from tests.api.constants import SEED_PASSWORD, SEED_USERS


def _login_as(role: str, api_client) -> str:
    """Logs in as the specified role and returns the token."""
    user = next(u for u in SEED_USERS if u["role"] == role)
    response = api_client.post(
        "/api/v1/auth/login",
        json={"email": user["email"], "password": SEED_PASSWORD},
    )
    if response.status_code != 200:
        raise ValueError(f"Failed to login as {role}: {response.json()}")
    return response.json()["access_token"]


@pytest.fixture(scope="session")
def analyst_token(api_client) -> str:
    """Session-scoped JWT for the seeded ANALYST user."""
    return _login_as("ANALYST", api_client)


@pytest.fixture(scope="session")
def lead_token(api_client) -> str:
    """Session-scoped JWT for the seeded LEAD user."""
    return _login_as("LEAD", api_client)


@pytest.fixture(scope="session")
def admin_token(api_client) -> str:
    """Session-scoped JWT for the seeded ADMIN user."""
    return _login_as("ADMIN", api_client)


@pytest.fixture(scope="session")
def token(request, api_client) -> str:
    """Log in as the requested role and return the access token.

    :param request: pytest request object; request.param is the role string.
    :return: JWT access token string.
    """
    return _login_as(request.param, api_client)
