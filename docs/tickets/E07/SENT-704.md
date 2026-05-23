# SENT-704 — Admin UI webhook delivery log

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E07 Outbound Webhooks |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-704-QA](./SENT-704-QA.md) |

---

## Summary

Admin UI webhook delivery log.

---

## Description

**As an** admin  
**I want** a table in the Admin panel that shows every webhook delivery attempt with its status and HTTP response code  
**So that** I can diagnose delivery failures and confirm that retries are working without querying the database directly

---

## Acceptance criteria

### AC1 — Delivery log table in Admin UI

- [ ] The Admin page (`/admin`) has a "Webhooks" tab or section that shows a paginated table of `webhook_deliveries` rows with columns: subscription URL, event type, `status`, `response_code`, `retry_count`, `attempted_at`
- [ ] Table root: `data-testid="webhook-delivery-table"`; each row: `data-testid="webhook-delivery-row-{id}"`

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
