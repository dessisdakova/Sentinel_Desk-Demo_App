# SENT-107-QA — Test: Login page with data-testid

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Labels** | `qa`, `automation`, `e2e-bootstrap` |
| **Implements after** | [SENT-107](./SENT-107.md) |
| **Test location** | Repository root `tests/` **only** |

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
| `tests/e2e/conftest.py` | `playwright_api_context`, `base_url`, `require_frontend` gate fixture |
| `tests/e2e/pages/base_page.py` | `BasePage` with `navigate()` helper |
| `tests/e2e/pages/login_page.py` | `LoginPage` using `data-testid` selectors from SENT-107 |
| `tests/e2e/test_login_page.py` | Login happy path, invalid password, role smoke as applicable |

`pytest-playwright` is already in `requirements-test.txt`. After installing, run:

```powershell
playwright install chromium
```

---

## Test scope

- **e2e** — creates browser tests in `tests/e2e/` (requires `require_frontend`)

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-107-1 | e2e | Login analyst with valid password | Dashboard or post-login route visible |
| QA-107-2 | e2e | Login invalid password | Error shown; stay on login |
| QA-107-3 | e2e | `page-login` root `data-testid` present | `expect(login_page.page_root).to_be_visible()` passes |

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md)

---

## Out of scope

- Alert queue or other pages (E03+)
- Fixing application bugs (file defects under BUG_GARDEN if found)

---

## Definition of Done

- [ ] `pytest tests/e2e -m e2e` runs login tests
- [ ] Uses Playwright `expect()` and auto-wait — no `time.sleep()`
- [ ] Test file paths documented in this ticket (edit when created)
