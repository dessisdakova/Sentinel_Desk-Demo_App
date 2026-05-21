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

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Platform Foundation

---

## Acceptance criteria

### AC1 —

- [ ] users table: id, email, password_hash, role, display_name, active, timestamps
### AC2 —

- [ ] alembic upgrade head succeeds on empty DB
### AC3 —

- [ ] Role enum: ANALYST, LEAD, ADMIN

---

## Technical notes

No auth routes yet.

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

