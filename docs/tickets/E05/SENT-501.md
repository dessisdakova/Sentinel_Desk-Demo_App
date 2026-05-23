# SENT-501 — Case models and migration

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E05 Case Management |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-501-QA](./SENT-501-QA.md) |

---

## Summary

Case models and migration.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Case Management

---

## Acceptance criteria

### AC1 —

- [ ] cases, case_alerts, case_notes tables
### AC2 —

- [ ] case_number format CASE-YYYY-NNNNN
- [ ] `CaseStatus` enum on `cases.status`: `OPEN`, `IN_PROGRESS`, `CLOSED` (CONSTITUTION §5.2)

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

