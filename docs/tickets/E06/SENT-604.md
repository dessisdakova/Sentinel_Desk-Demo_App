# SENT-604 — Playbooks page and run modal with polling

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E06 Playbooks and Async Execution |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `frontend`, `async`, `implementation` |
| **Depends on** | SENT-603 |
| **Paired QA ticket** | [SENT-604-QA](./SENT-604-QA.md) |

---

## Summary

Run playbook from UI and show live status until Celery task completes.

---

## Description

**As an** analyst  
**I want to** see playbook progress  
**So that** I know when automated steps finish before closing the alert  

---

## Acceptance criteria

### AC1 — Start run

- **When** user clicks `data-testid="playbook-run-submit"` on alert `ALERT_FOR_PLAYBOOK`
- **Then** API `POST /api/v1/playbooks/{id}/run` returns `playbook_run_id` and `status: "PENDING"`
- **And** modal shows status `RUNNING` once poll reflects worker start

### AC2 — Polling

- **While** run not terminal
- **Then** UI polls every 2s `GET /api/v1/playbook-runs/{id}`
- **And** displays current step name from `steps_completed`

### AC3 — Success

- **When** worker finishes all steps
- **Then** modal shows `data-testid="playbook-run-status-success"`
- **And** alert timeline has new events

### AC4 — Failure

- **Given** playbook step configured to fail in seed (optional flag)
- **Then** modal shows error state with message

---

## Technical notes

- TanStack Query `refetchInterval` 2s while polling `GET /api/v1/playbook-runs/{playbook_run_id}` until `SUCCESS` or `FAILED`
- Disable double-submit while running
- Timeout UI after 60s with friendly error

---

## Out of scope

- Tests in `tests/` (SENT-604-QA)

---

## Definition of Done

- [ ] Route `/playbooks` and run modal from alert detail
- [ ] All playbook-run data-testids present
- [ ] No test files outside `tests/`
