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

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Playbooks and Async Execution

---

## Acceptance criteria

### AC1 —

- [ ] playbooks and playbook_runs tables
### AC2 —

- [ ] Seed three playbooks per TEST_DATA
- [ ] `playbook_runs.status` enum: `PENDING`, `RUNNING`, `SUCCESS`, `FAILED` (CONSTITUTION §5.2)

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

