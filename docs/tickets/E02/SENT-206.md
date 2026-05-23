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

- [ ] `seed.py` adds 12 alerts with stable UUIDs per [TEST_DATA.md](../../TEST_DATA.md) §3 (extend `backend/scripts/seed.py` from SENT-108)
### AC2 —

- [ ] Mix of statuses, severities, sources
### AC3 —

- [ ] Primary rows use `external_id` values: `seed-edr-001`, `seed-phish-002`, `seed-edr-playbook-003` mapped to `ALERT_OPEN_HIGH`, `ALERT_ESCALATED`, `ALERT_FOR_PLAYBOOK`

---

## Technical notes

- UUID + `external_id` pairs must match TEST_DATA §3 exactly

## Out of scope

- Any files under repository root `tests/` (see paired QA ticket)
- Developer unit tests inside `backend/` or `frontend/`

---

## Definition of Done

- [ ] Acceptance criteria met
- [ ] `data-testid` hooks on new UI controls (if frontend)
- [ ] OpenAPI updated (if API)
- [ ] No test modules added outside `tests/`

