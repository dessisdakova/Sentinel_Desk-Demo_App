# SENT-303 — Alert queue React page and table

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E03 Triage Queue UI |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-303-QA](./SENT-303-QA.md) |

---

## Summary

Alert queue React page and table.

---

## Description

**As a** SOC analyst  
**I want** a paginated data table at `/alerts` that shows all key alert fields at a glance  
**So that** I can quickly scan and navigate to the alerts that need my attention without loading each one individually

---

## Acceptance criteria

### AC1 — Page route and root testid

- [ ] Route `/alerts` renders with `data-testid="page-alert-queue"` on the root element

### AC2 — Table columns

- [ ] Table shows columns: `title`, `severity`, `status`, `source`, `assignee`, `sla_due_at`, `created_at`

### AC3 — Server-driven pagination

- [ ] Page size selector with options 25, 50, 100; navigating pages calls the API with updated `page` and `size` params

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
