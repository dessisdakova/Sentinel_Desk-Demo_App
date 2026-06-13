# tests/e2e/pages/

Page Object Model (POM) classes — one module per page or route.

## Structure

| Module | Class | Route |
|--------|-------|-------|
| `base_page.py` | `BasePage` | — (base class, not a real page) |
| `login_page.py` | `LoginPage` | `/login` |

New pages are added here as the React frontend is built, one file per route.

## Conventions

- All page classes inherit from `BasePage`.
- Locators are declared as instance attributes in `__init__` using `page.get_by_test_id(...)`.
- Public methods expose high-level user actions only — callers never call `.fill()` or `.click()` directly.
- Use `expect(locator)` inside page methods for assertions that need auto-retry.

## Usage in a test

Use the `login_page` fixture from `tests/e2e/conftest.py` — it handles navigation and the `require_frontend` gate automatically:

```python
from playwright.sync_api import expect
import pytest

@pytest.mark.e2e
def test_analyst_can_login(login_page):
    login_page.login("analyst@demo.local", "DemoPass123!")
    expect(login_page.page).to_have_url("/dashboard")
```

When a test needs the raw `page` object directly (e.g. to inject sessionStorage), declare `require_frontend` explicitly:

```python
@pytest.mark.e2e
def test_something(page, require_frontend):
    page.goto("http://localhost:5173/login")
    ...
```
