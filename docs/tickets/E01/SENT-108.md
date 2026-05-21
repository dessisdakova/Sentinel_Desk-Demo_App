# SENT-108 — Seed script for users

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Story Points** | 3 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-108-QA](./SENT-108-QA.md) |

---

## Summary

Seed script for users.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Platform Foundation

---

## Acceptance criteria

### AC1 —

- [ ] scripts/seed.py creates 3 users per TEST_DATA.md
### AC2 —

- [ ] Idempotent: re-run does not duplicate emails
### AC3 —

- [ ] Document command in README

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

