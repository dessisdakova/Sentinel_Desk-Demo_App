# SENT-107 — Login page with data-testid

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Story Points** | 3 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-107-QA](./SENT-107-QA.md) |

---

## Summary

Login page with data-testid.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Platform Foundation

---

## Acceptance criteria

### AC1 —

- [ ] page-login root data-testid=page-login
### AC2 —

- [ ] Fields: login-email, login-password, login-submit
### AC3 —

- [ ] Shows API error toast on 401
### AC4 —

- [ ] Successful login redirects to /dashboard

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

