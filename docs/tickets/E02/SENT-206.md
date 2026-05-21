# SENT-206 — Seed alerts per TEST_DATA.md

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E02 Alert Ingestion and Async Enrichment |
| **Priority** | High |
| **Story Points** | 3 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-206-QA](./SENT-206-QA.md) |

---

## Summary

Seed alerts per TEST_DATA.md.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Alert Ingestion and Async Enrichment

---

## Acceptance criteria

### AC1 —

- [ ] seed.py adds 12 alerts with stable UUIDs
### AC2 —

- [ ] Mix of statuses, severities, sources
### AC3 —

- [ ] Includes external_ids seed-edr-001, seed-phish-002

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

