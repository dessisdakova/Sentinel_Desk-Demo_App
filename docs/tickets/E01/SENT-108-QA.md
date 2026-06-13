# SENT-108-QA — Test: Seed script for users

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Status** | Done |
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

- **api** — seed personas usable via HTTP; profile fields match `tests/constants.py` (covered by [SENT-104-QA](./SENT-104-QA.md), not duplicated here)
- **integration** — DB rows, bcrypt hashes, `active` flag, idempotency (AC2)

**No e2e** — seed is backend/CLI only.

**Overlap note:** [SENT-104-QA](./SENT-104-QA.md) covers the login *endpoint* and seed *persona* HTTP contract (`test_login.py`, `test_me.py`). This ticket adds **integration** assertions for the seed script’s DB side effects and idempotent re-run.

---

## Test cases

| ID | Layer | Scenario | Expected | Covered by |
|----|-------|----------|----------|------------|
| QA-108-1 | integration | Re-run of `scripts.seed` should not create duplicate users | Still exactly **4** rows for the seed emails; no duplicate email rows | `test_rerun_seed_does_not_duplicate_users` |
| QA-108-2 | integration | `SELECT active FROM users WHERE email = 'inactive@demo.local'` | `active` is `false` | `test_inactive_seed_user_has_active_false` |
| QA-108-3 | integration | `SELECT password_hash FROM users` for each seed email | Value starts with `$2b$` (bcrypt — not plaintext) | `test_seed_user_password_hash_is_bcrypt` (×4 parametrized) |
| QA-108-4 | integration | `COUNT(*)` where `email` is one of the four seed emails | Exactly **4** | `test_seed_users_count_is_four` |
| QA-108-5 | integration | Compare user row count for seed emails before and after a second seed run | Count unchanged (0 inserts on re-run) | `test_seed_rerun_does_not_change_row_count` |

### API coverage (SENT-104-QA — not re-tested here)

| Seed AC | SENT-104 test |
|---------|----------------|
| Active users login with `DemoPass123!` | `test_valid_login_returns_auth_token` |
| Inactive user returns `403 ACCOUNT_DISABLED` | `test_login_with_inactive_user_returns_403` |
| Profile `email` / `role` / `display_name` match constants | `test_auth_with_valid_token_returns_correct_user_profile` |

---

## Actual files

| File | Contents |
|------|----------|
| `tests/integration/infrastructure/test_seed_users.py` | QA-108-1 … QA-108-5 |
| `tests/integration/conftest.py` | `run_seed_script` fixture (subprocess: `docker compose exec api python -m scripts.seed`) |

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md) §2 — seed personas
- `tests/constants.py` — `SEED_USERS`, `SEED_INACTIVE_USER`, `SEED_PASSWORD`

Integration tests document the CLI seed prerequisite in each test docstring.

---

## Out of scope

- Fixing application bugs (file defects under BUG_GARDEN if found)
- Adding tests under `backend/` or `frontend/`
- Re-testing generic login validation already covered in SENT-104-QA

---

## Definition of Done

- [x] Tests run with `pytest tests/integration/infrastructure/test_seed_users.py -v` (8 tests: QA-108-3 runs ×4)
- [x] No dependency on manual data unless documented in test docstring (CLI seed prerequisite documented)
- [x] Test file paths documented in **Actual files** above
- [x] `ruff check tests/` passes with no new errors
