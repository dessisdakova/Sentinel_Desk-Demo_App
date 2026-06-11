import uuid

import pytest

pytestmark = [pytest.mark.api, pytest.mark.reg]

@pytest.mark.smoke
def test_admin_ping_returns_200_for_admin(api_client, admin_token):
    """QA-105-1: Admin can access /admin/ping and get 200."""
    response = api_client.get(
        "/api/v1/admin/ping",
        headers={"Authorization": f"Bearer {admin_token}"})

    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "pong"
    assert "user_id" in body
    try:
        uuid.UUID(body["user_id"])
    except ValueError:
        pytest.fail("user_id should be a valid UUID string.")


@pytest.mark.parametrize("token", [
    pytest.param("LEAD", id="lead"),
    pytest.param("ANALYST", id="analyst"),
], indirect=["token"])
def test_admin_ping_returns_403_for_lead_and_analyst(api_client, token):
    """QA-105-2/QA-105-3: Lead and analyst cannot access /admin/ping and get 403."""
    response = api_client.get(
        "/api/v1/admin/ping",
        headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 403
    body = response.json()
    assert body["error"]["code"] == "FORBIDDEN"
    assert body["error"]["message"] == (
        "You do not have permission to perform this action")


def test_admin_ping_returns_401_for_missing_token(api_client):
    """QA-105-4: Missing token cannot access /admin/ping and get 401."""
    response = api_client.get("/api/v1/admin/ping")

    assert response.status_code == 401
    body = response.json()
    assert body["error"]["code"] == "UNAUTHORIZED"
    assert body["error"]["message"] == "Missing or invalid authorization header"
    assert body["error"]["details"] is None
