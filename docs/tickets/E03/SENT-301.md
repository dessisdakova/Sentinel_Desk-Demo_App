# SENT-301 — Alerts list API with filters and pagination

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E03 Triage Queue UI |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-301-QA](./SENT-301-QA.md) |

---

## Summary

Alerts list API with filters and pagination.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Triage Queue UI

---

## Acceptance criteria

### AC1 —

- [ ] GET /api/v1/alerts supports page, size, severity, status, source, assigned_to, from, to, sort
### AC2 —

- [ ] Returns total count for pagination
### AC3 —

- [ ] Invalid enum returns 422

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

