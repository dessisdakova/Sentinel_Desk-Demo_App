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

**As a** developer  
**I want** a single `docker compose up` command to start the database, cache, and email capture services  
**So that** every team member and CI run has a reproducible local environment with no manual service installation

---

## Acceptance criteria

### AC1 — Infrastructure services

- [ ] `docker-compose.yml` starts `postgres:16`, `redis:7`, and `mailhog` services

### AC2 — Environment template

- [ ] `.env.example` documents all connection variables (DB URL, Redis URL, SMTP host/port)

### AC3 — README prerequisites

- [ ] README documents Docker Desktop as a prerequisite and includes `docker compose up / down` start/stop instructions

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
- [ ] Ticket ACs and DoD marked `[x]`, `Status: Done` added to metadata
- [ ] `README.md` App implementation status updated for this ticket
- [ ] Epic checklist ticked only if this was the last story in the epic
