# SENT-103-QA — Test: User model and Alembic initial migration

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-103](./SENT-103.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Design and implement automated tests for **SENT-103** — User model and Alembic initial migration.

---

## Test cases (minimum)

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-103-1 | integration | Schema/columns/constraints | Present |
| QA-103-2 | integration | Migrations applied | ? |
| QA-103-3 | integration | role column uses a PostgreSQL enum | Pass |
| QA-103-4 | integration | bad role insert fails | ? |

Extend with boundary cases from implementation acceptance criteria.

---

## Artifacts
To-Do

---

## How to run
To-dO

---

## Definition of Done

- [ ] Tests run with `pytest tests/` (appropriate subset/markers)
- [ ] No dependency on manual data unless documented in test docstring
- [ ] Test file paths documented in this ticket (edit when created)

---

## Completion
To-Do

**Next:** [SENT-104-QA](./SENT-104-QA.md)