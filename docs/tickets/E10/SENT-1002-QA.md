# SENT-1002-QA — Extend E10 test harness (QA-only; no implement ticket)

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E10 Test Harness and Bug Garden |
| **Priority** | High |
| **Labels** | `qa`, `automation`, `harness` |
| **Implements after** | SENT-101-QA / SENT-102-QA foundation; [SENT-1001](./SENT-1001.md) for `clean_db` (optional until reset API exists) |
| **Test location** | Repository root `tests/` **only** |
| **Note** | Replaces superseded [SENT-1002](./SENT-1002.md) — no paired implementation ticket |

---

## Summary

Extend the E01 pytest harness with auth/reset fixtures and testing documentation for E10+ suites.

---

## Description

**As a** QA engineer  
**I want** shared fixtures and docs for reset- and token-based tests  
**So that** E10 Selenium and bug-garden suites build on the E01 foundation without the dev agent touching `tests/`  

**Prerequisite:** SENT-101-QA and SENT-102-QA complete (CONSTITUTION §3.6).

---

## Acceptance criteria

### AC1 — Extend `tests/conftest.py` (do not recreate E01 fixtures)

- [ ] Add `admin_api_client` fixture (logs in as `admin@demo.local`, returns authenticated httpx client)
- [ ] Add `clean_db` fixture calling `POST /api/v1/test/reset` when SENT-1001 is done; document fallback until then
- [ ] Add token helper utilities (e.g. login helper returning Bearer token for analyst/lead/admin)

### AC2 — Documentation

- [ ] README **QA automation** subsection: pytest markers, smoke run, reset workflow (when SENT-1001 exists)
- [ ] Confirm `requirements-test.txt` lists deps for E10 work; add any missing entries

### AC3 — Verification tests

- [ ] Add or extend tests under `tests/api/` or `tests/integration/` per test cases below

### AC4 — No duplicate bootstrap

- [ ] Do **not** recreate root `tests/`, `pytest.ini`, or E01 gate fixtures

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-1002-1 | integration | `admin_api_client` can call an admin-only route | Pass |
| QA-1002-2 | integration | Token helper returns valid Bearer for each seeded role | Pass |
| QA-1002-3 | api | `pytest -m smoke` still passes | No regression from E01 harness |

---

## Prerequisites

- [ ] SENT-1001 reset API for full `clean_db` behavior; until then, document manual re-seed in fixture docstring

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md)

---

## Out of scope

- Fixing application bugs (file under BUG_GARDEN if found)
- Adding tests under `backend/` or `frontend/`

---

## Definition of Done

- [ ] All acceptance criteria met
- [ ] Tests run with `pytest tests/` (appropriate subset/markers)
- [ ] Test file paths documented in this ticket (edit when created)
