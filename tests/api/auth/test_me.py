import pytest

from tests.constants import SEED_USERS

pytestmark = [pytest.mark.api, pytest.mark.reg]


@pytest.mark.parametrize("user, token", [
    pytest.param(SEED_USERS[0], "analyst", id="analyst"),
    pytest.param(SEED_USERS[1], "lead", id="lead"),
    pytest.param(SEED_USERS[2], "admin", id="admin"),
], indirect=["token"]
)
def test_auth_with_valid_token_returns_correct_user_profile(api_client, user, token):
    """QA-104-4: Auth with valid token returns correct user profile."""
    response = api_client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    body = response.json()
    assert body["email"] == user["email"]
    assert body["role"] == user["role"]
    assert body["display_name"] == user["display_name"]


def test_auth_with_missing_authorization_header_returns_401(api_client):
    """QA-104-5: Auth with missing Authorization header returns 401."""
    response = api_client.get("/api/v1/auth/me")

    assert response.status_code == 401
    body = response.json()
    assert body["error"]["code"] == "UNAUTHORIZED"
    assert body["error"]["message"] == "Missing or invalid authorization header"


def test_auth_with_malformed_token_returns_401(api_client):
    """QA-104-6: Auth with malformed token returns 401."""
    response = api_client.get(
        "/api/v1/auth/me",
        headers={"Authorization": "Bearer malformed_token"}
    )

    assert response.status_code == 401
    body = response.json()
    assert body["error"]["code"] == "UNAUTHORIZED"
    assert body["error"]["message"] == "Invalid or expired access token"


@pytest.mark.parametrize("token,expected_role", [
    pytest.param("analyst", "ANALYST", id="analyst"),
    pytest.param("lead", "LEAD", id="lead"),
    pytest.param("admin", "ADMIN", id="admin"),
], indirect=["token"])
def test_me_returns_correct_role(api_client, token, expected_role):
    """QA-104-13: Each role token returns the correct role from /auth/me."""
    response = api_client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert response.json()["role"] == expected_role


def test_auth_with_expired_token_returns_401(api_client, expired_token):
    """QA-106-1: Request with expired JWT returns 401."""
    response = api_client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {expired_token}"}
    )

    assert response.status_code == 401
    body = response.json()
    assert body["error"]["code"] == "UNAUTHORIZED"
    assert body["error"]["message"] == "Invalid or expired access token"
