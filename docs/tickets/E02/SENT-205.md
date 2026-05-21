# SENT-205 — mock-siem container posting alerts

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E02 Alert Ingestion and Async Enrichment |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `infra`, `implementation` |
| **Paired QA ticket** | [SENT-205-QA](./SENT-205-QA.md) |

---

## Summary

mock-siem container posting alerts.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Alert Ingestion and Async Enrichment

---

## Acceptance criteria

### AC1 —

- [ ] mock-siem service POSTs ingest on interval
### AC2 —

- [ ] Configurable interval via env
### AC3 —

- [ ] Uses sample ingest payload pattern

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

