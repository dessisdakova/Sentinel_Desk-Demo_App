# SENT-106-QA — Test: React app shell, router, auth context

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-106](./SENT-106.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-106** — React app shell, router, auth context.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [ ] Implementation ticket **SENT-106** is complete and merged/runnable

---

## Test scope

- **api** — auth-related API checks if not already covered in SENT-104-QA
- **integration** — optional shell/route smoke via API only

**No e2e** — browser scaffold starts in [SENT-107-QA](./SENT-107-QA.md) after the login page exists.

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-106-1 | api | Unauthenticated request to a protected route returns 401 | `401` with error body; no data leaked |
| QA-106-2 | api | Request with expired or malformed JWT returns 401 | `401 INVALID_TOKEN` |
| QA-106-3 | api | Valid analyst token calls `GET /api/v1/auth/me`; role claim matches seeded user | `200` with `role=ANALYST` |

Extend with boundary cases from implementation acceptance criteria (e.g. CORS preflight from `http://localhost:5173`).

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

