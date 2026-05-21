# SENT-305-QA — Test: Bulk assign modal (E2E)

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E03 Triage Queue UI |
| **Implements after** | [SENT-305](./SENT-305.md) |
| **Test location** | `tests/e2e/` |

---

## Summary

E2E coverage for bulk assign from alert queue UI.

---

## Test cases

| ID | Scenario | Expected |
|----|----------|----------|
| QA-305-1 | Select 2 rows → bulk assign → confirm | Toast success; table shows assignee (may **xfail** after BUG-002) |
| QA-305-2 | Open bulk modal → cancel | No API call; selection cleared optional |

---

## Notes

- Use `data-testid`: `alert-queue-bulk-assign`, `bulk-assign-modal-confirm`
- After SENT-1004 plants BUG-002: mark QA-305-1 `@pytest.mark.xfail(reason="BUG-002")` until fixed

---

## Definition of Done

- [ ] E2E test in `tests/e2e/test_alert_queue_bulk.py`
- [ ] WebDriverWait on table refresh
