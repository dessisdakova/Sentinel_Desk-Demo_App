import pytest

from tests.constants import SPA_ORIGIN

pytestmark = [pytest.mark.api, pytest.mark.reg]


@pytest.mark.parametrize(
    ("client_fixture", "preflight_method"),
    [
        pytest.param("auth_client", "me_preflight", id="auth-me"),
        pytest.param("admin_client", "ping_preflight", id="admin-ping"),
    ],
)
def test_cors_options_preflight_from_UI(
    client_fixture, preflight_method, auth_client, admin_client
):
    """QA-106-2: CORS OPTIONS preflight from UI on protected GET routes."""
    clients = {"auth_client": auth_client, "admin_client": admin_client}
    client = clients[client_fixture]
    response = getattr(client, preflight_method)(origin=SPA_ORIGIN)

    assert response.status_code == 200
    assert response.headers["Access-Control-Allow-Origin"] == SPA_ORIGIN
    assert "GET" in response.headers["Access-Control-Allow-Methods"]
    assert response.headers["Access-Control-Allow-Credentials"] == "true"
