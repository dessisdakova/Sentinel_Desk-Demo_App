# SENT-103 — User model and Alembic initial migration

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-103-QA](./SENT-103-QA.md) |

---

## Summary

User model and Alembic initial migration.

---

## Description

**As an** authentication and RBAC system  
**I want** a `users` table with email, hashed password, role, and active flag  
**So that** login, role enforcement, and audit attribution have a stable, versioned schema from day one

---

## Acceptance criteria

### AC1 — User table schema

- [ ] `users` table columns: `id` (UUID PK), `email` (unique), `password_hash`, `role`, `display_name`, `active` (bool), `created_at`, `updated_at`

### AC2 — Alembic migration

- [ ] `alembic upgrade head` succeeds on an empty PostgreSQL database with no errors

### AC3 — Role enum

- [ ] `role` column uses a PostgreSQL enum: `ANALYST`, `LEAD`, `ADMIN` (matches CONSTITUTION §4)

---

## Technical notes

No auth routes yet — routes are added in SENT-104.

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
