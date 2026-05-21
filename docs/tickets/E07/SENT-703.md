# SENT-703 — mock-siem callback endpoint

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E07 Outbound Webhooks |
| **Priority** | High |
| **Story Points** | 3 |
| **Labels** | `infra`, `implementation` |
| **Paired QA ticket** | [SENT-703-QA](./SENT-703-QA.md) |

---

## Summary

mock-siem callback endpoint.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Outbound Webhooks

---

## Acceptance criteria

### AC1 —

- [ ] mock-siem exposes POST /callback
### AC2 —

- [ ] Records last payload for tests

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

