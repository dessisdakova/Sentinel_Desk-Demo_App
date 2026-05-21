# SENT-802-QA — Test: Dashboard React and date picker

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E08 Dashboard and Audit |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-802](./SENT-802.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-802** — Dashboard React and date picker.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [ ] Implementation ticket **SENT-802** is complete and merged/runnable
- [ ] Prefer `POST /api/v1/test/reset` before run if SENT-1001 done; else re-seed manually

---

## Test scope

- **e2e** — add cases under `tests/e2e/`

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-802-1 | e2e | Happy path for primary AC | Pass |
| QA-802-2 | e2e | One negative or edge case | Correct error or UI message |
| QA-802-3 | e2e | Data matches seed or TEST_DATA.md stable IDs where applicable | Consistent |

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

