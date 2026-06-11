import pytest

from tests.data.auth_seed import SEED_PASSWORD, SEED_USERS, TOKEN_EXPIRES_IN

pytestmark = [pytest.mark.api, pytest.mark.reg]


def test_valid_login_returns_auth_token(api_client):
    """QA-104-1: Successful login returns auth token."""
    for user in SEED_USERS:
        response = api_client.post(
            "/api/v1/auth/login",
            json={"email": user["email"], "password": user["password"]}
        )

        assert response.status_code == 200, f"Failed to login as {user['email']}"
        body = response.json()
        assert body["access_token"] is not None, "No access token returned."
        assert body["token_type"] == "bearer", "Invalid token type."
        assert body["expires_in"] == TOKEN_EXPIRES_IN, "Invalid expiration period."


def test_login_with_invalid_password_returns_401(api_client):
    """QA-104-2: Login with invalid password returns 401."""
    invalid_user = {"email": SEED_USERS[0]["email"], "password": "wrong_password"}

    response = api_client.post("/api/v1/auth/login", json=invalid_user)

    assert response.status_code == 401, (
        "Invalid password should return 401 Unauthorized.")
    body = response.json()
    assert body["error"]["code"] == "INVALID_CREDENTIALS", "Incorrect error code."
    assert body["error"]["message"] == "Invalid email or password", (
        "Incorrect error message.")


def test_login_with_missing_email_field_returns_422(api_client):
    """QA-104-3: Login with missing email field returns 422."""
    missing_email_user = {"password": SEED_PASSWORD}

    response = api_client.post("/api/v1/auth/login", json=missing_email_user)

    assert response.status_code == 422, (
        "Missing email field should return 422 Unprocessable Content." )
    body = response.json()
    assert body["detail"][0]["msg"] == "Field required", (
        "Incorrect error message.")
    assert body["detail"][0]["type"] == "missing", "Incorrect error type."
