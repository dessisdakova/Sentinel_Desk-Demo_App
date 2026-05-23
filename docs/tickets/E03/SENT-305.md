# SENT-305 — Bulk assign modal

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E03 Triage Queue UI |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-305-QA](./SENT-305-QA.md) |

---

## Summary

Bulk assign modal.

---

## Description

**As a** SOC lead  
**I want** to select multiple alerts in the queue and assign them all to an analyst in one action  
**So that** I can distribute incoming workloads quickly without opening each alert individually

---

## Acceptance criteria

### AC1 — Row selection checkboxes

- [ ] Each table row has a checkbox (`data-testid="alert-row-checkbox-{id}"`); a "select all on page" header checkbox is also present

### AC2 — Bulk assign modal

- [ ] Selecting one or more rows reveals a "Bulk assign" action that opens a modal (`data-testid="bulk-assign-modal"`) with an analyst dropdown (`data-testid="bulk-assign-analyst-select"`) and a confirm button (`data-testid="bulk-assign-confirm"`)

### AC3 — Success and error feedback

- [ ] On success, a toast confirms the number of alerts assigned; on partial failure, the toast reports how many succeeded and how many failed

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
