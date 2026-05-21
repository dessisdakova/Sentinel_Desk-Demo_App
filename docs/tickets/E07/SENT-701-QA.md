# SENT-701-QA — Test: Webhook subscription model and admin API

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E07 Outbound Webhooks |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-701](./SENT-701.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-701** — Webhook subscription model and admin API.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [ ] Implementation ticket **SENT-701** is complete and merged/runnable
- [ ] Prefer `POST /api/v1/test/reset` before run if SENT-1001 done; else re-seed manually

---

## Test scope

- **api** — add cases under `tests/api/`
- **integration** — add cases under `tests/integration/`

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-701-1 | api | Happy path for primary AC | Pass |
| QA-701-2 | integration | One negative or edge case | Correct error or UI message |
| QA-701-3 | api | Data matches seed or TEST_DATA.md stable IDs where applicable | Consistent |

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

