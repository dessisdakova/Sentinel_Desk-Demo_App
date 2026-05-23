# Epic E03 — Triage Queue UI

**Epic key:** `SENT-E03`  
**Summary:** Analyst-facing alert queue with server-side pagination, rich filters, bulk actions.  
**Business value:** Reduce MTTT — find the right alerts fast.

---

## Acceptance criteria

- [ ] Page `/alerts` with data-testid `page-alert-queue`
- [ ] Table columns: id, title, severity, status, source, assigned_to, sla_due_at, created_at
- [ ] Server pagination (page size 25, 50, 100)
- [ ] Filters: severity, status, source, assigned_to, date range (created_at)
- [ ] Sort by created_at, severity, sla_due_at
- [ ] Bulk select → modal: assign to analyst / change status
- [ ] Auto-refresh poll every 10s (configurable in frontend env)
- [ ] API `GET /api/v1/alerts` supports query params matching UI
- [ ] PATCH single alert updates assignee/status with audit

---

## UI patterns (required)

- Data table with pagination controls
- Rich filter bar with date pickers
- Bulk action modal
- Toast on success/error

---

## Stories

| Story key | Title |
|-----------|-------|
| SENT-301 | Alerts list API with filters + pagination |
| SENT-302 | PATCH alert + bulk endpoint |
| SENT-303 | Alert queue React page + table |
| SENT-304 | Filter bar + date pickers |
| SENT-305 | Bulk assign modal |
| SENT-306 | Queue auto-refresh polling |

---

## QA notes

- API: pagination boundaries, invalid filter values 422
- E2E: filter CRITICAL + verify row count — requires SENT-107-QA bootstrap; expand `AlertQueuePage` in SENT-303-QA / SENT-1003-QA
- E2E: bulk assign (becomes BUG-002 target in E10)
