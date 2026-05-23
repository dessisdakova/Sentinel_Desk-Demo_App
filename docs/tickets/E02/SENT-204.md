# SENT-204 — Alert GET by id and basic list API

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E02 Alert Ingestion and Async Enrichment |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-204-QA](./SENT-204-QA.md) |

---

## Summary

Alert GET by id and basic list API.

---

## Description

**As an** API consumer (SPA or test client)  
**I want** endpoints to fetch a single alert by UUID and list alerts with basic pagination  
**So that** the frontend and QA tests can read alert state — including enrichment fields — before the full filter UI is built in E03

---

## Acceptance criteria

### AC1 — Get alert by id with enrichment fields

- [ ] `GET /api/v1/alerts/{id}` returns the full alert object including `enrichment_status`, `sla_due_at`, and `ioc_list`
- [ ] Returns `404` for unknown ID

### AC2 — Basic paginated list

- [ ] `GET /api/v1/alerts` accepts `page` and `size` query params; returns `{ items, total, page, size }`
- [ ] No advanced filters required in this story (filters added in SENT-301)

### AC3 — Auth required

- [ ] Both endpoints require a valid analyst (or higher) JWT; returns `401` without token

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
