# SENT-205 — mock-siem container posting alerts

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E02 Alert Ingestion and Async Enrichment |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `infra`, `implementation` |
| **Paired QA ticket** | [SENT-205-QA](./SENT-205-QA.md) |

---

## Summary

mock-siem container posting alerts.

---

## Description

**As a** developer or QA engineer  
**I want** a mock SIEM container that continuously POSTs sample alert payloads to the ingest API on a configurable interval  
**So that** the alert queue fills automatically during local testing without manually calling the ingest endpoint

---

## Acceptance criteria

### AC1 — Continuous ingest posting

- [ ] The `mock-siem` service (port `8088`) POSTs to `POST /api/v1/alerts/ingest` at a configurable interval using the sample payload pattern from `docs/tickets/E02/sample-ingest-payload.json`

### AC2 — Configurable interval

- [ ] Posting interval is controlled by an environment variable (e.g. `MOCK_SIEM_INTERVAL_SECONDS`); defaults to 60s

### AC3 — Sample payload conformance

- [ ] Each POST uses a unique `external_id` (e.g. timestamped or UUID-based) so duplicate conflicts do not halt the loop

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
