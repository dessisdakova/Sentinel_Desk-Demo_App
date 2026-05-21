# SENT-104 — Auth API (login / logout / me)

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | Highest |
| **Story Points** | 5 |
| **Labels** | `backend`, `api`, `auth`, `implementation` |
| **Components** | API, Security |
| **Paired QA ticket** | [SENT-104-QA](./SENT-104-QA.md) |

---

## Summary

Implement JWT authentication endpoints for SentinelDesk users.

---

## Description

**As a** SOC analyst  
**I want to** log in with my work email and password  
**So that** I can access alerts and cases assigned to my role  

The API must issue a short-lived access token and expose a profile endpoint for the SPA to build navigation.

---

## Acceptance criteria

### AC1 — Login success

- **Given** seeded user `analyst@demo.local` with password `DemoPass123!`
- **When** `POST /api/v1/auth/login` with JSON body `{ "email", "password" }`
- **Then** response `200` contains `access_token`, `token_type: "bearer"`, `expires_in`
- **And** token contains claim `role=ANALYST`

### AC2 — Login failure

- **Given** valid email and wrong password
- **When** login is attempted
- **Then** response `401` with error body `{ "error": { "code": "INVALID_CREDENTIALS", ... } }`
- **And** no token is returned

### AC3 — Me endpoint

- **Given** valid Bearer token for lead user
- **When** `GET /api/v1/auth/me`
- **Then** response `200` with `id`, `email`, `role`, `display_name`

### AC4 — Logout

- **Given** valid token
- **When** `POST /api/v1/auth/logout`
- **Then** response `204` (client discards token; optional server denylist out of scope)

### AC5 — Inactive user

- **Given** user `active=false` in DB
- **When** login attempted
- **Then** `403` with code `ACCOUNT_DISABLED`

---

## Technical notes

- Use `python-jose` or PyJWT; secret from `JWT_SECRET` env
- Password verify: bcrypt via `passlib`
- Do not implement refresh token in this story (optional later)
- OpenAPI tags: `auth`

---

## Out of scope

- OAuth / SSO
- Password reset flow
- Rate limiting (may become BUG later)
- Any files under repository root `tests/` (see SENT-104-QA)

---

## Definition of Done

- [ ] Acceptance criteria met
- [ ] Documented in OpenAPI `/docs`
- [ ] No test modules added outside `tests/`
