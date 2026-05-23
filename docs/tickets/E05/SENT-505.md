# SENT-505 — Add to case from alert detail

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E05 Case Management |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-505-QA](./SENT-505-QA.md) |

---

## Summary

Add to case from alert detail.

---

## Description

**As a** SOC analyst  
**I want** to link an alert to a case directly from the alert detail page  
**So that** I can group related alerts into investigations without leaving the alert I am currently triaging

---

## Acceptance criteria

### AC1 — Add-to-case modal

- [ ] Alert detail Summary tab has an "Add to case" button (`data-testid="add-to-case-btn"`) that opens a modal offering two options:
  - **Create new case** — opens a form with title/priority fields
  - **Add to existing case** — shows a searchable dropdown of open cases
- [ ] Confirming either option calls `POST /api/v1/cases/{id}/alerts` and refreshes the alert status to `MERGED`

### AC2 — Testids on modal controls

- [ ] Modal root: `data-testid="add-to-case-modal"`
- [ ] New case option: `data-testid="add-to-case-new"`, existing case option: `data-testid="add-to-case-existing"`
- [ ] Confirm button: `data-testid="add-to-case-confirm"`

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
