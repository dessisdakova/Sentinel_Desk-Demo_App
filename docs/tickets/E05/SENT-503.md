# SENT-503 — Case list and detail UI

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E05 Case Management |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-503-QA](./SENT-503-QA.md) |

---

## Summary

Case list and detail UI.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Case Management

---

## Acceptance criteria

### AC1 —

- [ ] Routes /cases and /cases/:id with tabs Overview, Alerts, Notes, Activity

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

