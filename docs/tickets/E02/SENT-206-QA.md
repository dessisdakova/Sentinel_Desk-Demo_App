# SENT-206-QA — Test: Seed alerts per TEST_DATA.md

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E02 Alert Ingestion and Async Enrichment |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-206](./SENT-206.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-206** — Seed alerts per TEST_DATA.md.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [ ] Implementation ticket **SENT-206** is complete and merged/runnable

---

## Test scope

- **api** — add cases under `tests/api/`
- **integration** — add cases under `tests/integration/`

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-206-1 | api | Happy path for primary AC | Pass |
| QA-206-2 | integration | One negative or edge case | Correct error or UI message |
| QA-206-3 | api | Data matches seed or TEST_DATA.md stable IDs where applicable | Consistent |

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

