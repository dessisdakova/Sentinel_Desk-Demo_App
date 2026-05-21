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

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Outbound Webhooks

---

## Acceptance criteria

### AC1 —

- [ ] CRUD /api/v1/admin/webhooks admin only
### AC2 —

- [ ] Fields: url, events, secret, active

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

