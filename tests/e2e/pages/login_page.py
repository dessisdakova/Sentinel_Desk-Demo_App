from playwright.sync_api import Page

from tests.e2e.pages.base_page import BasePage
from tests.constants import LOGIN_PATH


class LoginPage(BasePage):
    """Page Object for the Login Page."""
    def __init__(self, page: Page) -> None:
        """Declare all login-page locators."""
        super().__init__(page)
        self.page_root = page.locator("[data-testid='page-login']")
        self.email_input = page.locator("[data-testid='login-email']")
        self.password_input = page.locator("[data-testid='login-password']")
        self.sign_in_button = page.locator("[data-testid='login-submit']")

    @classmethod
    def open(cls, page: Page) -> LoginPage:
        """Navigate to login page and return a LoginPage instance."""
        instance = cls(page)
        instance.navigate(LOGIN_PATH)
        return instance

    def login(self, email: str, password: str) -> None:
        """Fill the email and password fields and click the submit button.

        :param email: User email address.
        :param password: User password.
        """
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.sign_in_button.click()

    def is_page_loaded(self) -> bool:
        """Check if the login page root element is visible."""
        return self.page_root.is_visible()

