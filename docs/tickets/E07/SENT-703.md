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

**As a** QA engineer  
**I want** the mock SIEM service to expose a callback endpoint that records the last received webhook payload  
**So that** integration tests can assert that outbound webhook deliveries reach the expected destination with the correct payload

---

## Acceptance criteria

### AC1 — Callback endpoint

- [ ] The `mock-siem` service exposes `POST /callback` which accepts any JSON body and returns `200`

### AC2 — Last payload accessible for tests

- [ ] The mock SIEM stores the most recently received payload in memory and exposes it via `GET /callback/last` (returns `null` if no payload received yet)

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
- [ ] Ticket ACs and DoD marked `[x]`, `Status: Done` added to metadata
- [ ] `README.md` App implementation status updated for this ticket
- [ ] Epic checklist ticked only if this was the last story in the epic
