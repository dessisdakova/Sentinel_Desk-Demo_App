# SENT-804 — Audit page and CSV export

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E08 Dashboard and Audit |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-804-QA](./SENT-804-QA.md) |

---

## Summary

Audit page and CSV export.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Dashboard and Audit

---

## Acceptance criteria

### AC1 —

- [ ] Route /audit with export button
### AC2 —

- [ ] CSV download for current filter

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

