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

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Outbound Webhooks

---

## Acceptance criteria

### AC1 —

- [ ] POST signed payload on alert status change
### AC2 —

- [ ] 3 retries exponential backoff on 5xx/timeout
### AC3 —

- [ ] webhook_deliveries log

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

