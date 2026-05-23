# SENT-403 — Alert detail React tabs

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E04 Alert Detail |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-403-QA](./SENT-403-QA.md) |

---

## Summary

Alert detail React tabs.

---

## Description

**As a** SOC analyst  
**I want** the alert detail page to organise information into named tabs — Summary, Timeline, IOCs, Related, and Threat Intel  
**So that** I can navigate directly to the information I need without scrolling through a single long page

---

## Acceptance criteria

### AC1 — Multi-tab layout with testids

- [ ] Route `/alerts/:id` renders with `data-testid="page-alert-detail"` on the root element
- [ ] Five tabs present: **Summary**, **Timeline**, **IOCs**, **Related**, **Threat Intel** — each with `data-testid="tab-summary"`, `tab-timeline"`, `tab-iocs"`, `tab-related"`, `tab-threat-intel"`

### AC2 — Tab content panels

- [ ] Clicking each tab shows its corresponding panel; inactive tab panels are hidden (not removed from DOM if using Headless UI / Radix)

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
