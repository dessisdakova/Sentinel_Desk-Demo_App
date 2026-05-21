# Epic E09 — Admin & Notifications

**Epic key:** `SENT-E09`  
**Summary:** Admin console for users/rules; email via MailHog; SMS as UI mock.  
**Business value:** Operate the platform without code changes.

---

## Acceptance criteria

- [ ] Admin page `/admin` tabs: Users | Detection Rules | Webhooks
- [ ] CRUD users (role assignment, deactivate)
- [ ] Detection rules: simple JSON conditions (severity + source → auto-tag)
- [ ] On escalation/assignment: email sent to MailHog
- [ ] SMS: `Notification` record + toast only
- [ ] MailHog link in admin footer for QA convenience

---

## Stories

| Story key | Title |
|-----------|-------|
| SENT-901 | Admin users API + UI |
| SENT-902 | Detection rules model + apply on enrich |
| SENT-903 | send_email Celery task → MailHog |
| SENT-904 | Notification model + SMS mock toast |

---

## QA notes

- E2E: open MailHog UI in new tab (optional) or API MailHog v2 messages
- Integration: escalation creates notification row status SENT
