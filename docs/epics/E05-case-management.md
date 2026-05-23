# Epic E05 — Case Management

**Epic key:** `SENT-E05`  
**Summary:** Group related alerts into investigations with notes and status workflow.  
**Business value:** Track complex incidents across multiple events.

---

## Acceptance criteria

- [ ] Case list `/cases` with pagination and status filter
- [ ] Create case from alert detail (“Add to case” modal: new or existing)
- [ ] Case detail `/cases/:id` tabs: Overview | Alerts | Notes | Activity
- [ ] Notes: add note modal, author and timestamp visible
- [ ] Link/unlink alerts on case
- [ ] Only LEAD+ can close **case** (`CaseStatus.CLOSED`)
- [ ] `case_number` human-readable: `CASE-2026-00001`

---

## Stories

| Story key | Title |
|-----------|-------|
| SENT-501 | Case models + migration |
| SENT-502 | Case CRUD + link alerts API |
| SENT-503 | Case list + detail UI |
| SENT-504 | Notes API + modal |
| SENT-505 | Add-to-case from alert detail |

---

## QA notes

- Integration: link alert → verify `case_alerts` join table
- E2E: create case, add note, close as lead
