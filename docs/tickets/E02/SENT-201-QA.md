# SENT-201-QA — Test: Alert and AlertEvent models and migration

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Status** | Done |
| **Epic** | SENT-E02 Alert Ingestion and Async Enrichment |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-201](./SENT-201.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Automated integration coverage for **SENT-201** — `alerts` and `alert_events` table schemas, indexes, foreign keys, and Alembic head revision `20260613_0002`.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [x] Implementation ticket **SENT-201** is complete and merged/runnable
- [x] Migrations applied (`docker compose exec api alembic upgrade head`)

---

## Test scope

- **integration** — direct PostgreSQL schema assertions under `tests/integration/infrastructure/`

**No api / e2e** — no HTTP endpoints in SENT-201.

---

## Test cases

| ID | Layer | Scenario | Test function |
|----|-------|----------|---------------|
| QA-201-1 | integration | `alerts` table column names | `test_alerts_table_has_expected_columns` |
| QA-201-2 | integration | `alerts` column types and nullability | `test_alerts_table_columns_have_correct_data_type` |
| QA-201-3 | integration | `alerts` primary key on `id` | `test_alerts_table_primary_key_is_correct` |
| QA-201-4 | integration | `alerts.assigned_to_id` → `users.id` | `test_alerts_table_foreign_key_is_correct` |
| QA-201-5 | integration | `alert_events` table column names | `test_alert_events_table_has_expected_columns` |
| QA-201-6 | integration | `alert_events` column types and nullability | `test_alert_events_table_columns_have_correct_data_type` |
| QA-201-7 | integration | `alert_events` primary key on `id` | `test_alert_events_table_primary_key_is_correct` |
| QA-201-8 | integration | `alert_events` FKs → `alerts.id`, `users.id` | `test_alert_events_table_foreign_keys_are_correct` |
| QA-201-9 | integration | Composite index `(status, severity, created_at DESC)` and index on `assigned_to_id` | `test_alerts_table_has_expected_indexes` |
| QA-201-10 | integration | Alembic at head (`20260613_0002`) | `test_alembic_migration_is_at_head` |

**Overlap note:** [SENT-103-QA](../E01/SENT-103-QA.md) also checks Alembic head via `tests/integration/infrastructure/test_db_migration.py`. That file’s `EXPECTED_MIGRATION_REVISION` is updated whenever a new migration ships; QA-201-10 duplicates the check in the alerts schema file for ticket traceability.

**Docker down:** Tests using `require_infrastructure` **skip** quickly.

**Migrations not applied:** Schema and migration tests **fail** (run `alembic upgrade head` first).

---

## Actual files

| File | Contents |
|------|----------|
| `tests/integration/infrastructure/test_alerts_table_schema.py` | QA-201-1 … QA-201-10 (10 tests) |

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md) — no alert seed rows required (schema-only tests)

---

## Out of scope

- Fixing application bugs (file defects under BUG_GARDEN if found)
- Adding tests under `backend/` or `frontend/`

---

## How to run

```powershell
docker compose up -d
docker compose exec api alembic upgrade head

pytest tests/integration/infrastructure/test_alerts_table_schema.py -v
# or
pytest -m integ -v
```

---

## Definition of Done

- [x] Tests run with `pytest tests/integration/infrastructure/test_alerts_table_schema.py -v` (10 tests)
- [x] No dependency on manual data unless documented in test docstring
- [x] Test file paths documented in **Actual files** above
- [x] `ruff check tests/` passes with no new errors
- [x] Matches [TESTING_STRATEGY.md](../../TESTING_STRATEGY.md)

---

## Completion

| Date | Notes |
|------|-------|
| 2026-06-14 | 10 integration tests in one file; FK assertions use `constraint_column_usage`; index checks driven from `expected_indexes` dict |

**Next:** [SENT-202-QA](./SENT-202-QA.md)
