# SENT-603-QA — Test: Playbook APIs and playbook-run status

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E06 Playbooks and Async Execution |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-603](./SENT-603.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

API and integration tests for playbook list, run, and **`GET /api/v1/playbook-runs/{id}`** polling (not a generic jobs URL).

---

## Description

**As a** QA engineer  
**I want** tests that verify the canonical playbook async contract  
**So that** SENT-604 UI and integration tests poll the correct endpoint  

---

## Prerequisites

- [ ] Implementation ticket **SENT-603** is complete and merged/runnable
- [ ] **Seed baseline** — before SENT-1001 (E10): manual re-seed ([TEST_DATA.md §5](../../TEST_DATA.md#5-how-to-reset-by-phase) Option B/C); after SENT-1002-QA: `clean_db` or reset API

---

## Test scope

- **api** — add cases under `tests/api/`
- **integration** — add cases under `tests/integration/`

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-603-1 | api | `GET /api/v1/playbooks` as analyst | 200, includes `PLAYBOOK_ISOLATE` |
| QA-603-2 | api | `POST .../playbooks/{id}/run` on `ALERT_FOR_PLAYBOOK` | Returns `playbook_run_id`, `status: PENDING` |
| QA-603-3 | integration | Poll `GET /api/v1/playbook-runs/{id}` until `SUCCESS` | Status transitions; no `/jobs/` URL |
| QA-603-4 | api | Run on CLOSED alert | 400 |
| QA-603-5 | api | `playbook-runs` response `status` values | Only `PENDING`, `RUNNING`, `SUCCESS`, `FAILED` |

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md) — `ALERT_FOR_PLAYBOOK`, `PLAYBOOK_ISOLATE`

---

## Out of scope

- Fixing application bugs (file defects under BUG_GARDEN if found)
- Testing a generic `/api/v1/jobs/{task_id}` route (not part of E06)

---

## Definition of Done

- [ ] Tests run with `pytest tests/` (appropriate subset/markers)
- [ ] No dependency on manual data unless documented in test docstring
- [ ] Test file paths documented in this ticket (edit when created)
