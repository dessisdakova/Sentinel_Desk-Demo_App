# SentinelDesk — Bug Garden

Intentional defects for QA practice. Tests referencing these bugs should use `@pytest.mark.xfail` until fixed.

**Policy:** Do not fix bugs in the same PR that adds the failing test — practice red → green cycle.

---

## Status legend

| Status | Meaning |
|--------|---------|
| `PLANTED` | Not implemented yet — reserved slot |
| `ACTIVE` | In codebase, test should fail |
| `FIXED` | Resolved — remove xfail |

---

## Bug catalog

### BUG-001 — Severity filter ignores CRITICAL when combined with date range

| Field | Value |
|-------|-------|
| Status | PLANTED |
| Area | Alert queue API + UI |
| Steps | Set severity=CRITICAL and date range = last 7 days |
| Expected | Only CRITICAL alerts in range |
| Actual | Returns all severities |
| Test idea | API: `GET /alerts?severity=CRITICAL&from=...` count mismatch vs DB query |

---

### BUG-002 — Bulk assign modal closes but does not persist assignment

| Field | Value |
|-------|-------|
| Status | PLANTED |
| Area | Alert queue UI |
| Steps | Select 2 alerts → Bulk assign → Choose analyst → Confirm |
| Expected | `assigned_to` updated on both |
| Actual | Toast success but DB unchanged |
| Test idea | E2E + integration DB check |

---

### BUG-003 — Playbook polling shows success before Celery task completes

| Field | Value |
|-------|-------|
| Status | PLANTED |
| Area | Playbook run UI |
| Steps | Run "Isolate host" on slow alert |
| Expected | Success UI only when `playbook_runs.status` is `SUCCESS` |
| Actual | Success banner at 1s while status still `RUNNING` |
| Test idea | E2E race — good flakiness lesson with proper waits |

---

### BUG-004 — Analyst can approve own escalation (RBAC bypass)

| Field | Value |
|-------|-------|
| Status | PLANTED |
| Area | Alert detail → Escalation tab |
| Steps | Analyst escalates, same analyst clicks Approve |
| Expected | 403 Forbidden |
| Actual | 200 OK |
| Test idea | API negative test + E2E |

---

### BUG-005 — Audit export CSV truncates at 100 rows without warning

| Field | Value |
|-------|-------|
| Status | PLANTED |
| Area | Audit log page |
| Steps | Seed >150 audit rows, export CSV |
| Expected | All rows or explicit limit message |
| Actual | Silent truncate at 100 |
| Test idea | Integration: compare CSV line count to DB count |

---

### BUG-006 — Webhook signature not validated on mock SIEM callback

| Field | Value |
|-------|-------|
| Status | PLANTED |
| Area | Outbound webhooks |
| Steps | POST callback without `X-Sentinel-Signature` |
| Expected | 401 |
| Actual | 200 |
| Test idea | Security-adjacent API test (lower priority per your goals) |

---

### BUG-007 — Dashboard MTTT metric uses wrong timezone (UTC vs local)

| Field | Value |
|-------|-------|
| Status | PLANTED |
| Area | Dashboard metrics |
| Steps | Compare dashboard KPI to manual SQL for “today” in local TZ |
| Expected | Match local midnight boundary |
| Actual | Off by one day near midnight |
| Test idea | Integration with frozen clock (`freezegun`) |

---

### BUG-008 — iframe Threat Intel tab: IOC query parameter not passed

| Field | Value |
|-------|-------|
| Status | PLANTED |
| Area | Alert detail iframe |
| Steps | Open alert with domain IOC `evil.demo` |
| Expected | iframe URL contains `?ioc=evil.demo` |
| Actual | iframe loads generic page |
| Test idea | E2E `switch_to.frame` + assert URL or embedded text |

---

## Adding new bugs

1. Add row to this file with reproduction steps.  
2. Link verification to `docs/tickets/E10/SENT-1004-QA.md` (xfail tests).  
3. Add pytest marker and xfail.  
4. When learning exercise complete, fix and mark `FIXED`.
