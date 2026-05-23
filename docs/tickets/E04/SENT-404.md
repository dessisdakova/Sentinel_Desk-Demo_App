# SENT-404 — IOC list component

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E04 Alert Detail |
| **Priority** | High |
| **Story Points** | 3 |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-404-QA](./SENT-404-QA.md) |

---

## Summary

IOC list component.

---

## Description

**As a** SOC analyst  
**I want** the IOCs tab to list each indicator of compromise with its type and a copy-to-clipboard button  
**So that** I can quickly extract IPs, domains, hashes, and URLs for pivoting into external threat intelligence tools

---

## Acceptance criteria

### AC1 — Render IOC types

- [ ] Each IOC in `ioc_list` is displayed with its `type` badge (`IP`, `DOMAIN`, `HASH`, `URL`) and `value` string

### AC2 — Copy button with testid

- [ ] Each IOC row has a copy-to-clipboard button with `data-testid="ioc-copy-{index}"` (zero-based index)

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
