# SENT-103 — User model and Alembic initial migration

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Status** | Done |
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

- [x] `users` table columns: `id` (UUID PK), `email` (unique), `password_hash`, `role`, `display_name`, `active` (bool), `created_at`, `updated_at`

### AC2 — Alembic migration

- [x] `alembic upgrade head` succeeds on an empty PostgreSQL database with no errors

### AC3 — Role enum

- [x] `role` column uses a PostgreSQL enum: `ANALYST`, `LEAD`, `ADMIN` (matches CONSTITUTION §4)

---

## Technical notes

No auth routes yet — routes are added in SENT-104.

---

## Artifacts

| Path | Purpose |
|------|---------|
| `backend/app/models/user.py` | `User` ORM model, `UserRole` enum |
| `backend/app/models/base.py` | SQLAlchemy `Base` |
| `backend/app/core/database.py` | Async engine + session factory |
| `backend/alembic/` | Migration environment |
| `backend/alembic/versions/20260523_0001_initial_users_table.py` | Initial migration |

---

## Out of scope

- Any files under repository root `tests/` (see paired QA ticket)
- Developer unit tests inside `backend/` or `frontend/`

---

## Definition of Done

- [x] Acceptance criteria met
- [x] `data-testid` hooks on new UI controls (if frontend)
- [x] OpenAPI updated (if API)
- [x] No test modules added outside `tests/`
- [x] Ticket ACs and DoD marked `[x]`, `Status: Done` added to metadata
- [x] `README.md` App implementation status updated for this ticket
- [x] Epic checklist ticked only if this was the last story in the epic
