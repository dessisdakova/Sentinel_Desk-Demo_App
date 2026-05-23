# Epic E06 — Playbooks & Async Execution

**Epic key:** `SENT-E06`  
**Summary:** Run predefined response playbooks via background jobs with UI polling.  
**Business value:** Consistent, repeatable response actions.

---

## Acceptance criteria

- [ ] Playbook definitions in DB (seed: Isolate host, Notify owner, Escalate)
- [ ] Page `/playbooks` lists playbooks with trigger severity
- [ ] From alert detail or playbooks page: Run playbook modal
- [ ] `POST /api/v1/playbooks/{id}/run` enqueues Celery task; returns `playbook_run_id` + initial `status: PENDING`
- [ ] UI polls **`GET /api/v1/playbook-runs/{id}` only** (every 2s) until `SUCCESS` or `FAILED`
- [ ] Playbook run creates `alert_events` for each step
- [ ] Failed step sets run status `FAILED` with error message

---

## Stories

| Story key | Title |
|-----------|-------|
| SENT-601 | Playbook + PlaybookRun models |
| SENT-602 | run_playbook Celery task (multi-step, delays) |
| SENT-603 | Playbook APIs + playbook-run status endpoint |
| SENT-604 | Playbooks page + run modal + polling UI |

---

## QA notes

- E2E: explicit wait for success — practice flakiness (BUG-003)
- Integration: `playbook_runs.status` transitions `PENDING` → `RUNNING` → `SUCCESS`
- API: cannot run playbook on CLOSED alert → 400
- Poll **`/api/v1/playbook-runs/{id}`** — not a generic jobs URL
