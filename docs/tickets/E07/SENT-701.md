# SENT-701 — Webhook subscription model and admin API

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E07 Outbound Webhooks |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-701-QA](./SENT-701-QA.md) |

---

## Summary

Webhook subscription model and admin API.

---

## Description

**As an** admin  
**I want** CRUD endpoints to manage outbound webhook subscriptions  
**So that** I can register external systems to receive signed event notifications when alert statuses change

---

## Acceptance criteria

### AC1 — Admin-only CRUD for webhook subscriptions

- [ ] `GET`, `POST`, `PATCH`, `DELETE /api/v1/admin/webhooks` — requires `ADMIN` role; non-admins receive `403`

### AC2 — Subscription fields validated

- [ ] Subscription record includes: `url` (valid HTTPS URL), `events` (list of event types, e.g. `["ALERT_STATUS_CHANGED"]`), `secret` (used to sign payloads), `active` (bool)
- [ ] Invalid URL or empty `events` array returns `422`

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
