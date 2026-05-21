# SENT-101 — Docker Compose for Postgres, Redis, MailHog

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `infra`, `implementation` |
| **Paired QA ticket** | [SENT-101-QA](./SENT-101-QA.md) |

---

## Summary

Docker Compose for Postgres, Redis, MailHog.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Platform Foundation

---

## Acceptance criteria

### AC1 —

- [ ] docker-compose.yml starts postgres:16, redis:7, mailhog
### AC2 —

- [ ] .env.example documents all connection vars
### AC3 —

- [ ] README: prerequisites Docker Desktop, how to start/stop

---

## Technical notes

No application code beyond compose and env template.

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

