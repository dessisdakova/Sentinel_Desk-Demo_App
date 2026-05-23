# SENT-902 — Detection rules model and apply on enrich

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E09 Admin and Notifications |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-902-QA](./SENT-902-QA.md) |

---

## Summary

Detection rules model and apply on enrich.

---

## Description

**As an** admin  
**I want** configurable detection rules that automatically tag alerts during enrichment based on severity and source  
**So that** analysts see pre-computed tags on newly ingested alerts without manual classification

---

## Acceptance criteria

### AC1 — Detection rules schema and admin API

- [ ] `detection_rules` table: `id` (UUID PK), `severity` (nullable enum filter), `source` (nullable enum filter), `tag` (string to apply), `active` (bool)
- [ ] Admin API (e.g. `GET/POST/PATCH /api/v1/admin/rules`) — `ADMIN` role only

### AC2 — Rules applied during enrichment

- [ ] `enrich_alert` Celery task (SENT-203) evaluates all active rules against the alert's `severity` and `source`; matching rules append their `tag` to the alert's `ioc_list` or a dedicated `tags` field

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
- [ ] Ticket ACs and DoD marked `[x]`, `Status: Done` added to metadata
- [ ] `README.md` App implementation status updated for this ticket
- [ ] Epic checklist ticked only if this was the last story in the epic
