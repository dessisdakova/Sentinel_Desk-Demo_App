# Epic E04 — Alert Detail (Multi-tab + Iframe)

**Epic key:** `SENT-E04`  
**Summary:** Deep dive on one alert: summary, timeline, IOCs, related cases, threat intel iframe.  
**Business value:** Analysts have full context before disposition.

---

## Acceptance criteria

- [ ] Route `/alerts/:id` with tabs: Summary | Timeline | IOCs | Related | Threat Intel
- [ ] Summary: edit severity, status (role-gated), assignee dropdown
- [ ] Timeline: append-only events from `alert_events` + audit
- [ ] IOCs: list with copy button; types IP, DOMAIN, HASH, URL
- [ ] Related: linked cases with navigation
- [ ] Threat Intel tab: iframe `http://localhost:8090/embed?ioc=<first-domain>`
- [ ] Escalation flow: analyst requests → lead approves (API + UI)
- [ ] intel-embed docker service serves static HTML

---

## Stories

| Story key | Title |
|-----------|-------|
| SENT-401 | Alert detail API + events endpoint |
| SENT-402 | Escalation state machine + approval API |
| SENT-403 | Alert detail React tabs |
| SENT-404 | IOC list component |
| SENT-405 | intel-embed static server + iframe tab |
| SENT-406 | Escalation UI on Summary tab |

---

## QA notes

- E2E: tab switching preserves alert id in URL
- E2E: iframe switch and assert IOC text (BUG-008 later)
- API: escalation forbidden for analyst approve (BUG-004 later)
