from playwright.sync_api import Page

from tests.constants import SPA_ORIGIN


class BasePage:
    """Shared base for all Page Object Models."""

    def __init__(self, page: Page) -> None:
        """Store Page instance for use by subclass locators and actions."""
        self._page = page

    @property
    def page(self) -> Page:
        """The underlying Playwright Page instance."""
        return self._page

    def navigate(self, path: str = "") -> None:
        """Navigate to page URL.

        :param path: URL path (e.g. /login).
            Pass an empty string to navigate to the root URL.
        """
        self._page.goto(f"{SPA_ORIGIN}{path}")
