import pytest

pytestmark = [pytest.mark.api, pytest.mark.reg]


@pytest.mark.parametrize(
    "token",
    [
        pytest.param("ANALYST", id="analyst"),
        pytest.param("LEAD", id="lead"),
        pytest.param("ADMIN", id="admin"),
    ],
    indirect=["token"],
)
def test_log_out_returns_204(auth_client, token):
    """QA-104-7: Log out returns 204."""
    response = auth_client.logout(token=token)

    assert response.status_code == 204


def test_after_logout_token_still_valid(auth_client, analyst_token):
    """QA-104-14: After logout token still valid."""
    response = auth_client.logout(token=analyst_token)

    assert response.status_code == 204

    response = auth_client.me(token=analyst_token)

    assert response.status_code == 200
