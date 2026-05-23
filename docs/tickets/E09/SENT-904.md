# SENT-904 — Notification model and SMS mock toast

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E09 Admin and Notifications |
| **Priority** | High |
| **Story Points** | 3 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-904-QA](./SENT-904-QA.md) |

---

## Summary

Notification model and SMS mock toast.

---

## Description

**As a** SOC platform  
**I want** SMS notifications to be recorded as `notifications` rows and shown as a toast in the UI — without calling any real SMS provider  
**So that** QA can assert SMS notification behaviour from the DB and UI without incurring external API costs or requiring Twilio credentials

---

## Acceptance criteria

### AC1 — SMS channel creates notification row only

- [ ] When an SMS notification is triggered (e.g. for a high-severity escalation), a `notifications` row is created with `channel=SMS`, a fictional recipient number (`+1-555-***`), `subject`, and `status=SENT` — no external API call is made

### AC2 — UI toast confirms SMS simulation

- [ ] The UI displays a toast message `"SMS simulated to +1-555-***"` (`data-testid="sms-simulated-toast"`) after the notification row is written

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
