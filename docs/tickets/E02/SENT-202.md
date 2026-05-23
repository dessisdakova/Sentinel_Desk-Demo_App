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

**As a** mock SIEM integration  
**I want** to POST structured alert payloads to a single ingest endpoint authenticated with an API key  
**So that** external systems can push alerts into SentinelDesk without user JWT credentials

---

## Acceptance criteria

### AC1 — Successful ingest

- [ ] `POST /api/v1/alerts/ingest` with `X-API-Key: dev-ingest-key-change-in-prod` and valid payload returns `202 Accepted`

### AC2 — Alert created in correct initial state

- [ ] Alert is created with `status=NEW` and `enrichment_status=PENDING` in the database

### AC3 — Duplicate external_id rejected

- [ ] Re-posting with the same `external_id` returns `409 Conflict`

### AC4 — Invalid payload rejected

- [ ] Missing required fields return `422` with error body matching CONSTITUTION §12.2 shape `{ "error": { "code", "message", "details" } }`

### AC5 — Audit log entry

- [ ] `audit_logs` row with `action=ALERT_INGESTED` is written for every successful ingest

---

## Technical notes

Payload schema: `docs/tickets/E02/sample-ingest-payload.json`

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
