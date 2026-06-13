import os
from urllib.parse import urlparse

import pytest
from playwright.sync_api import Page

from tests.conftest import _port_is_open
from tests.constants import SPA_ORIGIN
from tests.e2e.constants import LOGIN_PATH
from tests.e2e.pages.login_page import LoginPage


@pytest.fixture(scope="session")
def base_url() -> str:
    """Root URL of the React frontend.

    :return: Frontend base URL with no trailing slash.
    """
    return os.getenv("FRONTEND_URL", SPA_ORIGIN).rstrip("/")


@pytest.fixture(scope="session")
def require_frontend(base_url) -> None:
    """Skip E2E browser tests when the React dev server is not running.

    :param base_url: Root URL of the React frontend.
    """
    parsed = urlparse(base_url)
    host = parsed.hostname or "localhost"
    port = parsed.port or 5173
    if not _port_is_open(host, port):
        pytest.skip(
            f"Frontend not available at {base_url}. "
            "Run: docker compose up -d."
        )


@pytest.fixture(scope="function")
def login_page(page: Page, require_frontend) -> LoginPage:
    """Navigate to the login page and return a ready LoginPage instance.

    :param page: Playwright built-in fixture.
    :return: LoginPage instance.
    """
    return LoginPage.open(page)
