# SENT-603 — Playbook APIs and playbook-run status

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E06 Playbooks and Async Execution |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-603-QA](./SENT-603-QA.md) |

---

## Summary

Playbook list/run APIs and playbook-run status endpoint (single poll URL for async UI).

---

## Description

**As an** analyst  
**I want** REST endpoints to list playbooks, start a run, and poll run status  
**So that** the UI modal can show progress until completion  

---

## Acceptance criteria

### AC1 — List playbooks

- [ ] `GET /api/v1/playbooks` — analyst JWT; returns seeded playbooks

### AC2 — Start run

- [ ] `POST /api/v1/playbooks/{id}/run` with body `{ "alert_id": "<uuid>" }` (analyst JWT)
- [ ] Returns `201` or `202` with `{ "playbook_run_id", "status": "PENDING" }`
- [ ] Enqueues Celery `run_playbook`; stores optional `celery_task_id` on row (internal — not required in response)

### AC3 — Poll run status (canonical async endpoint)

- [ ] `GET /api/v1/playbook-runs/{id}` — analyst JWT
- [ ] Response includes `status` (`PENDING` \| `RUNNING` \| `SUCCESS` \| `FAILED`), `steps_completed`, `error_message` when failed
- [ ] OpenAPI documents PlaybookRun status enum — **not** Celery `FAILURE`

### AC4 — Negative

- [ ] Run on invalid alert or alert in **terminal** `AlertStatus` → `400` (`ALERT_TERMINAL`)

---

## Technical notes

- Follow [ARCHITECTURE.md](../../ARCHITECTURE.md) §5.2 — **no** `GET /api/v1/jobs/{task_id}` in this epic
- Map Celery task state → `playbook_runs.status` in worker (SENT-602)

---

## Out of scope

- Generic Celery job status route
- Any files under repository root `tests/` (see paired QA ticket)

---

## Definition of Done

- [ ] Acceptance criteria met
- [ ] OpenAPI updated
- [ ] No test modules added outside `tests/`
