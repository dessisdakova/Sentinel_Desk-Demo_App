import pytest

pytestmark = [pytest.mark.e2e, pytest.mark.reg]


@pytest.mark.smoke
def test_health_returns_200_and_correct_body(playwright_api_context):
    """QA-107-PW-1: Health endpoint returns HTTP 200 with ``{"status": "ok"}``."""
    # Playwright API request context hits the same /health route as httpx tests.
    response = playwright_api_context.get("/health")

    assert response.status == 200, "Health endpoint must return 200."
    assert response.json() == {"status": "ok"}, (
        "Health response body must be {'status': 'ok'}."
    )


def test_health_echoes_request_id_header(playwright_api_context):
    """QA-107-PW-2: Health endpoint echoes the ``X-Request-ID`` header back to the caller."""
    request_id = "PWTEST-001"

    # Send a known request ID and check the API echoes it in the response.
    response = playwright_api_context.get(
        "/health", headers={"X-Request-ID": request_id}
    )

    assert response.status == 200
    assert response.headers.get("x-request-id") == request_id, (
        "Response must echo the X-Request-ID sent in the request."
    )


def test_unknown_path_returns_404(playwright_api_context):
    """QA-107-PW-3: Requesting an unknown API path returns HTTP 404."""
    # Do not fail the test automatically on 404 — we assert the status ourselves.
    response = playwright_api_context.get(
        "/unknown-path",
        fail_on_status_code=False,
    )

    assert response.status == 404, "Unknown path must return 404."
