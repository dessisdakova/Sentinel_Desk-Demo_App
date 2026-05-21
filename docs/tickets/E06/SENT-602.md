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

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Playbooks and Async Execution

---

## Acceptance criteria

### AC1 —

- [ ] Multi-step task with 2-5s delay per step
### AC2 —

- [ ] Statuses PENDING, RUNNING, SUCCESS, FAILED
### AC3 —

- [ ] Writes alert_events per step

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

