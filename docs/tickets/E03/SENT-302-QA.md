# SENT-302-QA — Test: PATCH and bulk alert API

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E03 Triage Queue UI |
| **Implements after** | [SENT-302](./SENT-302.md) |
| **Test location** | `tests/api/`, `tests/integration/` |

---

## Summary

API and DB integration tests for single and bulk alert updates.

---

## Test cases

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-302-1 | api | PATCH assign `ALERT_OPEN_HIGH` to analyst | 200 |
| QA-302-2 | integration | After QA-302-1, DB `assigned_to_id` matches | Pass |
| QA-302-3 | api | Bulk assign two seed alerts | `updated: 2` |
| QA-302-4 | integration | Bulk assign → count DB rows updated | Pass |
| QA-302-5 | api | Bulk with closed alert | `failed` non-empty |
| QA-302-6 | api | Empty `alert_ids` | 422 |

**After E10 (BUG-002):** API bulk tests should still pass; E2E bulk may xfail — see SENT-1004-QA.

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md) — `ALERT_OPEN_HIGH` (`seed-edr-001`), second alert constant as needed

---

## Definition of Done

- [ ] `tests/api/test_alerts_bulk.py` (or equivalent) passes
- [ ] Mutating tests leave DB restorable — manual re-seed before SENT-1001; `clean_db` after SENT-1002-QA
