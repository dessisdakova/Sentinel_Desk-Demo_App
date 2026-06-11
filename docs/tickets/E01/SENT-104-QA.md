# SENT-104-QA — Test: Auth API

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Status** | Done |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | Highest |
| **Labels** | `qa`, `api`, `integration` |
| **Implements after** | [SENT-104](./SENT-104.md) |
| **Test location** | `tests/api/auth/`, `tests/api/health/`, `tests/integration/auth/` |

---

## Summary

Automate API and integration coverage for authentication endpoints.

---

## Description

**As a** QA engineer  
**I want** repeatable auth tests  
**So that** later epics can depend on tokens and roles without manual login

---

## Prerequisites

- [x] SENT-104 implemented
- [x] SENT-108 seed users available (or manual seed)

---

## Test cases

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-104-1 | api | Login analyst, lead, admin with valid password | 200 + token each |
| QA-104-2 | api | Login wrong password | 401 INVALID_CREDENTIALS |
| QA-104-3 | api | Login missing email field | 422 |
| QA-104-4 | api | GET /auth/me with valid token | 200 profile matches role |
| QA-104-5 | api | GET /auth/me without Authorization | 401 |
| QA-104-6 | api | GET /auth/me malformed token | 401 |
| QA-104-7 | api | POST /auth/logout | 204 |
| QA-104-8 | integration | Login analyst, lead, admin → decode sub → DB user row email matches | Pass (parametrized × 3 roles) |
| QA-104-9 | api | Login inactive user (seed or fixture) | 403 ACCOUNT_DISABLED |
| QA-104-10 | api | Login success `expires_in`, covered in QA-104-1 | 28800 (or `JWT_EXPIRE_HOURS` × 3600) |
| QA-104-11 | api | Login with wrong email (unknown user) | 401 INVALID_CREDENTIALS |
| QA-104-12 | api | Login with malformed JSON body | 422 |
| QA-104-13 | api | Analyst token on /auth/me | returns role ANALYST |
| QA-104-14 | api | After logout 204 | /auth/me still works with same token |

---

## Actual files

| File | Contents |
|------|----------|
| `tests/api/auth/test_login.py` | QA-104-1, 2, 3, 9, 11, 12 |
| `tests/api/auth/test_me.py` | QA-104-4, 5, 6, 13 |
| `tests/api/auth/test_logout.py` | QA-104-7, 14 |
| `tests/api/auth/test_jwt_token.py` | QA-104-10 |
| `tests/integration/auth/test_login_token.py` | QA-104-8 |
| `tests/api/conftest.py` | `analyst_token`, `lead_token`, `admin_token`, `token` (indirect) fixtures |
| `tests/api/constants.py` | `SEED_USERS`, `SEED_INACTIVE_USER`, `SEED_PASSWORD`, `TOKEN_EXPIRES_IN` |

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md) — section 2

---

## Definition of Done

- [x] `pytest tests/api/ tests/integration/auth/ -v` passes (21 tests)
- [x] No tests under `backend/`
