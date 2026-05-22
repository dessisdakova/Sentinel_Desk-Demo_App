import pytest


pytestmark = pytest.mark.api


def test_health_returns_200(api_client):
    """QA-102-1: Health endpoint returns 200 and all required data"""
    request_id = "TEST0108-999999"

    response = api_client.get("/health", headers={"X-Request-ID": request_id})
    
    assert response.status_code == 200 , "Health endpoint must return 200."
    assert response.json() == {"status": "ok"}, "Health response must return {'status': 'ok'}."
    assert "X-Request-ID" in response.headers, "X-Request-ID header must be present."
    assert request_id == response.headers["X-Request-ID"], "Request ID must be included in X-Request-ID."


def test_unknown_path_returns_404(api_client):
    """QA-102-2: Unknown path returns 404."""
    response = api_client.get("/unknown-path")

    assert response.status_code == 404, "Unknown/invalid path must return 404."
