# SENT-405 — intel-embed static server and iframe tab

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E04 Alert Detail |
| **Priority** | High |
| **Story Points** | 5 |
| **Labels** | `infra`, `implementation` |
| **Paired QA ticket** | [SENT-405-QA](./SENT-405-QA.md) |

---

## Summary

intel-embed static server and iframe tab.

---

## Description

**As a** SOC analyst  
**I want** the Threat Intel tab on the alert detail page to embed a mock threat intelligence page in an iframe, pre-seeded with the alert's first domain IOC as a query parameter  
**So that** Selenium tests can practise switching into iframes and asserting embedded content, simulating real SOC portal integrations

---

## Acceptance criteria

### AC1 — intel-embed Docker service

- [ ] A Docker service (`intel-embed`) on port `8090` serves a static HTML page at `GET /embed` that renders visible content (e.g. a fake VirusTotal-style report)

### AC2 — Iframe passes IOC query param

- [ ] The Threat Intel tab renders `<iframe src="http://localhost:8090/embed?ioc={value}">` where `{value}` is the `value` of the first `domain`-type IOC in `ioc_list`; if no domain IOC exists, the param is omitted

---

## Technical notes

---

## Out of scope

- Any files under repository root `tests/` (see paired QA ticket)
- Developer unit tests inside `backend/` or `frontend/`

---

## Definition of Done

- [ ] Acceptance criteria met
- [ ] `data-testid` hooks on new UI controls (if frontend)
- [ ] OpenAPI updated (if API)
- [ ] No test modules added outside `tests/`
- [ ] Ticket ACs and DoD marked `[x]`, `Status: Done` added to metadata
- [ ] `README.md` App implementation status updated for this ticket
- [ ] Epic checklist ticked only if this was the last story in the epic
