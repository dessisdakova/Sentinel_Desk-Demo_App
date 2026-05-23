# SENT-1103-QA â€” Test: aria-label pass on login, dashboard, alert queue

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E11 Portfolio Scale and NFR Hooks |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-1103](./SENT-1103.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-1103** â€” aria-label pass on login, dashboard, alert queue.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [ ] **Seed baseline** — before SENT-1001 (E10): manual re-seed ([TEST_DATA.md §5](../../TEST_DATA.md#5-how-to-reset-by-phase) Option B/C); after SENT-1002-QA: `clean_db` or reset API
- [ ] **SENT-107-QA** E2E bootstrap complete (required for e2e scope)

---

## Test scope

- **e2e** â€” add cases under `tests/e2e/`

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-1103-1 | e2e | Happy path for primary AC | Pass |
| QA-1103-2 | e2e | One negative or edge case | Correct error or UI message |
| QA-1103-3 | e2e | Data matches seed or TEST_DATA.md stable IDs where applicable | Consistent |

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

