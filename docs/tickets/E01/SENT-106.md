# SENT-106 — React app shell, router, auth context

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-106-QA](./SENT-106-QA.md) |

---

## Summary

React app shell, router, auth context.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Platform Foundation

---

## Acceptance criteria

### AC1 —

- [ ] Vite + React + TypeScript scaffold in frontend/
### AC2 —

- [ ] Routes: /login, protected layout with outlet
### AC3 —

- [ ] AuthContext stores JWT in memory and `sessionStorage` key `sentinel_access_token`
- [ ] API client attaches `Authorization: Bearer <token>`; clears storage on logout
- [ ] Redirects unauthenticated users to `/login`
### AC4 —

- [ ] Role-based nav placeholders (Dashboard, Alerts disabled until later)

---

## Technical notes

- Follow [ARCHITECTURE.md](../../ARCHITECTURE.md) §3 auth contract — JWT Bearer + sessionStorage only
- No alert pages yet.

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

