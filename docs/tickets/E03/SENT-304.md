# SENT-304 — Filter bar and date pickers

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E03 Triage Queue UI |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-304-QA](./SENT-304-QA.md) |

---

## Summary

Filter bar and date pickers.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Triage Queue UI

---

## Acceptance criteria

### AC1 —

- [ ] Filters: severity, status, source, assignee, date range
### AC2 —

- [ ] data-testid on each filter control
### AC3 —

- [ ] Apply resets page to 1

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

