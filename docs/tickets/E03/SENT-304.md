# SENT-304 — Filter bar and date pickers

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E03 Triage Queue UI |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-304-QA](./SENT-304-QA.md) |

---

## Summary

Filter bar and date pickers.

---

## Description

**As a** SOC analyst  
**I want** a filter bar above the alert queue table with dropdowns for severity, status, source, assignee, and a date range picker  
**So that** I can narrow the queue to a specific time window or alert category without writing API queries manually

---

## Acceptance criteria

### AC1 — Filter controls

- [ ] Filter bar includes: `severity` dropdown, `status` dropdown, `source` dropdown, `assignee` dropdown (lists analyst users), date range (from / to) using `react-day-picker`

### AC2 — Testids on all filter controls

- [ ] Each filter control has a `data-testid` following the naming convention `alert-queue-filter-<name>` (e.g. `alert-queue-filter-severity`)

### AC3 — Apply resets pagination

- [ ] Applying or clearing any filter resets the current page to 1

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
