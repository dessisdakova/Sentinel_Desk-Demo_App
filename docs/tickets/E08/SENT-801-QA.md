# SENT-801-QA — Test: metrics summary API and Redis cache

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E08 Dashboard and Audit |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-801](./SENT-801.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-801** — metrics summary API and Redis cache.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [ ] Implementation ticket **SENT-801** is complete and merged/runnable
- [ ] **Seed baseline** � before SENT-1001 (E10): manual re-seed ([TEST_DATA.md �5](../../TEST_DATA.md#5-how-to-reset-by-phase) Option B/C); after SENT-1002-QA: `clean_db` or reset API

---

## Test scope

- **api** — add cases under `tests/api/`
- **integration** — add cases under `tests/integration/`

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-801-1 | api | Happy path for primary AC | Pass |
| QA-801-2 | integration | One negative or edge case | Correct error or UI message |
| QA-801-3 | api | Data matches seed or TEST_DATA.md stable IDs where applicable | Consistent |

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

