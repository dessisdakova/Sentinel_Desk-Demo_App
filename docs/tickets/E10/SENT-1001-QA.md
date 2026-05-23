# SENT-1001-QA — Test: Test reset endpoint

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E10 Test Harness and Bug Garden |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-1001](./SENT-1001.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Automated tests for the reset API — first ticket that **uses** `POST /api/v1/test/reset` (do not require reset before testing it).

---

## Description

**As a** QA engineer  
**I want** tests that verify the reset endpoint  
**So that** later suites can rely on `clean_db` (SENT-1002-QA)  

---

## Prerequisites

- [ ] [SENT-1001](./SENT-1001.md) implemented — reset route live
- [ ] Admin user seeded (`admin@demo.local`); full seed data per TEST_DATA.md (manual CLI seed before first test run)
- [ ] **Do not** call reset in a prerequisite — this ticket **tests** reset for the first time

---

## Test scope

- **api** — auth, status codes, non-prod guard
- **integration** — after reset, DB matches seed counts / stable IDs from TEST_DATA.md

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-1001-1 | api | Admin POST reset in local env | 200 or 204 per AC |
| QA-1001-2 | api | Analyst token POST reset | 403 |
| QA-1001-3 | integration | After reset, `ALERT_OPEN_HIGH` UUID present; user count = 3 |
| QA-1001-4 | api | `ENVIRONMENT=production` (if testable) | Reset disabled |

Extend with boundary cases from [SENT-1001](./SENT-1001.md) acceptance criteria.

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md)

---

## Out of scope

- `clean_db` fixture (SENT-1002-QA)
- Fixing unrelated bugs

---

## Definition of Done

- [ ] Tests run with `pytest tests/` (appropriate subset/markers)
- [ ] Test file paths documented in this ticket (edit when created)
