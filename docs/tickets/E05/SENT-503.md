# SENT-503 — Case list and detail UI

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E05 Case Management |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-503-QA](./SENT-503-QA.md) |

---

## Summary

Case list and detail UI.

---

## Description

**As a** SOC analyst  
**I want** a case list page and a tabbed case detail page  
**So that** I can navigate between open investigations, review linked alerts, and read or add notes from a single UI

---

## Acceptance criteria

### AC1 — Case list and detail routes with tabs

- [ ] Route `/cases` renders a paginated table of cases with `data-testid="page-case-list"`
- [ ] Route `/cases/:id` renders a detail view with `data-testid="page-case-detail"` and four tabs: **Overview** (`data-testid="tab-overview"`), **Alerts** (`tab-alerts`), **Notes** (`tab-notes`), **Activity** (`tab-activity`)

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
