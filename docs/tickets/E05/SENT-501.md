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

**As a** SOC investigation platform  
**I want** `cases`, `case_alerts`, and `case_notes` tables with a human-readable case number format  
**So that** analysts can group related alerts into named investigations and leads can track and close them through a defined status lifecycle

---

## Acceptance criteria

### AC1 — Case, CaseAlert, and CaseNote tables

- [ ] `cases` table: `id` (UUID PK), `case_number` (unique string), `status` (`CaseStatus` enum), `priority`, `lead_id` (FK users), `created_at`, `updated_at`
- [ ] `case_alerts` join table: `case_id` (FK), `alert_id` (FK), `linked_at`
- [ ] `case_notes` table: `id` (UUID PK), `case_id` (FK), `body` (text), `author_id` (FK users), `created_at`
- [ ] Migration runs cleanly with `alembic upgrade head`

### AC2 — Case number format and CaseStatus enum

- [ ] `case_number` follows format `CASE-YYYY-NNNNN` (e.g. `CASE-2026-00001`) — auto-generated on insert
- [ ] `CaseStatus` enum on `cases.status`: `OPEN`, `IN_PROGRESS`, `CLOSED` — **separate from `AlertStatus`** (CONSTITUTION §5.2)

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
