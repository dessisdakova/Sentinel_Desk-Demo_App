# SENT-603-QA — Test: Playbook APIs and job status endpoint

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E06 Playbooks and Async Execution |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-603](./SENT-603.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-603** — Playbook APIs and job status endpoint.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [ ] Implementation ticket **SENT-603** is complete and merged/runnable
- [ ] **Seed baseline** � before SENT-1001 (E10): manual re-seed ([TEST_DATA.md �5](../../TEST_DATA.md#5-how-to-reset-by-phase) Option B/C); after SENT-1002-QA: `clean_db` or reset API

---

## Test scope

- **api** — add cases under `tests/api/`
- **integration** — add cases under `tests/integration/`

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-603-1 | api | Happy path for primary AC | Pass |
| QA-603-2 | integration | One negative or edge case | Correct error or UI message |
| QA-603-3 | api | Data matches seed or TEST_DATA.md stable IDs where applicable | Consistent |

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

