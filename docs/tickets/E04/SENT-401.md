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

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Alert Detail

---

## Acceptance criteria

### AC1 —

- [ ] GET /api/v1/alerts/{id} full detail with iocs
### AC2 —

- [ ] GET /api/v1/alerts/{id}/events ordered chronologically

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

