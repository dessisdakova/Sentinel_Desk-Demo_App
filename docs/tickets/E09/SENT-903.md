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

**As a** SOC platform  
**I want** a Celery task that sends notification emails via MailHog SMTP when an alert is escalated or assigned  
**So that** QA can verify email delivery by inspecting MailHog at http://localhost:8025 without needing a real mail server

---

## Acceptance criteria

### AC1 — Email sent on escalation and assignment

- [ ] When an alert transitions to `ESCALATED`, a `send_email` Celery task is enqueued that sends an SMTP message to `mailhog:1025` addressed to the lead or assigned user (`@demo.local` addresses only)
- [ ] When an alert is assigned (`PATCH /api/v1/alerts/{id}` with `assigned_to`), a notification email is sent to the newly assigned analyst

### AC2 — Notification row created

- [ ] Each email send attempt creates a `notifications` row with `channel=EMAIL`, `recipient`, `subject`, and `status` (`SENT` or `FAILED`)

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
