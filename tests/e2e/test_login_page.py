import re

import pytest
from playwright.sync_api import Page, expect

from tests.constants import (
    SEED_ANALYST_USER,
    SEED_INACTIVE_USER,
    SEED_PASSWORD,
    SPA_ORIGIN
)
from tests.e2e.constants import ( 
    DASHBOARD_PATH,
    LOGIN_PATH,
    INVALID_CREDENTIALS_MESSAGE,
    MISSING_EMAIL_MESSAGE,
    MISSING_PASSWORD_MESSAGE,
    DISABLED_ACCOUNT_MESSAGE
)
from tests.e2e.pages.login_page import LoginPage

pytestmark = [pytest.mark.e2e, pytest.mark.reg]


@pytest.mark.smoke
def test_login_page_is_visible(login_page):
    """QA-107-1: All key login-page elements are present and visible."""
    expect(login_page.page_root).to_be_visible()
    expect(login_page.email_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.sign_in_button).to_be_visible()


def test_valid_credentials_redirect_to_dashboard(login_page):
    """QA-107-2: Valid credentials redirect to the dashboard."""
    # Login with valid credentials.
    login_page.login(SEED_ANALYST_USER["email"], SEED_PASSWORD)

    # re.compile() compiles the pattern into a regex object
    # re.escape() escapes special characters in the pattern
    expect(login_page.page).to_have_url(re.compile(re.escape(DASHBOARD_PATH)))


def test_wrong_password_shows_error(login_page):
    """QA-107-3: Wrong password displays an inline error and user stays on login page."""
    # Login with wrong password.
    login_page.login(SEED_ANALYST_USER["email"], "WrongPassword!")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text(INVALID_CREDENTIALS_MESSAGE)
    expect(login_page.page).to_have_url(re.compile(re.escape(LOGIN_PATH)))


def test_inactive_user_shows_error(login_page):
    """QA-107-4: Inactive account displays an inline error and user stays on login page."""
    # Login with inactive user.
    login_page.login(SEED_INACTIVE_USER["email"], SEED_PASSWORD)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text(DISABLED_ACCOUNT_MESSAGE)
    expect(login_page.page).to_have_url(re.compile(re.escape(LOGIN_PATH)))


def test_empty_email_shows_error(login_page):
    """QA-107-5: Submitting with an empty email field displays an inline error."""
    # Login with empty email.
    login_page.login("", SEED_PASSWORD)

    expect(login_page.error_missing_creds).to_be_visible()
    expect(login_page.error_missing_creds).to_have_text(MISSING_EMAIL_MESSAGE)


def test_empty_password_shows_error(login_page: LoginPage) -> None:
    """QA-107-6: Submitting with an empty password field displays an inline error."""
    # Login with empty password.
    login_page.login(SEED_ANALYST_USER["email"], "")

    expect(login_page.error_missing_creds).to_be_visible()
    expect(login_page.error_missing_creds).to_have_text(MISSING_PASSWORD_MESSAGE)


def test_authenticated_user_redirected_from_login(page, require_frontend, analyst_token):
    """QA-107-7: A pre-authenticated user navigating to login page is sent to the dashboard."""
    # Navigate to the base URL.
    page.goto(SPA_ORIGIN)
    # Inject the token via JS function.
    page.evaluate(
        "(token) => sessionStorage.setItem('sentinel_access_token', token)",
        analyst_token,
    )
    # Navigate to /login. The app boots, reads sessionStorage, calls /api/v1/auth/me,
    # and LoginPage redirects to /dashboard when isAuthenticated becomes true.
    page.goto(f"{SPA_ORIGIN}{LOGIN_PATH}")

    expect(page).to_have_url(re.compile(re.escape(DASHBOARD_PATH)))
