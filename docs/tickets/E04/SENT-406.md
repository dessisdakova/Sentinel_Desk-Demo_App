# SENT-406 — Escalation UI on Summary tab

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E04 Alert Detail |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-406-QA](./SENT-406-QA.md) |

---

## Summary

Escalation UI on Summary tab.

---

## Description

**As a** SOC analyst or lead  
**I want** the Summary tab to show role-appropriate escalation action buttons  
**So that** analysts can request escalation without accessing lead-only actions, and leads can approve or reject without additional navigation

---

## Acceptance criteria

### AC1 — Escalate button for analysts

- [ ] When the alert status is `NEW`, `TRIAGING`, or `TRUE_POSITIVE` and the logged-in user is `ANALYST`, an "Escalate" button is visible with `data-testid="alert-escalate-btn"`
- [ ] Clicking it calls `PATCH /api/v1/alerts/{id}` with `{ "status": "ESCALATED" }` and refreshes the alert

### AC2 — Approve / Reject visible for Lead+ only

- [ ] When the alert status is `ESCALATED`, an `ANALYST` user sees no Approve or Reject buttons
- [ ] A `LEAD` or `ADMIN` user sees "Approve" (`data-testid="alert-approve-btn"`) and "Reject" (`data-testid="alert-reject-btn"`) buttons

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
