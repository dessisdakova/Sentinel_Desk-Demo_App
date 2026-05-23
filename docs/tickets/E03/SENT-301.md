# SENT-301 — Alerts list API with filters and pagination

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E03 Triage Queue UI |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-301-QA](./SENT-301-QA.md) |

---

## Summary

Alerts list API with filters and pagination.

---

## Description

**As a** SOC analyst  
**I want** the alerts list endpoint to support rich filtering by severity, status, source, assignee, and date range  
**So that** I can focus the queue on only the alerts relevant to my current triage session without manually scanning every row

---

## Acceptance criteria

### AC1 — Filter and sort query params

- [ ] `GET /api/v1/alerts` supports query params: `page`, `size`, `severity`, `status`, `source`, `assigned_to` (user UUID), `from` (ISO date), `to` (ISO date), `sort` (e.g. `created_at_desc`)

### AC2 — Paginated response with total count

- [ ] Response shape: `{ "items": [...], "total": N, "page": N, "size": N }` — `total` must reflect the filtered count, not the unfiltered table size

### AC3 — Invalid enum values rejected

- [ ] Passing an unknown `severity` or `status` value returns `422 Unprocessable Entity`

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
