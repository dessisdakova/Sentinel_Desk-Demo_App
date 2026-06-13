import pytest

from tests.api.constants import SPA_ORIGIN


pytestmark = [pytest.mark.api, pytest.mark.reg]


def test_cors_options_preflight_from_localhost_5173_on_auth_me(api_client):
    """QA-106-2: CORS OPTIONS preflight from Origin: http://localhost:5173 on /api/v1/auth/me"""
    response = api_client.options(
        "/api/v1/auth/me",
        headers={
            "Origin": SPA_ORIGIN,
            "Access-Control-Request-Method": "GET",
            "Access-Control-Request-Headers": "authorization",
        },
    )

    assert response.status_code == 200
    assert response.headers["Access-Control-Allow-Origin"] == SPA_ORIGIN
    assert response.headers["Access-Control-Allow-Credentials"] == "true"
