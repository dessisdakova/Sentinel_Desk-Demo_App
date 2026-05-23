# SENT-502 — Case CRUD and link alerts API

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E05 Case Management |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-502-QA](./SENT-502-QA.md) |

---

## Summary

Case CRUD and link alerts API.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Case Management

---

## Acceptance criteria

### AC1 —

- [ ] CRUD /api/v1/cases
### AC2 —

- [ ] POST /api/v1/cases/{id}/alerts link and unlink
### AC3 —

- [ ] Only **LEAD+** may set **case** `CaseStatus` to `CLOSED` (not alert disposition — see CONSTITUTION §5.2)

---

## Technical notes

- `cases.status` enum: `OPEN`, `IN_PROGRESS`, `CLOSED` per CONSTITUTION §5.2

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

