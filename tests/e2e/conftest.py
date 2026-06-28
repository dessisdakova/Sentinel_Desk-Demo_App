import os
from pathlib import Path
from urllib.parse import urlparse

import allure
import pytest
from playwright.sync_api import Page

from tests.conftest import _port_is_open
from tests.constants import SPA_ORIGIN
from tests.e2e.pages.login_page import LoginPage


def _attach_playwright_artifacts(artifact_dir: Path) -> None:
    """Attach Playwright failure artifacts from disk to the current Allure test."""
    for screenshot in sorted(artifact_dir.glob("test-failed*.png")):
        allure.attach.file(
            str(screenshot),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
    trace = artifact_dir / "trace.zip"
    if trace.is_file():
        allure.attach.file(
            str(trace),
            name="trace",
            attachment_type=allure.attachment_type.ZIP,
        )


@pytest.fixture(autouse=True)
def _playwright_output_path_for_allure(request, output_path) -> None:
    """Resolve pytest-playwright's per-test artifact dir for the Allure hook."""
    request.node._playwright_output_path = output_path


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Attach Playwright screenshot and trace to Allure after a failing E2E test."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        item.rep_call = report
        return
    if report.when != "teardown":
        return

    call_report = getattr(item, "rep_call", None)
    if call_report is None or not call_report.failed:
        return

    artifact_dir = getattr(item, "_playwright_output_path", None)
    if artifact_dir is not None:
        _attach_playwright_artifacts(Path(artifact_dir))


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
            "Run: docker compose up -d  OR  cd frontend && npm run dev"
        )


@pytest.fixture(scope="function")
def login_page(page: Page, require_frontend) -> LoginPage:
    """Navigate to the login page and return a ready LoginPage instance.

    :param page: Playwright built-in fixture — one browser tab per test.
    :param require_frontend: Gate fixture — skips if the Vite dev server is not running.
    :return: LoginPage instance already navigated to /login.
    """
    return LoginPage.open(page)
