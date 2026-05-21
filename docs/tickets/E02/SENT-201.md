# SENT-201 — Alert and AlertEvent models and migration

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E02 Alert Ingestion and Async Enrichment |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-201-QA](./SENT-201-QA.md) |

---

## Summary

Alert and AlertEvent models and migration.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Alert Ingestion and Async Enrichment

---

## Acceptance criteria

### AC1 —

- [ ] alerts table per CONSTITUTION enums severity, source, status
### AC2 —

- [ ] alert_events table for timeline
### AC3 —

- [ ] Foreign keys and indexes on status, created_at

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

