# SENT-403 — Alert detail React tabs

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E04 Alert Detail |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-403-QA](./SENT-403-QA.md) |

---

## Summary

Alert detail React tabs.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Alert Detail

---

## Acceptance criteria

### AC1 —

- [ ] Route /alerts/:id tabs Summary, Timeline, IOCs, Related, Threat Intel
### AC2 —

- [ ] data-testid=page-alert-detail and tab-*

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

