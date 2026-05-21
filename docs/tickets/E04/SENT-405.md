# SENT-405 — intel-embed static server and iframe tab

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E04 Alert Detail |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `infra`, `implementation` |
| **Paired QA ticket** | [SENT-405-QA](./SENT-405-QA.md) |

---

## Summary

intel-embed static server and iframe tab.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Alert Detail

---

## Acceptance criteria

### AC1 —

- [ ] intel-embed service port 8090 serves /embed
### AC2 —

- [ ] Iframe src includes ioc query param from first domain IOC

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

