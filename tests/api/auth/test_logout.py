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
