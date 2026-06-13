# SENT-107-QA — Test: Login page with data-testid

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Labels** | `qa`, `automation`, `e2e-bootstrap` |
| **Implements after** | [SENT-107](./SENT-107.md) |
| **Test location** | Repository root `tests/` **only** |
| **Status** | Done |

---

## Summary

Bootstrap the E2E test layer and cover the login page — **first Playwright work in the project** (see TESTING_STRATEGY §4.3).

---

## Description

**As a** QA engineer  
**I want** a minimal Playwright scaffold and login tests  
**So that** later UI epics can add feature E2E tests without re-inventing browser setup  

**Prerequisite:** SENT-101-QA / SENT-102-QA foundation (`tests/`, `pytest.ini`, root `conftest.py`).

---

## Deliverables (bootstrap)

| File | Content |
|------|---------|
| `tests/e2e/conftest.py` | `base_url`, `require_frontend` gate fixture, `login_page` fixture |
| `tests/e2e/constants.py` | E2E path and expected-message constants |
| `tests/e2e/pages/base_page.py` | `BasePage` with `navigate()` helper and `page` property |
| `tests/e2e/pages/login_page.py` | `LoginPage` — `data-testid` locators, `open()` factory, `login()` action |
| `tests/e2e/test_login_page.py` | 7 login tests (QA-107-1 → QA-107-7) |

`pytest-playwright` is already in `requirements-test.txt`. After installing, run:

```powershell
playwright install chromium
```

---

## Test scope

- **e2e** — creates browser tests in `tests/e2e/` (requires `require_frontend`)

---

## Test cases

| ID | Layer | Scenario | Test function |
|----|-------|----------|---------------|
| QA-107-1 | e2e | Login page loads — all key elements visible | `test_login_page_is_visible` |
| QA-107-2 | e2e | Valid credentials redirect to `/dashboard` | `test_valid_credentials_redirect_to_dashboard` |
| QA-107-3 | e2e | Wrong password — inline error; stay on `/login` | `test_wrong_password_shows_error` |
| QA-107-4 | e2e | Inactive account — inline error; stay on `/login` | `test_inactive_user_shows_error` |
| QA-107-5 | e2e | Empty email — client-side validation error | `test_empty_email_shows_error` |
| QA-107-6 | e2e | Empty password — client-side validation error | `test_empty_password_shows_error` |
| QA-107-7 | e2e | Already-authenticated user at `/login` → redirect to `/dashboard` | `test_authenticated_user_redirected_from_login` |

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md)

---

## Out of scope

- Alert queue or other pages (E03+)
- Fixing application bugs (file defects under BUG_GARDEN if found)

---

## Definition of Done

- [x] `pytest tests/e2e -m e2e` runs login tests
- [x] Uses Playwright `expect()` and auto-wait — no `time.sleep()`
- [x] Test file paths documented in this ticket (edit when created)
