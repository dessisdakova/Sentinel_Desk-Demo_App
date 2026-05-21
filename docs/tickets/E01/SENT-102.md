# SENT-102 — FastAPI project structure and health endpoint

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Story Points** | 3 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-102-QA](./SENT-102-QA.md) |

---

## Summary

FastAPI project structure and health endpoint.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Platform Foundation

---

## Acceptance criteria

### AC1 —

- [ ] GET /health returns 200 { status: ok }
### AC2 —

- [ ] App starts in docker api service on port 8000
### AC3 —

- [ ] Structured logging with request_id middleware

---

## Technical notes

Skeleton only: main.py, core/config, api router stub.

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

