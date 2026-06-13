import os
from urllib.parse import urlparse

import pytest
from playwright.sync_api import APIRequestContext, Playwright

from tests.conftest import _port_is_open


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


