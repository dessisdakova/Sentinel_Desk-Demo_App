# SENT-303 — Alert queue React page and table

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E03 Triage Queue UI |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-303-QA](./SENT-303-QA.md) |

---

## Summary

Alert queue React page and table.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Triage Queue UI

---

## Acceptance criteria

### AC1 —

- [ ] Route /alerts data-testid=page-alert-queue
### AC2 —

- [ ] Columns: title, severity, status, source, assignee, sla_due_at, created_at
### AC3 —

- [ ] Server-driven pagination 25/50/100

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

