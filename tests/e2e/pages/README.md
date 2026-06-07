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

```python
from tests.e2e.pages.login_page import LoginPage

@pytest.mark.e2e
def test_analyst_can_login(page, require_frontend):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.assert_page_loaded()
    login_page.login("analyst@demo.local", "DemoPass123!")
    # assert post-login state here
```
