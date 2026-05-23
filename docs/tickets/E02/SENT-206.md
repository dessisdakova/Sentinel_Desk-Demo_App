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

**As a** QA engineer  
**I want** the seed script to populate 12 baseline alerts with fixed UUIDs and known statuses  
**So that** integration and E2E tests can reference stable, predictable alert records by UUID constant instead of relying on dynamically created data

---

## Acceptance criteria

### AC1 — Seed creates 12 baseline alerts with stable UUIDs

- [ ] `seed.py` (extended from SENT-108) inserts 12 alerts using the exact UUIDs from [TEST_DATA.md §3](../../TEST_DATA.md)

### AC2 — Mixed statuses, severities, and sources

- [ ] The 12 alerts cover at least 3 different `AlertStatus` values and at least 2 different `severity` values and `source` values (ensures filters have data to work with in E03)

### AC3 — QA constants map correctly

- [ ] `ALERT_OPEN_HIGH` → UUID `11111111-1111-4111-8111-111111111101`, `external_id=seed-edr-001`
- [ ] `ALERT_ESCALATED` → UUID `11111111-1111-4111-8111-111111111102`, `external_id=seed-phish-002`
- [ ] `ALERT_FOR_PLAYBOOK` → UUID `11111111-1111-4111-8111-111111111103`, `external_id=seed-edr-playbook-003`

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
- [ ] Ticket ACs and DoD marked `[x]`, `Status: Done` added to metadata
- [ ] `README.md` App implementation status updated for this ticket
- [ ] Epic checklist ticked only if this was the last story in the epic
