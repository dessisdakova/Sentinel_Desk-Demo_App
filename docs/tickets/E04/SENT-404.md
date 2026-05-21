# SENT-404 — IOC list component

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E04 Alert Detail |
| **Priority** | High |
| **Story Points** | 3 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-404-QA](./SENT-404-QA.md) |

---

## Summary

IOC list component.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Alert Detail

---

## Acceptance criteria

### AC1 —

- [ ] Render IOC types IP, DOMAIN, HASH, URL
### AC2 —

- [ ] Copy button data-testid=ioc-copy-{index}

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

