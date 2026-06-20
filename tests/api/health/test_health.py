import pytest

pytestmark = [pytest.mark.api, pytest.mark.reg]


@pytest.mark.smoke
def test_health_returns_200_and_verify_response(api_client):
    """QA-102-1: Health endpoint returns 200, correct JSON, and echoes X-Request-ID."""
    request_id = "TEST0108-999999"

    # Call GET /health and send a custom request ID header.
    response = api_client.get("/health", headers={"X-Request-ID": request_id})

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert "X-Request-ID" in response.headers
    assert request_id == response.headers["X-Request-ID"]


def test_unknown_path_returns_404(api_client):
    """QA-102-2: Unknown API path returns HTTP 404."""
    # Request a route that does not exist in the API.
    response = api_client.get("/unknown-path")

    assert response.status_code == 404
