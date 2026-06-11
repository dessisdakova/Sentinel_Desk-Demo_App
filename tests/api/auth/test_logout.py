import pytest

pytestmark = [pytest.mark.api, pytest.mark.reg]


def test_log_out_returns_204(api_client, analyst_token):
    """QA-104-7: Log out returns 204."""
    response = api_client.post(
        "/api/v1/auth/logout",
        headers={"Authorization": f"Bearer {analyst_token}"})

    assert response.status_code == 204
