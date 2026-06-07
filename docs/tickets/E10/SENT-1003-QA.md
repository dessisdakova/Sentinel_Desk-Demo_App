# SENT-1003-QA — Standardize Playwright POM and e2e conftest (QA-only)

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E10 Test Harness and Bug Garden |
| **Priority** | High |
| **Labels** | `qa`, `e2e`, `playwright` |
| **Implements after** | [SENT-107-QA](../E01/SENT-107-QA.md) (e2e bootstrap); [SENT-1002-QA](./SENT-1002-QA.md) recommended |
| **Test location** | `tests/e2e/` **only** |
| **Note** | **Does not** first-create `tests/e2e/` — that happens in SENT-107-QA (see TESTING_STRATEGY §4.3) |

---

## Summary

Enhance the existing E2E scaffold with shared page objects, conftest polish, and login smoke coverage.

---

## Description

**As a** QA engineer  
**I want** reusable, consistent E2E building blocks  
**So that** feature tests from E03 onward stay maintainable  

**Prerequisite:** SENT-107-QA already created `tests/e2e/conftest.py`, `pages/login_page.py`, and basic login tests.

---

## Acceptance criteria

### AC1 — Enhance (do not recreate bootstrap)

- [ ] Polish `tests/e2e/conftest.py` (shared helpers, any additional session fixtures)
- [ ] Ensure `pages/login_page.py` follows POM conventions used going forward
- [ ] Add `pages/alert_queue_page.py` (skeleton OK — expand in SENT-303-QA)
- [ ] Add or refine `tests/e2e/test_login_smoke.py` if not complete in SENT-107-QA

### AC2 — Verification

- [ ] `pytest tests/e2e -m e2e` runs login smoke
- [ ] Uses Playwright `expect()` and auto-wait — no `time.sleep()`

---

## Test cases (minimum)

| ID | Scenario | Expected |
|----|----------|----------|
| QA-1003-1 | Login analyst | Lands on dashboard, `page-login` not visible |
| QA-1003-2 | Login invalid password | Stays on login, error shown |
| QA-1003-3 | Login admin | Nav shows admin entry when applicable |

---

## Definition of Done

- [ ] All acceptance criteria met
- [ ] No tests under `frontend/`
