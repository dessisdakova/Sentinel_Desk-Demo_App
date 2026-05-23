# SENT-702 — deliver_webhook Celery task with retries

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E07 Outbound Webhooks |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-702-QA](./SENT-702-QA.md) |

---

## Summary

deliver_webhook Celery task with retries.

---

## Description

**As a** SOC platform  
**I want** outbound webhook deliveries to be queued as Celery tasks with automatic retry on failure  
**So that** transient errors from the receiving system do not silently drop notifications, and QA can assert retry behaviour from the `webhook_deliveries` log

---

## Acceptance criteria

### AC1 — Signed payload on alert status change

- [ ] When an alert status changes, `deliver_webhook` is enqueued for each active subscription whose `events` list matches the event type
- [ ] Payload is signed with `X-Sentinel-Signature: sha256=<hmac>` using the subscription's `secret`

### AC2 — Retry policy

- [ ] On `5xx` response or connection timeout, the task retries up to 3 times with exponential backoff (e.g. 5s, 25s, 125s)

### AC3 — Delivery log

- [ ] Each attempt (success or failure) writes a `webhook_deliveries` row with `status`, `response_code`, `retry_count`, and `attempted_at`

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
