# SENT-105 — RBAC dependency require_roles

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-105-QA](./SENT-105-QA.md) |

---

## Summary

RBAC dependency require_roles.

---

## Description

**As an** API  
**I want** a reusable FastAPI dependency that reads the `role` claim from the JWT and rejects callers with insufficient privileges  
**So that** every protected route can enforce role-based access with a single decorator instead of duplicating auth logic

---

## Acceptance criteria

### AC1 — Role enforcement dependency

- [ ] `require_roles([...])` FastAPI dependency returns `403` with error code `FORBIDDEN` if the caller's JWT role is not in the allowed list

### AC2 — Sample protected route

- [ ] `GET /api/v1/admin/ping` is gated with `require_roles(["ADMIN"])` and returns `200` for admin, `403` for analyst and lead

---

## Technical notes

- Wire to JWT `role` claim from `Authorization: Bearer` header (SENT-104) — not cookies

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
