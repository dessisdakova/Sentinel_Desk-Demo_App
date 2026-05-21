# SENT-903 — send_email Celery task to MailHog

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E09 Admin and Notifications |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-903-QA](./SENT-903-QA.md) |

---

## Summary

send_email Celery task to MailHog.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Admin and Notifications

---

## Acceptance criteria

### AC1 —

- [ ] On escalation and assignment send SMTP to mailhog:1025
### AC2 —

- [ ] notification row created

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

