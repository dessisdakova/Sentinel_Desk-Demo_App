from playwright.sync_api import Page


class BasePage:
    """Shared base for all Page Object Models."""

    def __init__(self, page: Page) -> None:
        """Store the Playwright Page instance for use by subclass locators and actions."""
        self._page = page

    def navigate(self, path: str = "") -> None:
        """Navigate to ``base_url + path``.

        :param path: URL path relative to ``base_url`` (e.g. ``"/login"``).
            Pass an empty string to navigate to the root URL.
        """
        self._page.goto(path)
