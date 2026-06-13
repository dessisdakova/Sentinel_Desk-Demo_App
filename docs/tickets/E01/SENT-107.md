# SENT-107 — Login page with data-testid

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Story Points** | 3 |
| **Status** | Done |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-107-QA](./SENT-107-QA.md) |

---

## Summary

Login page with data-testid.

---

## Description

**As a** SOC analyst  
**I want** a login form with stable `data-testid` attributes on every interactive element  
**So that** I can sign in to SentinelDesk and Selenium tests can reliably locate and interact with the form without depending on CSS classes or text content

---

## Acceptance criteria

### AC1 — Page root testid

- [x] Login page root element has `data-testid="page-login"`

### AC2 — Form field testids

- [x] Email input: `data-testid="login-email"`
- [x] Password input: `data-testid="login-password"`
- [x] Submit button: `data-testid="login-submit"`

### AC3 — Error feedback

- [x] Shows an error toast or inline message when the API returns `401` (invalid credentials)

### AC4 — Redirect on success

- [x] Successful login redirects the user to `/dashboard`

---

## Technical notes

---

## Out of scope

- Any files under repository root `tests/` (see paired QA ticket)
- Developer unit tests inside `backend/` or `frontend/`

---

## Definition of Done

- [x] Acceptance criteria met
- [x] `data-testid` hooks on new UI controls (if frontend)
- [x] OpenAPI updated (if API)
- [x] No test modules added outside `tests/`
- [x] Ticket ACs and DoD marked `[x]`, `Status: Done` added to metadata
- [x] `README.md` App implementation status updated for this ticket
- [ ] Epic checklist ticked only if this was the last story in the epic
