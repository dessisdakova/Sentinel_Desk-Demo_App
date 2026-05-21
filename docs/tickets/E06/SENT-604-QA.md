# SENT-604-QA — Test: Playbook run modal and polling

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Epic** | SENT-E06 Playbooks and Async Execution |
| **Implements after** | [SENT-604](./SENT-604.md), SENT-602, SENT-603 |
| **Test location** | `tests/e2e/`, `tests/integration/` |

---

## Summary

E2E and integration tests for async playbook execution UI.

---

## Test cases

| ID | Layer | Scenario | Expected |
|----|-------|----------|----------|
| QA-604-1 | integration | POST run → poll DB `playbook_runs.status` until SUCCESS | Pass |
| QA-604-2 | e2e | Run Isolate playbook on `ALERT_FOR_PLAYBOOK` | Success banner within 30s (WebDriverWait) |
| QA-604-3 | api | Run on CLOSED alert | 400 |

---

## Flakiness practice

Use explicit wait on `data-testid="playbook-run-status-success"`. After BUG-003 planted, add xfail test documenting premature success.

```python
WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="playbook-run-status-success"]'))
)
```

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md) — `ALERT_FOR_PLAYBOOK`, `PLAYBOOK_ISOLATE`

---

## Definition of Done

- [ ] Integration + E2E tests pass (except marked xfail for BUG-003)
