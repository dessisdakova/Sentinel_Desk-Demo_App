# SENT-1102-QA â€” Test: Locustfile sample for ingest and list

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E11 Portfolio Scale and NFR Hooks |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-1102](./SENT-1102.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-1102** â€” Locustfile sample for ingest and list.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [ ] **Seed baseline** — before SENT-1001 (E10): manual re-seed ([TEST_DATA.md §5](../../TEST_DATA.md#5-how-to-reset-by-phase) Option B/C); after SENT-1002-QA: `clean_db` or reset API

---

## Test scope

- **api** â€” add cases under `tests/api/`

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-1102-1 | api | Happy path for primary AC | Pass |
| QA-1102-2 | api | One negative or edge case | Correct error or UI message |
| QA-1102-3 | api | Data matches seed or TEST_DATA.md stable IDs where applicable | Consistent |

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

