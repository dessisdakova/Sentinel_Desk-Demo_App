# SENT-602 — run_playbook Celery task

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E06 Playbooks and Async Execution |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-602-QA](./SENT-602-QA.md) |

---

## Summary

run_playbook Celery task.

---

## Description

**As a** SOC platform  
**I want** a Celery task that executes playbook steps sequentially with realistic delays and writes timeline events per step  
**So that** the async polling UI can show live progress and QA can practise handling flaky timing without `time.sleep`

---

## Acceptance criteria

### AC1 — Multi-step execution with delays

- [ ] `run_playbook` Celery task iterates over `playbook.steps_json` with a simulated 2–5s delay per step

### AC2 — Status transitions

- [ ] Task updates `playbook_runs.status`: `PENDING` (at creation) → `RUNNING` (when first step starts) → `SUCCESS` (all steps done) or `FAILED` (exception or deliberate failure step)
- [ ] Celery's internal `FAILURE` state is **never** written to `playbook_runs.status` — always map to `FAILED`

### AC3 — Per-step alert timeline events

- [ ] An `alert_events` row is written for each completed step containing the step name and result in `payload`

---

## Technical notes

- Updates `playbook_runs.status` using enum `PENDING`, `RUNNING`, `SUCCESS`, `FAILED` only (map from Celery internally)
- Store `celery_task_id` on row if useful for ops — not exposed as public poll API

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
