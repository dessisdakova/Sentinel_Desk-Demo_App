# SENT-402 — Escalation state machine and approval API

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E04 Alert Detail |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-402-QA](./SENT-402-QA.md) |

---

## Summary

Escalation state machine and approval API.

---

## Description

**As a** SOC analyst  
**I want** to escalate an alert to a lead for approval  
**So that** high-severity or ambiguous alerts get a second pair of eyes before being closed, with every state change recorded in the audit log

---

## Acceptance criteria

### AC1 — Analyst requests escalation

- [ ] `PATCH /api/v1/alerts/{id}` with `{ "status": "ESCALATED" }` (analyst JWT) transitions the alert to `ESCALATED`
- [ ] Only valid from non-terminal statuses (`NEW`, `TRIAGING`, `TRUE_POSITIVE`) — rejects terminal statuses with `INVALID_STATE`

### AC2 — Lead approves or rejects escalation

- [ ] `POST /api/v1/alerts/{id}/approve` (Lead+ JWT) transitions `ESCALATED → CLOSED`; `POST /api/v1/alerts/{id}/reject` returns the alert to `TRIAGING`
- [ ] An `ANALYST` calling either endpoint receives `403 Forbidden` (enforced by `require_roles(["LEAD", "ADMIN"])`)

### AC3 — Audit entries for each transition

- [ ] Each status transition writes an `audit_logs` row with `actor`, `action` (e.g. `ALERT_ESCALATED`, `ALERT_APPROVED`, `ALERT_REJECTED`), and the previous/new status in `diff`

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
