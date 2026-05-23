# SENT-601 — Playbook and PlaybookRun models

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E06 Playbooks and Async Execution |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-601-QA](./SENT-601-QA.md) |

---

## Summary

Playbook and PlaybookRun models.

---

## Description

**As a** SOC platform  
**I want** `playbooks` and `playbook_runs` tables seeded with the three baseline playbooks  
**So that** the async execution and polling features in later stories have a stable schema and known data to work with

---

## Acceptance criteria

### AC1 — Playbook and PlaybookRun tables

- [ ] `playbooks` table: `id` (UUID PK), `name`, `trigger_severity`, `steps_json` (JSONB array of step definitions), `created_at`
- [ ] `playbook_runs` table: `id` (UUID PK), `playbook_id` (FK), `alert_id` (FK), `status` (`PlaybookRunStatus` enum), `steps_completed` (int), `error_message` (nullable), `celery_task_id` (nullable string), `created_at`, `updated_at`
- [ ] Migration runs cleanly with `alembic upgrade head`

### AC2 — Seed three baseline playbooks and correct status enum

- [ ] `seed.py` inserts the three playbooks from [TEST_DATA.md §3](../../TEST_DATA.md): `PLAYBOOK_ISOLATE` (UUID `33333333-3333-4333-8333-333333333301`), plus "Notify owner" and "Escalate to lead"
- [ ] `playbook_runs.status` enum: `PENDING`, `RUNNING`, `SUCCESS`, `FAILED` — **separate from `AlertStatus` and `CaseStatus`** (CONSTITUTION §5.2); Celery `FAILURE` must be mapped to `FAILED` internally

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
