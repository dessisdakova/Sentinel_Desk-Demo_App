import pytest

from tests.constants import SEED_INACTIVE_USER, SEED_USERS, TOKEN_EXPIRES_IN

pytestmark = [pytest.mark.api, pytest.mark.reg]


IRRELEVANT_PASSWORD = "irrelevant-password"


@pytest.mark.smoke
@pytest.mark.parametrize(
    "user",
    [
        pytest.param(SEED_USERS[0], id="analyst"),
        pytest.param(SEED_USERS[1], id="lead"),
        pytest.param(SEED_USERS[2], id="admin"),
    ],
)
def test_valid_login_returns_auth_token(auth_client, user, password_for):
    """QA-104-1: Successful login returns auth token."""
    response = auth_client.login(user["email"], password_for(user["key"]))

    assert response.status_code == 200
    body = response.json()
    assert body["access_token"] is not None
    assert body["token_type"] == "bearer"
    assert body["expires_in"] == TOKEN_EXPIRES_IN


@pytest.mark.parametrize(
    "email,password",
    [
        pytest.param(SEED_USERS[0]["email"], "wrong_password", id="wrong-password"),
        pytest.param("unknown@demo.local", IRRELEVANT_PASSWORD, id="unknown-email"),
    ],
)
def test_login_with_invalid_credentials_return_401(auth_client, email, password):
    """QA-104-2/QA-104-11: Login with invalid password/unknown email returns 401."""
    response = auth_client.login_with_payload({"email": email, "password": password})

    assert response.status_code == 401
    body = response.json()
    assert body["error"]["code"] == "INVALID_CREDENTIALS"
    assert body["error"]["message"] == "Invalid email or password"


def test_login_with_missing_email_field_returns_422(auth_client):
    """QA-104-3: Login with missing email field returns 422."""
    response = auth_client.login_with_payload({"password": IRRELEVANT_PASSWORD})

    assert response.status_code == 422
    body = response.json()
    assert body["detail"][0]["msg"] == "Field required"
    assert body["detail"][0]["type"] == "missing"


def test_login_with_inactive_user_returns_403(auth_client, password_for):
    """QA-104-9: Login with inactive user returns 403."""
    response = auth_client.login(
        SEED_INACTIVE_USER["email"],
        password_for(SEED_INACTIVE_USER["key"]),
    )

    assert response.status_code == 403
    body = response.json()
    assert body["error"]["code"] == "ACCOUNT_DISABLED"
    assert body["error"]["message"] == "This account has been disabled"


def test_login_with_malformed_json_body_returns_422(auth_client):
    """QA-104-12: Login with malformed JSON body returns 422."""
    response = auth_client.login_with_malformed_body()

    assert response.status_code == 422
    body = response.json()
    assert body["detail"][0]["msg"] == "JSON decode error"
    assert body["detail"][0]["type"] == "json_invalid"
