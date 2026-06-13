import pytest

from tests.constants import SPA_ORIGIN

pytestmark = [pytest.mark.api, pytest.mark.reg]


@pytest.mark.parametrize("path", ["/api/v1/auth/me", "/api/v1/admin/ping"])
def test_cors_options_preflight_from_UI_on_auth_me(api_client, path):
    """QA-106-2: CORS OPTIONS preflight from UI on /api/v1/auth/me."""
    response = api_client.options(
        path,
        headers={
            "Origin": SPA_ORIGIN,
            "Access-Control-Request-Method": "GET",
            "Access-Control-Request-Headers": "authorization",
        },
    )

    assert response.status_code == 200
    assert response.headers["Access-Control-Allow-Origin"] == SPA_ORIGIN
    assert "GET" in response.headers["Access-Control-Allow-Methods"]
    assert response.headers["Access-Control-Allow-Credentials"] == "true"
