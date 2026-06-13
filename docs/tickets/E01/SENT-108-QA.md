# SENT-108-QA — Test: Seed script for users

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-108](./SENT-108.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-108** — Seed script for users.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [x] Implementation ticket **SENT-108** is complete and merged/runnable
- [x] Baseline seed applied at least once (`docker compose exec api python -m scripts.seed` — see [TEST_DATA.md §3.1](../../TEST_DATA.md#31-seed-script--file-path-and-run-commands))

---

## Test scope

- **api** — verify seed personas are usable via HTTP and profile fields match `tests/constants.py`
- **integration** — verify DB rows, bcrypt hashes, `active` flag, and idempotency (AC2)

**No e2e** — seed is backend/CLI only.

**Overlap note:** [SENT-104-QA](./SENT-104-QA.md) covers the login *endpoint* contract. This ticket asserts the *seed data contract* — same emails/passwords, but focused on AC1 (four baseline users) and AC2 (idempotent re-run), not generic auth errors.

---

## Test cases

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-108-1 | integration | Re-run of scripts.seed should not create duplicate users | Still exactly **4** rows for the seed emails; no duplicate email rows |
| QA-108-2 | integration | `SELECT active FROM users WHERE email = 'inactive@demo.local'` | `active` is `false` |
| QA-108-3 | integration | `SELECT password_hash FROM users` for any seed email | Value starts with `$2b$` (bcrypt — not plaintext) |
| QA-108-4 | integration | `COUNT(*)` where `email` is one of the four seed emails | Exactly **4** |
| QA-108-5 | integration | Compare user row count for seed emails immediately before and after a second seed run | Count unchanged (0 inserts on re-run) |

### Planned files

Extend with boundary cases from implementation acceptance criteria.

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md)

---

## Out of scope

- Fixing application bugs (file defects under BUG_GARDEN if found)
- Adding tests under `backend/` or `frontend/`
- Re-testing generic login validation already covered in SENT-104-QA (wrong password, missing fields, malformed JSON)

---

## Definition of Done

- [ ] Tests run with `pytest tests/api/seed/ tests/integration/infrastructure/test_seed_users.py -v`
- [ ] No dependency on manual data unless documented in test docstring (document CLI seed prerequisite)
- [ ] Test file paths documented in **Planned files** above (tick when created)
- [ ] `ruff check tests/` passes with no new errors
