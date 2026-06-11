import pytest

from tests.api.constants import (
    SEED_INACTIVE_USER,
    SEED_PASSWORD,
    SEED_USERS,
    TOKEN_EXPIRES_IN,
)

pytestmark = [pytest.mark.api, pytest.mark.reg]


@pytest.mark.smoke
def test_valid_login_returns_auth_token(api_client):
    """QA-104-1: Successful login returns auth token."""
    active_users = [user for user in SEED_USERS if user["status"] == "active"]

    for user in active_users:
        response = api_client.post(
            "/api/v1/auth/login",
            json={"email": user["email"], "password": user["password"]}
        )

        assert response.status_code == 200
        body = response.json()
        assert body["access_token"] is not None
        assert body["token_type"] == "bearer"
        assert body["expires_in"] == TOKEN_EXPIRES_IN


@pytest.mark.parametrize("email,password", [
    pytest.param(SEED_USERS[0]["email"], "wrong_password", id="wrong-password"),
    pytest.param("unknown@demo.local", SEED_PASSWORD, id="unknown-email"),
])
def test_login_with_invalid_credentials_return_401(api_client, email, password):
    """QA-104-2/QA-104-11: Login with invalid password/unknown email returns 401."""
    invalid_user = {"email": email, "password": password}

    response = api_client.post("/api/v1/auth/login", json=invalid_user)

    assert response.status_code == 401
    body = response.json()
    assert body["error"]["code"] == "INVALID_CREDENTIALS"
    assert body["error"]["message"] == "Invalid email or password"


def test_login_with_missing_email_field_returns_422(api_client):
    """QA-104-3: Login with missing email field returns 422."""
    missing_email_user = {"password": SEED_PASSWORD}

    response = api_client.post("/api/v1/auth/login", json=missing_email_user)

    assert response.status_code == 422
    body = response.json()
    assert body["detail"][0]["msg"] == "Field required"
    assert body["detail"][0]["type"] == "missing"


def test_login_with_inactive_user_returns_403(api_client):
    """QA-104-9: Login with inactive user returns 403."""
    inactive_user = {"email": SEED_INACTIVE_USER["email"], "password": SEED_PASSWORD}

    response = api_client.post("/api/v1/auth/login", json=inactive_user)

    assert response.status_code == 403
    body = response.json()
    assert body["error"]["code"] == "ACCOUNT_DISABLED"
    assert body["error"]["message"] == "This account has been disabled"


def test_login_with_malformed_json_body_returns_422(api_client):
    """QA-104-12: Login with malformed JSON body returns 422."""
    response = api_client.post(
        "/api/v1/auth/login",
        content=b"{not valid json}",
        headers={"Content-Type": "application/json"}
        )

    assert response.status_code == 422
    body = response.json()
    assert body["detail"][0]["msg"] == "JSON decode error"
    assert body["detail"][0]["type"] == "json_invalid"
