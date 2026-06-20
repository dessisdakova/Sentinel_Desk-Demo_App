# SENT-105-QA — Test: RBAC dependency require_roles

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-105](./SENT-105.md) |
| **Test location** | Repository root `tests/` **only** |
| **Status** | Done |

---

## Summary

Design and implement automated tests for **SENT-105** — RBAC dependency require_roles.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [x] Implementation ticket **SENT-105** is complete and merged/runnable

---

## Test scope

- **api** — add cases under `tests/api/`
- **integration** — add cases under `tests/integration/`

---

## Test cases

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-105-1 | api | Admin role can access /admin/ping — response body has `message` and valid UUID `user_id` | 200 |
| QA-105-2 | api | Lead role cannot access /admin/ping — error body has `FORBIDDEN` code | 403 |
| QA-105-3 | api | Analyst role cannot access /admin/ping — error body has `FORBIDDEN` code | 403 |
| QA-105-4 | api | Missing Authorization header cannot access /admin/ping — error body has `UNAUTHORIZED` code | 401 |
| QA-105-5 | integration | `user_id` in response matches admin UUID queried from DB by email | Pass |

---

## Test files

- `tests/api/admin/test_admin_ping.py`
- `tests/integration/admin/test_admin_rbac.py`

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md)

---

## Out of scope

- Fixing application bugs (file defects under BUG_GARDEN if found)
- Adding tests under `backend/` or `frontend/`

---

## Definition of Done

- [x] Tests run with `pytest tests/` (appropriate subset/markers)
- [x] No dependency on manual data unless documented in test docstring
- [x] Test file paths documented in this ticket (edit when created)
