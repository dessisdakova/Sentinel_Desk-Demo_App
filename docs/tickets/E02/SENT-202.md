# SENT-202 — Ingest API with API key auth

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E02 Alert Ingestion and Async Enrichment |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-202-QA](./SENT-202-QA.md) |

---

## Summary

Ingest API with API key auth.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Alert Ingestion and Async Enrichment

---

## Acceptance criteria

### AC1 —

- [ ] POST /api/v1/alerts/ingest with X-API-Key returns 202
### AC2 —

- [ ] Valid payload creates alert status NEW
### AC3 —

- [ ] Duplicate external_id returns 409
### AC4 —

- [ ] Invalid payload returns 422 with error shape
### AC5 —

- [ ] Audit log ALERT_INGESTED

---

## Technical notes

Payload schema: docs/tickets/E02/sample-ingest-payload.json

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

