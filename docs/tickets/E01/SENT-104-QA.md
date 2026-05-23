# SENT-104-QA — Test: Auth API

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | Highest |
| **Labels** | `qa`, `api`, `integration` |
| **Implements after** | [SENT-104](./SENT-104.md) |
| **Test location** | `tests/api/`, `tests/integration/` |

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

- [ ] SENT-104 implemented
- [ ] SENT-108 seed users available (or manual seed)

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
| QA-104-8 | integration | Login analyst → decode sub → DB user row email matches | Pass |
| QA-104-9 | api | Login inactive user (seed or fixture) | 403 ACCOUNT_DISABLED |
| QA-104-10 | api | Login success `expires_in` | 28800 (or `JWT_EXPIRE_HOURS` × 3600) |

---

## Suggested files

- `tests/api/test_auth.py`
- `tests/conftest.py` — add `analyst_token`, `lead_token`, `admin_token` fixtures (extend in E10)

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md) — section 2

---

## Definition of Done

- [ ] `pytest tests/api/test_auth.py -v` passes
- [ ] No tests under `backend/`
