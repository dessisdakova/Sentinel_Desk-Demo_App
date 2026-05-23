# SENT-803 — Audit log API and pagination

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E08 Dashboard and Audit |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-803-QA](./SENT-803-QA.md) |

---

## Summary

Audit log API and pagination.

---

## Description

**As a** SOC lead  
**I want** a paginated, filterable audit log endpoint restricted to Lead+ roles  
**So that** I can trace every action taken on alerts and cases for compliance reviews and incident post-mortems

---

## Acceptance criteria

### AC1 — Audit log endpoint with role gate

- [ ] `GET /api/v1/audit` requires `LEAD` or `ADMIN` role; an `ANALYST` receives `403 Forbidden`
- [ ] Returns a paginated response: `{ "items": [...], "total": N, "page": N, "size": N }`

### AC2 — Filter parameters

- [ ] Supports query params: `from` (ISO date), `to` (ISO date), `actor` (user UUID), `entity_type` (e.g. `alert`, `case`)

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
