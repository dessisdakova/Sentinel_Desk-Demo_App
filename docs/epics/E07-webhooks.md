# Epic E07 — Outbound Webhooks

**Epic key:** `SENT-E07`  
**Summary:** Notify external systems when alert status changes; retry on failure.  
**Business value:** Integration with ticketing/SOAR tools (simulated).

---

## Acceptance criteria

- [ ] Admin can CRUD webhook subscriptions (url, events[], secret)
- [ ] On alert status change, worker POSTs signed payload to subscriber URL
- [ ] `webhook_deliveries` logs each attempt with response code
- [ ] 3 retries with exponential backoff on 5xx/timeout
- [ ] mock-siem exposes `/callback` to receive webhooks for tests
- [ ] Delivery log visible in Admin UI

---

## Stories

| Story key | Title |
|-----------|-------|
| SENT-701 | Webhook subscription model + admin API |
| SENT-702 | deliver_webhook Celery task with retries |
| SENT-703 | mock-siem callback endpoint |
| SENT-704 | Admin UI delivery log table |

---

## QA notes

- Integration: trigger status change → assert delivery row SUCCESS
- API: invalid signature on callback (BUG-006)
