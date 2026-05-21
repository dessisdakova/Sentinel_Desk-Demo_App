# SENT-1004-QA — Test: Bug garden (xfail suite)

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E10 Test Harness and Bug Garden |
| **Implements after** | [SENT-1004](./SENT-1004.md) |
| **Test location** | `tests/api/`, `tests/integration/`, `tests/e2e/` |

---

## Summary

Write one detecting test per BUG-001…BUG-008, marked **xfail** until fixed.

---

## Test cases

| ID | Bug | Layer | File (suggested) |
|----|-----|-------|------------------|
| QA-1004-1 | BUG-001 | api | `tests/api/test_bug_001_filter.py` |
| QA-1004-2 | BUG-002 | e2e | `tests/e2e/test_bug_002_bulk_assign.py` |
| QA-1004-3 | BUG-003 | e2e | `tests/e2e/test_bug_003_playbook_poll.py` |
| QA-1004-4 | BUG-004 | api | `tests/api/test_bug_004_escalation_rbac.py` |
| QA-1004-5 | BUG-005 | integration | `tests/integration/test_bug_005_audit_csv.py` |
| QA-1004-6 | BUG-006 | api | `tests/api/test_bug_006_webhook_sig.py` |
| QA-1004-7 | BUG-007 | integration | `tests/integration/test_bug_007_mttt_tz.py` |
| QA-1004-8 | BUG-008 | e2e | `tests/e2e/test_bug_008_iframe_ioc.py` |

Each test:

```python
@pytest.mark.bug("BUG-00X")
@pytest.mark.xfail(reason="BUG-00X: known defect", strict=False)
def test_...():
    ...
```

---

## Definition of Done

- [ ] Eight xfail tests run and fail for the right reason
- [ ] When a bug is fixed, remove xfail and set BUG status FIXED in BUG_GARDEN.md
