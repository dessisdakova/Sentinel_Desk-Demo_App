# SENT-803 — Audit log API and pagination

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E08 Dashboard and Audit |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-803-QA](./SENT-803-QA.md) |

---

## Summary

Audit log API and pagination.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Dashboard and Audit

---

## Acceptance criteria

### AC1 —

- [ ] GET /api/v1/audit LEAD+ only
### AC2 —

- [ ] Filters: from, to, actor, entity_type

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

