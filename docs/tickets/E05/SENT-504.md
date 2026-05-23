# SENT-504 — Notes API and modal

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E05 Case Management |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-504-QA](./SENT-504-QA.md) |

---

## Summary

Notes API and modal.

---

## Description

**As a** SOC analyst  
**I want** to add free-text notes to a case and see all previous notes in chronological order  
**So that** investigators can document findings, hypotheses, and handoff context directly in the case record

---

## Acceptance criteria

### AC1 — Notes API

- [ ] `POST /api/v1/cases/{id}/notes` with `{ "body": "..." }` (analyst JWT) creates a `case_notes` row and returns `201` with the created note
- [ ] `GET /api/v1/cases/{id}` (or a dedicated `/notes` sub-resource) returns notes ordered by `created_at ASC`

### AC2 — Notes list on case detail UI

- [ ] The **Notes** tab on the case detail page lists existing notes and includes an "Add note" button (`data-testid="case-add-note-btn"`) that opens a modal with a text area and submit button

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
