# SENT-103-QA — Test: User model and Alembic initial migration

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Status** | **Done** |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-103](./SENT-103.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Automated integration coverage for **SENT-103** — `users` table schema, Alembic revision, `user_role` enum, and DB constraint behaviour (unique email, invalid role).

---

## Test cases

| ID | Scenario | Test function | Fixtures |
|----|----------|---------------|----------|
| QA-103-1 | Columns, types, NOT NULL | `test_users_table_has_expected_columns` | `postgres_connection` |
| QA-103-1 | Primary key on `id` | `test_users_table_has_primary_key_on_id` | `postgres_connection` |
| QA-103-1 | Unique index on `email` | `test_users_email_has_unique_index` | `postgres_connection` |
| QA-103-2 | Alembic at head (`20260523_0001`) | `test_alembic_migration_is_at_head` | `postgres_connection` |
| QA-103-3 | Column type is `user_role` enum | `test_users_table_has_expected_columns` (role column assert) | `postgres_connection` |
| QA-103-3 | Enum labels `ANALYST`, `LEAD`, `ADMIN` | `test_user_role_enum_has_expected_values` | `postgres_connection` |
| QA-103-4 | Invalid role insert → `InvalidTextRepresentation` | `test_invalid_role_insert_fails` | `postgres_write_connection` |
| QA-103-5 | Valid insert per role (parametrized) | `test_valid_role_insert_succeeds` (×3 roles) | `postgres_write_connection` |
| QA-103-6 | Duplicate email → `UniqueViolation` | `test_duplicate_email_insert_fails` | `postgres_write_connection` |

**QA-103-5 / QA-103-6:** Boundary cases beyond ticket minimum; map to SENT-103 AC (enum + unique email).

**Insert tests:** Use `postgres_write_connection` — transaction is rolled back after each test; no rows persist.

**Docker down:** Tests using `require_infrastructure` **skip** quickly.

**Migrations not applied:** Schema and migration tests **fail** (run `alembic upgrade head` first).

---

## Artifacts

| Path | Purpose |
|------|---------|
| `tests/integration/test_db_users_table.py` | **9** integration tests (schema, enum, inserts) |
| `tests/integration/test_db_migration_applied.py` | **1** integration test (Alembic revision) |
| `tests/integration/conftest.py` | `postgres_write_connection` fixture (auto-rollback) |

---

## How to run

```powershell
docker compose up -d
docker compose exec api alembic upgrade head

pytest tests/integration/test_db_users_table.py tests/integration/test_db_migration_applied.py -v
# or
pytest -m integ -v
```

With Docker stopped: integration tests **skip**. With Docker up but migrations missing: schema/migration tests **fail**.

---

## Definition of Done

- [x] Tests run with `pytest -m integ`
- [x] No dependency on manual data (insert tests generate UUIDs/emails; rollback via fixture)
- [x] Test file paths documented in this ticket
- [x] Matches [TESTING_STRATEGY.md](../../TESTING_STRATEGY.md)

---

## Completion

| Date | Notes |
|------|-------|
| 2026-06-07 | 10 tests across 2 files; QA-103-1 split into 3 functions; parametrized valid-role inserts; `postgres_write_connection` fixture |

**Next:** [SENT-104-QA](./SENT-104-QA.md)
