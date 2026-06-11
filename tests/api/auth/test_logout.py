import pytest

pytestmark = [pytest.mark.api, pytest.mark.reg]


@pytest.mark.parametrize("token", [
    pytest.param("ANALYST", id="analyst"),
    pytest.param("LEAD", id="lead"),
    pytest.param("ADMIN", id="admin"),
], indirect=["token"])
def test_log_out_returns_204(api_client, token):
    """QA-104-7: Log out returns 204."""
    response = api_client.post(
        "/api/v1/auth/logout",
        headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 204


def test_after_logout_token_still_valid(api_client, analyst_token):
    """QA-104-14: After logout token still valid."""
    response = api_client.post(
        "/api/v1/auth/logout",
        headers={"Authorization": f"Bearer {analyst_token}"})

    assert response.status_code == 204

    response = api_client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {analyst_token}"})

    assert response.status_code == 200
