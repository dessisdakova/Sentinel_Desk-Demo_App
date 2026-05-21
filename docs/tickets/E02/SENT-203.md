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

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Alert Ingestion and Async Enrichment

---

## Acceptance criteria

### AC1 —

- [ ] Celery worker service in docker-compose
### AC2 —

- [ ] enrich_alert sets enrichment_status PENDING then COMPLETE
### AC3 —

- [ ] Sets sla_due_at based on severity
### AC4 —

- [ ] Creates alert_event ENRICHMENT_COMPLETE

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

