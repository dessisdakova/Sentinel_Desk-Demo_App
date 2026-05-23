# SENT-802 — Dashboard React and date picker

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E08 Dashboard and Audit |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-802-QA](./SENT-802-QA.md) |

---

## Summary

Dashboard React and date picker.

---

## Description

**As a** SOC lead  
**I want** a dashboard page with KPI cards and a date range picker  
**So that** I can quickly assess the current state of the queue and tune the time window to compare performance across different shifts or days

---

## Acceptance criteria

### AC1 — Dashboard route with KPI cards

- [ ] Route `/dashboard` renders with `data-testid="page-dashboard"`
- [ ] KPI cards for each metric returned by `GET /api/v1/metrics/summary`: open alerts, MTTT, pending escalations, open cases — each with a `data-testid="kpi-<name>"` attribute

### AC2 — Date range picker affects metrics

- [ ] A date range picker (`data-testid="dashboard-date-range"`) lets the user select from/to dates; changing the range re-fetches `GET /api/v1/metrics/summary` with updated params and re-renders the cards

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
