# SENT-603 — Playbook APIs and job status endpoint

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

Playbook APIs and job status endpoint.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Playbooks and Async Execution

---

## Acceptance criteria

### AC1 —

- [ ] GET /api/v1/playbooks
### AC2 —

- [ ] POST /api/v1/playbooks/{id}/run
### AC3 —

- [ ] GET /api/v1/playbook-runs/{id}
### AC4 —

- [ ] GET /api/v1/jobs/{task_id}

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

