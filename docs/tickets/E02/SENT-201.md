# SENT-201 — Alert and AlertEvent models and migration

| Field | Value |
|-------|-------|git add .
| **Type** | Story |
| **Epic** | SENT-E02 Alert Ingestion and Async Enrichment |
| **Priority** | High |
| **Story Points** | 5 |
| **Status** | Done |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-201-QA](./SENT-201-QA.md) |

---

## Summary

Alert and AlertEvent models and migration.

---

## Description

**As a** SOC platform  
**I want** an `alerts` table with full status, severity, and IOC schema and an `alert_events` timeline table  
**So that** ingested alerts have a versioned DB foundation that all triage, enrichment, and audit features can build on

---

## Acceptance criteria

### AC1 — Alert table schema

- [x] `alerts` table per CONSTITUTION §5 and §5.2: columns include `id` (UUID PK), `external_id` (unique string), `source` (enum), `severity` (enum), `status` (`AlertStatus` enum), `enrichment_status` (separate column, not `AlertStatus`), `title`, `ioc_list` (JSONB — see CONSTITUTION §5 note), `assigned_to_id` (FK users), `sla_due_at`, `created_at`, `updated_at`

### AC2 — AlertEvent table schema

- [x] `alert_events` table: `id` (UUID PK), `alert_id` (FK alerts), `event_type` (string), `payload` (JSONB), `created_by` (FK users nullable), `created_at`

### AC3 — Indexes and foreign keys

- [x] Composite index on `(status, severity, created_at DESC)` and index on `(assigned_to_id)` per ARCHITECTURE.md §4.2
- [x] All foreign keys present and migration runs cleanly with `alembic upgrade head`

---

## Technical notes

---

## Out of scope

- Any files under repository root `tests/` (see paired QA ticket)
- Developer unit tests inside `backend/` or `frontend/`

---

## Definition of Done

- [x] Acceptance criteria met
- [x] `data-testid` hooks on new UI controls (if frontend)
- [x] OpenAPI updated (if API)
- [x] No test modules added outside `tests/`
- [x] Ticket ACs and DoD marked `[x]`, `Status: Done` added to metadata
- [x] `README.md` App implementation status updated for this ticket
- [x] Epic checklist ticked only if this was the last story in the epic
