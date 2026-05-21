# Epic E08 — Dashboard & Audit

**Epic key:** `SENT-E08`  
**Summary:** KPI dashboard for supervisors and immutable audit export.  
**Business value:** Visibility into team workload and compliance.

---

## Acceptance criteria

- [ ] Dashboard `/dashboard` with cards: open alerts, mean time to triage, escalations pending, cases open
- [ ] Date range picker affects metrics (Redis cache 30s)
- [ ] Audit log `/audit` table: who, what, when, entity — LEAD+ only
- [ ] Export CSV button downloads audit rows for filter range
- [ ] All mutating APIs write audit log (verify sample actions)

---

## Stories

| Story key | Title |
|-----------|-------|
| SENT-801 | metrics/summary API + Redis cache |
| SENT-802 | Dashboard React + date picker |
| SENT-803 | Audit log API + pagination |
| SENT-804 | Audit page + CSV export |

---

## QA notes

- API: audit entries created on PATCH alert
- E2E: lead exports CSV
- BUG-005 / BUG-007 planted in E10
