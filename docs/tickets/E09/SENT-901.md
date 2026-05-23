# SENT-901 — Admin users API and UI

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E09 Admin and Notifications |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-901-QA](./SENT-901-QA.md) |

---

## Summary

Admin users API and UI.

---

## Description

**As an** admin  
**I want** a Users tab in the admin panel with full CRUD and the ability to deactivate accounts  
**So that** I can on-board new analysts, change roles, and immediately revoke access for departed staff without touching the database directly

---

## Acceptance criteria

### AC1 — Admin users CRUD in UI and API

- [ ] `/admin` page has a "Users" tab (`data-testid="admin-tab-users"`) with a table of all users and controls to create, edit role, and deactivate
- [ ] Backing API: `GET /api/v1/admin/users`, `POST /api/v1/admin/users`, `PATCH /api/v1/admin/users/{id}` — all require `ADMIN` role

### AC2 — Deactivation prevents login

- [ ] Setting `active=false` via `PATCH /api/v1/admin/users/{id}` immediately causes the deactivated user's next login attempt to return `403` with code `ACCOUNT_DISABLED` (matches SENT-104 AC5)

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
- [ ] Ticket ACs and DoD marked `[x]`, `Status: Done` added to metadata
- [ ] `README.md` App implementation status updated for this ticket
- [ ] Epic checklist ticked only if this was the last story in the epic
