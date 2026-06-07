import os
from urllib.parse import urlparse

import pytest
from playwright.sync_api import APIRequestContext, Playwright

from tests.conftest import _port_is_open


@pytest.fixture(scope="session")
def base_url() -> str:
    """Root URL of the React frontend."""
    return os.getenv("FRONTEND_URL", "http://localhost:5173").rstrip("/")


@pytest.fixture(scope="session")
def require_frontend(base_url) -> None:
    """Skip E2E browser tests when the React dev server is not running.

    Probes the Vite port with a bare TCP check — the same pattern used by
    ``require_api`` in the root conftest. Add this fixture to any test or
    fixture that opens a real browser session against the frontend UI.

    :param base_url: Root URL of the React frontend (resolved from the
            ``FRONTEND_URL`` env var or defaulting to
            ``http://localhost:5173``).
    """
    parsed = urlparse(base_url)
    host = parsed.hostname or "localhost"
    port = parsed.port or 5173
    if not _port_is_open(host, port):
        pytest.skip(
            f"Frontend not available at {base_url}. "
            "Run: docker compose up -d."
        )


@pytest.fixture(scope="session")
def playwright_api_context(
    playwright: Playwright,
    api_base_url: str,
    require_api: None,
) -> APIRequestContext:
    """Playwright ``APIRequestContext`` pointed at the FastAPI service.

    Scope: session — one context is shared across all tests that request it,
    matching the scope of the httpx ``api_client`` in the root conftest.

    Use this fixture for:

    - Playwright-style API tests before the React frontend exists.
    - API-level setup and teardown inside browser (E2E) tests, for example
      seeding a user via API before navigating the UI.

    Response attributes use Playwright conventions:

    - ``.status``  — HTTP status code (int). Use instead of ``.status_code``.
    - ``.json()``  — Parsed JSON body (dict / list).
    - ``.headers`` — Response headers (case-insensitive dict-like).

    By default Playwright raises ``APIError`` on 4xx / 5xx responses.
    Pass ``fail_on_status_code=False`` to suppress this and assert manually.

    :param playwright: Playwright instance injected by pytest-playwright.
        playwright: Playwright instance injected by pytest-playwright.
    :param api_base_url: FastAPI root URL from the root conftest fixture
        (e.g. ``http://localhost:8000``).
    :param require_api: Gate fixture — skips the test if the FastAPI service
        is not reachable or its ``/health`` endpoint is unhealthy.
    :yield: Playwright ``APIRequestContext`` for the FastAPI service.
    """
    context = playwright.request.new_context(base_url=api_base_url)
    yield context
    context.dispose()
