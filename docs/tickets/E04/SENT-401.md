# SENT-401 — Alert detail API and events endpoint

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E04 Alert Detail |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-401-QA](./SENT-401-QA.md) |

---

## Summary

Alert detail API and events endpoint.

---

## Description

**As a** SOC analyst  
**I want** an API endpoint that returns the full alert detail including IOCs, and a separate endpoint for the chronological event timeline  
**So that** the alert detail page can render all tabs — Summary, IOCs, and Timeline — from stable, well-typed API responses

---

## Acceptance criteria

### AC1 — Full alert detail including IOCs

- [ ] `GET /api/v1/alerts/{id}` returns the complete alert object with `ioc_list` (JSONB array of `{type, value}` objects) and all enrichment fields

### AC2 — Alert events timeline

- [ ] `GET /api/v1/alerts/{id}/events` returns `alert_events` rows for the alert, ordered by `created_at ASC`

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
