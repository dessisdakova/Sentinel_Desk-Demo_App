# SENT-306 — Queue auto-refresh polling

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E03 Triage Queue UI |
| **Priority** | High |
| **Story Points** | 3 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-306-QA](./SENT-306-QA.md) |

---

## Summary

Queue auto-refresh polling.

---

## Description

**As a** SOC analyst  
**I want** the alert queue to refresh automatically while I have the page open  
**So that** newly ingested alerts from the mock SIEM appear in my queue without me manually reloading the page

---

## Acceptance criteria

### AC1 — Auto-refresh when page is visible

- [ ] The alert list re-fetches from the API every 10 seconds while the browser tab is in the foreground (use TanStack Query `refetchInterval`)

### AC2 — Configurable interval via environment variable

- [ ] Polling interval is overridable via `VITE_QUEUE_POLL_MS` environment variable (useful for speeding up E2E tests)

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
