import pytest

from tests.constants import SEED_USERS

pytestmark = [pytest.mark.api, pytest.mark.reg]


@pytest.mark.parametrize(
    "user, token",
    [
        pytest.param(SEED_USERS[0], "ANALYST", id="analyst"),
        pytest.param(SEED_USERS[1], "LEAD", id="lead"),
        pytest.param(SEED_USERS[2], "ADMIN", id="admin"),
    ],
    indirect=["token"],
)
def test_auth_with_valid_token_returns_correct_user_profile(auth_client, user, token):
    """QA-104-4: Auth with valid token returns correct user profile."""
    response = auth_client.me(token=token)

    assert response.status_code == 200
    body = response.json()
    assert body["email"] == user["email"]
    assert body["role"] == user["role"]
    assert body["display_name"] == user["display_name"]


def test_auth_with_missing_authorization_header_returns_401(auth_client):
    """QA-104-5: Auth with missing Authorization header returns 401."""
    response = auth_client.me()

    assert response.status_code == 401
    body = response.json()
    assert body["error"]["code"] == "UNAUTHORIZED"
    assert body["error"]["message"] == "Missing or invalid authorization header"


def test_auth_with_malformed_token_returns_401(auth_client):
    """QA-104-6: Auth with malformed token returns 401."""
    response = auth_client.me(token="malformed_token")

    assert response.status_code == 401
    body = response.json()
    assert body["error"]["code"] == "UNAUTHORIZED"
    assert body["error"]["message"] == "Invalid or expired access token"


@pytest.mark.parametrize(
    "token,expected_role",
    [
        pytest.param("ANALYST", "ANALYST", id="analyst"),
        pytest.param("LEAD", "LEAD", id="lead"),
        pytest.param("ADMIN", "ADMIN", id="admin"),
    ],
    indirect=["token"],
)
def test_me_returns_correct_role(auth_client, token, expected_role):
    """QA-104-13: Each role token returns the correct role from /auth/me."""
    response = auth_client.me(token=token)

    assert response.status_code == 200
    assert response.json()["role"] == expected_role


def test_auth_with_expired_token_returns_401(auth_client, expired_token):
    """QA-106-1: Request with expired JWT returns 401."""
    response = auth_client.me(token=expired_token)

    assert response.status_code == 401
    body = response.json()
    assert body["error"]["code"] == "UNAUTHORIZED"
    assert body["error"]["message"] == "Invalid or expired access token"
