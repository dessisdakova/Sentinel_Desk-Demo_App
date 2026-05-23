# SENT-203 — Celery worker and enrich_alert task

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E02 Alert Ingestion and Async Enrichment |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-203-QA](./SENT-203-QA.md) |

---

## Summary

Celery worker and enrich_alert task.

---

## Description

**As a** SOC platform  
**I want** a Celery worker that asynchronously enriches newly ingested alerts with SLA deadlines and tags  
**So that** analysts see complete, prioritised data without waiting for synchronous processing to block the ingest API response

---

## Acceptance criteria

### AC1 — Worker service in Docker Compose

- [ ] A `worker` service running Celery is added to `docker-compose.yml` alongside the existing `api` service

### AC2 — Enrichment status transitions

- [ ] `enrich_alert` task sets `enrichment_status=PENDING` immediately on enqueue, then updates to `COMPLETE` after finishing — observable by polling `GET /api/v1/alerts/{id}`

### AC3 — SLA calculation

- [ ] `sla_due_at` is set based on alert `severity` (e.g. CRITICAL: +1h, HIGH: +4h, MEDIUM: +24h, LOW: +72h from `created_at`)

### AC4 — Timeline event

- [ ] Creates an `alert_events` row with `event_type=ENRICHMENT_COMPLETE` when the task finishes

---

## Technical notes

---

## Out of scope

- Any files under repository root `tests/` (see paired QA ticket)
- Developer unit tests inside `backend/` or `frontend/`

---

## Definition of Done

- [ ] Acceptance criteria met
- [ ] `data-testid` hooks on new UI controls (if frontend)
- [ ] OpenAPI updated (if API)
- [ ] No test modules added outside `tests/`
- [ ] Ticket ACs and DoD marked `[x]`, `Status: Done` added to metadata
- [ ] `README.md` App implementation status updated for this ticket
- [ ] Epic checklist ticked only if this was the last story in the epic
