# SENT-804 — Audit page and CSV export

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E08 Dashboard and Audit |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-804-QA](./SENT-804-QA.md) |

---

## Summary

Audit page and CSV export.

---

## Description

**As a** SOC lead  
**I want** an audit log page with an export-to-CSV button that downloads the currently filtered rows  
**So that** I can share audit evidence with compliance teams or store it offline without requiring DB access

---

## Acceptance criteria

### AC1 — Audit log page route

- [ ] Route `/audit` renders with `data-testid="page-audit"` and displays the paginated audit log table (consumes the API from SENT-803)

### AC2 — CSV export for current filter

- [ ] An "Export CSV" button (`data-testid="audit-export-csv-btn"`) triggers a download of the audit rows matching the current filter (same `from`, `to`, `actor`, `entity_type` params)
- [ ] The export endpoint returns a CSV file (`Content-Type: text/csv`) — implement server-side CSV generation (do **not** silently truncate; see BUG-005 which will be planted in E10)

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
