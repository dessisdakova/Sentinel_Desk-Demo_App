# SENT-801 — metrics summary API and Redis cache

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E08 Dashboard and Audit |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-801-QA](./SENT-801-QA.md) |

---

## Summary

metrics summary API and Redis cache.

---

## Description

**As a** SOC lead  
**I want** a summary metrics endpoint that returns KPIs for a given date range, cached in Redis for 30 seconds  
**So that** the dashboard loads quickly under repeated page views without hammering the database on every request

---

## Acceptance criteria

### AC1 — Metrics summary endpoint

- [ ] `GET /api/v1/metrics/summary?from=<ISO>&to=<ISO>` returns a JSON object with at minimum: `open_alerts` (count), `mttt_minutes` (float), `pending_escalations` (count), `open_cases` (count)

### AC2 — Scoped to date range

- [ ] `from` and `to` parameters filter the underlying data to the specified UTC time window; missing params default to a sensible range (e.g. last 30 days)

### AC3 — Redis cache TTL 30s

- [ ] Response is cached in Redis with a 30-second TTL keyed by the date-range params; a second identical request within 30s hits the cache, not the DB (verifiable via Redis CLI or integration test)

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
