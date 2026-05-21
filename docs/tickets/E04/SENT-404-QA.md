# SENT-404-QA — Test: IOC list component

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E04 Alert Detail |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-404](./SENT-404.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-404** — IOC list component.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [ ] Implementation ticket **SENT-404** is complete and merged/runnable
- [ ] Prefer `POST /api/v1/test/reset` before run if SENT-1001 done; else re-seed manually

---

## Test scope

- **e2e** — add cases under `tests/e2e/`

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-404-1 | e2e | Happy path for primary AC | Pass |
| QA-404-2 | e2e | One negative or edge case | Correct error or UI message |
| QA-404-3 | e2e | Data matches seed or TEST_DATA.md stable IDs where applicable | Consistent |

Extend with boundary cases from implementation acceptance criteria.

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md)

---

## Out of scope

- Fixing application bugs (file defects under BUG_GARDEN if found)
- Adding tests under `backend/` or `frontend/`

---

## Definition of Done

- [ ] Tests run with `pytest tests/` (appropriate subset/markers)
- [ ] No dependency on manual data unless documented in test docstring
- [ ] Test file paths documented in this ticket (edit when created)

