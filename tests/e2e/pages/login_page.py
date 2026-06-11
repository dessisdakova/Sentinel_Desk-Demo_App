from playwright.sync_api import Page

from tests.e2e.pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for the Login Page."""

    URL = "/login"

    def __init__(self, page: Page) -> None:
        """Declare all login-page locators."""
        super().__init__(page)
        self.page_root = page.get_by_test_id("page-login")
        self.email_input = page.get_by_test_id("login-email")
        self.password_input = page.get_by_test_id("login-password")
        self.submit_button = page.get_by_test_id("login-submit")
        self.error_message = page.get_by_test_id("login-error")

    def navigate(self, path: str = URL) -> None:
        """Navigate to the login page.

        :param path: Defaults to ``/login``.
        """
        super().navigate(path)

    def login(self, email: str, password: str) -> None:
        """Fill the email and password fields and click the submit button.

        :param email: User email address.
        :param password: User password.
        """
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()

    def is_page_loaded(self) -> bool:
        """Check if the login page root element is visible."""
        return self.page_root.is_visible()

    def is_error_visible(self) -> bool:
        """Check if an inline error message is displayed."""
        return self.error_message.is_visible()
