# SENT-201-QA — Test: Alert and AlertEvent models and migration

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E02 Alert Ingestion and Async Enrichment |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-201](./SENT-201.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-201** — Alert and AlertEvent models and migration.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [ ] Implementation ticket **SENT-201** is complete and merged/runnable

---

## Test scope

- **integration** — add cases under `tests/integration/`

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-201-1 | integration | Verify alert table exist with expected schema | Pass |
| QA-201-2 | integration | Verify alert table's columns data type | Pass |
| QA-201-3 | integration | alert table's primary key is 'id' | Pass |
| QA-201-4 | integration | alert table's foreign key is 'assigned_to_id' from users table | Pass |
| QA-201-5 | integration | Verify alert_events table exist with expected schema | Pass |
| QA-201-6 | integration | Verify alert_events table's columns data type | Pass |
| QA-201-7 | integration | alert_events table's primary key is id | Pass |
| QA-201-8 | integration | alert_events table's foreign keys are 'alert_id' from alerts table and 'created_by' from users table | Pass |
| QA-201-9 | integration | Verify composite index on (status, severity, created_at DESC) and index on (assigned_to_id) exist | Pass |
| QA-201-10 | integration | Verify migration runs cleanly with alembic upgrade head | Pass |

Extend with boundary cases from implementation acceptance criteria.

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

