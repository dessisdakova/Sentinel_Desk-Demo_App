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

Bootstrap the E2E test layer and cover the login page — **first Selenium work in the project** (see TESTING_STRATEGY §4.3).

---

## Description

**As a** QA engineer  
**I want** a minimal Selenium scaffold and login tests  
**So that** later UI epics can add feature E2E tests without re-inventing WebDriver setup  

**Prerequisite:** SENT-101-QA / SENT-102-QA foundation (`tests/`, `pytest.ini`, root `conftest.py`).

---

## Deliverables (bootstrap)

| File | Content |
|------|---------|
| `tests/e2e/conftest.py` | WebDriver fixture (Chrome via WebDriver Manager), `base_url`, optional screenshot on failure |
| `tests/e2e/pages/login_page.py` | `LoginPage` using `data-testid` selectors from SENT-107 |
| `tests/e2e/test_login_page.py` | Login happy path, invalid password, role smoke as applicable |

Add `selenium` / `webdriver-manager` to `requirements-test.txt` if not present.

---

## Test scope

- **e2e** — creates `tests/e2e/` tree (first browser tests in project)

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-107-1 | e2e | Login analyst with valid password | Dashboard or post-login route visible |
| QA-107-2 | e2e | Login invalid password | Error shown; stay on login |
| QA-107-3 | e2e | `page-login` root `data-testid` present | Selector stable for POM |

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
- [ ] Uses `WebDriverWait`, not fixed sleep only
- [ ] Test file paths documented in this ticket (edit when created)
