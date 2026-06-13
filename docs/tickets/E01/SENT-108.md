# SENT-108 — Seed script for users

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Story Points** | 3 |
| **Status** | Done |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-108-QA](./SENT-108-QA.md) ✅ Done |

---

## Summary

Seed script for users.

---

## Description

**As a** developer and QA engineer  
**I want** a repeatable seed script that creates the four baseline users with known credentials and fixed UUIDs  
**So that** integration tests and manual exploration always start from a known auth state without manual DB setup

---

## Acceptance criteria

### AC1 — Seed creates baseline users

- [x] `backend/scripts/seed.py` inserts the 4 users from [TEST_DATA.md §2](../../TEST_DATA.md) (`analyst@demo.local`, `lead@demo.local`, `admin@demo.local`, `inactive@demo.local`) with passwords hashed via bcrypt, roles from CONSTITUTION §4, and `inactive@demo.local` seeded with `active = False`

### AC2 — Idempotent

- [x] Re-running `python -m scripts.seed` does not duplicate users (upsert or skip-on-conflict by email)

### AC3 — Run command documented

- [x] README documents `docker compose exec api python -m scripts.seed` (and the local equivalent `cd backend && python -m scripts.seed`)

---

## Technical notes

- Add `backend/scripts/__init__.py` so `python -m scripts.seed` works from api container (`WORKDIR /app` = `backend/`)
- Update `backend/Dockerfile` to `COPY scripts ./scripts` when this ticket lands
- Document run command in README (see TEST_DATA.md §3.1)

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
