import pytest

from tests.api.constants import SEED_USERS

pytestmark = [pytest.mark.api, pytest.mark.reg]


def test_auth_with_valid_token_returns_correct_user_profile(api_client, analyst_token):
    """QA-104-4: Auth with valid token returns correct user profile."""
    response = api_client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {analyst_token}"})

    assert response.status_code == 200, "Valid token should return 200."
    body = response.json()
    assert body["email"] == SEED_USERS[0]["email"], "Incorrect email."
    assert body["role"] == SEED_USERS[0]["role"], "Incorrect role."
    assert body["display_name"] == SEED_USERS[0]["display_name"]


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
    pytest.param("ANALYST", "ANALYST", id="analyst"),
    pytest.param("LEAD", "LEAD", id="lead"),
    pytest.param("ADMIN", "ADMIN", id="admin"),
], indirect=["token"])
def test_me_returns_correct_role(api_client, token, expected_role):
    """QA-104-13: Each role token returns the correct role from /auth/me."""
    response = api_client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert response.json()["role"] == expected_role
