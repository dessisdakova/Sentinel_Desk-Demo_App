# Epic E06 — Playbooks & Async Execution

**Epic key:** `SENT-E06`  
**Summary:** Run predefined response playbooks via background jobs with UI polling.  
**Business value:** Consistent, repeatable response actions.

---

## Acceptance criteria

- [ ] Playbook definitions in DB (seed: Isolate host, Notify owner, Escalate)
- [ ] Page `/playbooks` lists playbooks with trigger severity
- [ ] From alert detail or playbooks page: Run playbook modal
- [ ] `POST /playbooks/{id}/run` enqueues Celery task, returns `task_id`
- [ ] UI polls `GET /jobs/{task_id}` or `GET /playbook-runs/{id}` until terminal state
- [ ] Playbook run creates `alert_events` for each step
- [ ] Failed step sets run status FAILED with error message

---

## Stories

| Story key | Title |
|-----------|-------|
| SENT-601 | Playbook + PlaybookRun models |
| SENT-602 | run_playbook Celery task (multi-step, delays) |
| SENT-603 | Playbook APIs + job status endpoint |
| SENT-604 | Playbooks page + run modal + polling UI |

---

## QA notes

- E2E: explicit wait for success — practice flakiness (BUG-003)
- Integration: playbook_runs row transitions PENDING→SUCCESS
- API: cannot run playbook on CLOSED alert → 400
