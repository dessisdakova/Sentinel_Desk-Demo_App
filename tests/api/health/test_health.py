import pytest

pytestmark = [pytest.mark.api, pytest.mark.reg]


@pytest.mark.smoke
def test_health_returns_200_and_verify_response(health_client):
    """QA-102-1: Health endpoint returns 200, correct JSON, and echoes X-Request-ID."""
    request_id = "TEST0108-999999"

    response = health_client.health(request_id=request_id)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert "X-Request-ID" in response.headers
    assert request_id == response.headers["X-Request-ID"]


def test_unknown_path_returns_404(health_client):
    """QA-102-2: Unknown API path returns HTTP 404."""
    response = health_client.unknown_path()

    assert response.status_code == 404
