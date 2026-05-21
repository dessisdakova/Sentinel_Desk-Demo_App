# SENT-1003-QA — Test: Selenium conftest and page objects

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E10 Test Harness and Bug Garden |
| **Priority** | High |
| **Labels** | `qa`, `e2e`, `selenium` |
| **Implements after** | SENT-107, SENT-1002 (harness scaffolding) |
| **Test location** | `tests/e2e/` **only** |

---

## Summary

Add Selenium WebDriver fixtures and page objects for Login and Alert Queue.

---

## Description

**As a** QA engineer  
**I want** reusable E2E building blocks  
**So that** UI tests from E01 onward stay maintainable

---

## Prerequisites

- [ ] SENT-1002 harness exists (pytest.ini, conftest base)
- [ ] SENT-107 login page implemented
- [ ] E03 queue optional until E03 QA — stub POM methods OK in E10

---

## Deliverables

| File | Content |
|------|---------|
| `tests/e2e/conftest.py` | webdriver fixture (Chrome), base_url, screenshot on failure optional |
| `tests/e2e/pages/login_page.py` | LoginPage with data-testid selectors |
| `tests/e2e/pages/alert_queue_page.py` | AlertQueuePage skeleton (expand in SENT-303-QA) |
| `tests/e2e/test_login_smoke.py` | Login as analyst → dashboard visible |

---

## Test cases (minimum)

| ID | Scenario | Expected |
|----|----------|----------|
| QA-1003-1 | Login analyst | Lands on dashboard, page-login not visible |
| QA-1003-2 | Login invalid password | Stays on login, error shown |
| QA-1003-3 | Login admin | Nav shows admin entry when applicable |

---

## Definition of Done

- [ ] `pytest tests/e2e -m e2e` runs login smoke
- [ ] Uses WebDriverWait, not fixed sleep only
- [ ] No tests under frontend/

