# SENT-504 — Notes API and modal

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E05 Case Management |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-504-QA](./SENT-504-QA.md) |

---

## Summary

Notes API and modal.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Case Management

---

## Acceptance criteria

### AC1 —

- [ ] POST /api/v1/cases/{id}/notes
### AC2 —

- [ ] Notes list on case detail

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

