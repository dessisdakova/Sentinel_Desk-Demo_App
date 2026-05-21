# SENT-505-QA — Test: Add to case from alert detail

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E05 Case Management |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-505](./SENT-505.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-505** — Add to case from alert detail.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [ ] Implementation ticket **SENT-505** is complete and merged/runnable
- [ ] Prefer `POST /api/v1/test/reset` before run if SENT-1001 done; else re-seed manually

---

## Test scope

- **e2e** — add cases under `tests/e2e/`

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-505-1 | e2e | Happy path for primary AC | Pass |
| QA-505-2 | e2e | One negative or edge case | Correct error or UI message |
| QA-505-3 | e2e | Data matches seed or TEST_DATA.md stable IDs where applicable | Consistent |

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

