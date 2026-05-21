# SENT-402 — Escalation state machine and approval API

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E04 Alert Detail |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-402-QA](./SENT-402-QA.md) |

---

## Summary

Escalation state machine and approval API.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Alert Detail

---

## Acceptance criteria

### AC1 —

- [ ] Analyst can request escalation to ESCALATED_PENDING
### AC2 —

- [ ] Lead approves or rejects escalation
### AC3 —

- [ ] Audit entries for each transition

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

