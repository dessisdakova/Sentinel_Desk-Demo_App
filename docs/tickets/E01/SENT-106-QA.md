# SENT-106-QA — Test: React app shell, router, auth context

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Status** | Done |
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

- [x] Implementation ticket **SENT-106** is complete and merged/runnable

---

## Test scope

- **api** — auth-related API checks if not already covered in SENT-104-QA
- **integration** — optional shell/route smoke via API only

**No e2e** — browser scaffold starts in [SENT-107-QA](./SENT-107-QA.md) after the login page exists.

---

## Test cases

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-106-1 | api | Request with expired JWT returns 401 | `401 UNAUTHORIZED` |
| QA-106-2 | api | CORS OPTIONS preflight from Origin: http://localhost:5173 on /api/v1/auth/me | Pass |
| QA-106-3 | api | CORS preflight on a protected route (`/api/v1/admin/ping`) | Pass |

Frontend ACs (router redirect, `sessionStorage`, role nav) are covered in [SENT-107-QA](./SENT-107-QA.md) E2E.

---

## Actual files

| File | Contents |
|------|----------|
| `tests/api/auth/test_me.py` | QA-106-1 (`test_auth_with_expired_token_returns_401`) |
| `tests/api/test_cors.py` | QA-106-2, QA-106-3 |
| `tests/api/constants.py` | `SPA_ORIGIN` |
| `tests/conftest.py` | `expired_token` fixture (mints synthetically expired JWT via `JWT_SECRET`) |
| `requirements-test.txt` | `PyJWT` (token minting for QA-106-1) |

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md)
- `JWT_SECRET` from `.env` (same value as API — used only to mint expired tokens in tests)

---

## Out of scope

- Fixing application bugs (file defects under BUG_GARDEN if found)
- Adding tests under `backend/` or `frontend/`

---

## Definition of Done

- [x] Tests run with `pytest tests/api/auth/test_me.py::test_auth_with_expired_token_returns_401 tests/api/test_cors.py -v` (3 tests)
- [x] No dependency on manual data unless documented in test docstring
- [x] Test file paths documented in this ticket (edit when created)