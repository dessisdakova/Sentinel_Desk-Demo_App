# SENT-306 — Queue auto-refresh polling

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E03 Triage Queue UI |
| **Priority** | High |
| **Story Points** | 3 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-306-QA](./SENT-306-QA.md) |

---

## Summary

Queue auto-refresh polling.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Triage Queue UI

---

## Acceptance criteria

### AC1 —

- [ ] Poll alerts list every 10s when page visible
### AC2 —

- [ ] Env VITE_QUEUE_POLL_MS override

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

