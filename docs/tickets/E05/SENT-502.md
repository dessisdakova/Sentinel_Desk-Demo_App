# SENT-502 — Case CRUD and link alerts API

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E05 Case Management |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-502-QA](./SENT-502-QA.md) |

---

## Summary

Case CRUD and link alerts API.

---

## Description

**As a** SOC analyst or lead  
**I want** REST endpoints to create, read, update, and delete cases, and to link or unlink alerts  
**So that** investigations can be opened, populated with related alerts, and formally closed by a lead — all through the API

---

## Acceptance criteria

### AC1 — Case CRUD endpoints

- [ ] `GET /api/v1/cases` (list, paginated), `POST /api/v1/cases` (create), `GET /api/v1/cases/{id}` (detail), `PATCH /api/v1/cases/{id}` (update status/priority/lead)

### AC2 — Link and unlink alerts

- [ ] `POST /api/v1/cases/{id}/alerts` with `{ "alert_id": "<uuid>" }` links the alert to the case and sets `alert.status = MERGED`
- [ ] Linking an alert that is already `MERGED` returns `400 INVALID_STATE` (CONSTITUTION §5.1 — one case per alert)
- [ ] `DELETE /api/v1/cases/{id}/alerts/{alert_id}` unlinks the alert (optional; if implemented, does **not** revert `MERGED` status)

### AC3 — Case closure is Lead+ only

- [ ] `PATCH /api/v1/cases/{id}` with `{ "status": "CLOSED" }` requires `LEAD` or `ADMIN` role; an `ANALYST` receives `403 Forbidden`

---

## Technical notes

- `cases.status` enum: `OPEN`, `IN_PROGRESS`, `CLOSED` per CONSTITUTION §5.2

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
