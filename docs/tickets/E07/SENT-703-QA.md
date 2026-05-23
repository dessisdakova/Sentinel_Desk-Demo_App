# SENT-703-QA â€” Test: mock-siem callback endpoint

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E07 Outbound Webhooks |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-703](./SENT-703.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-703** â€” mock-siem callback endpoint.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [ ] Implementation ticket **SENT-703** is complete and merged/runnable
- [ ] **Seed baseline** — before SENT-1001 (E10): manual re-seed ([TEST_DATA.md §5](../../TEST_DATA.md#5-how-to-reset-by-phase) Option B/C); after SENT-1002-QA: `clean_db` or reset API

---

## Test scope

- **integration** â€” add cases under `tests/integration/`

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-703-1 | integration | Happy path for primary AC | Pass |
| QA-703-2 | integration | One negative or edge case | Correct error or UI message |
| QA-703-3 | integration | Data matches seed or TEST_DATA.md stable IDs where applicable | Consistent |

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

