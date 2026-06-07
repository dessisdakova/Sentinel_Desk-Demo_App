# SENT-104 — Auth API (login / logout / me)

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Status** | Done |
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

The API must issue a JWT access token (8-hour lifetime) and expose a profile endpoint for the SPA to build navigation.

---

## Acceptance criteria

### AC1 — Login success

- **Given** seeded user `analyst@demo.local` with password `DemoPass123!`
- **When** `POST /api/v1/auth/login` with JSON body `{ "email", "password" }`
- **Then** response `200` contains `access_token`, `token_type: "bearer"`, `expires_in: 28800` (8h; from `JWT_EXPIRE_HOURS`)
- **And** token contains claim `role=ANALYST` (and `sub` = user id)

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

- Use `python-jose` or PyJWT; secret from `JWT_SECRET`; expiry from `JWT_EXPIRE_HOURS` (default 8)
- Password verify: bcrypt via `passlib`
- **No refresh token** and **no HttpOnly cookies** in this story
- OpenAPI tags: `auth`

---

## Artifacts

| Path | Purpose |
|------|---------|
| `backend/app/api/routes/auth.py` | Login, logout, me routes |
| `backend/app/services/auth_service.py` | Login business logic |
| `backend/app/core/security.py` | bcrypt + JWT helpers |
| `backend/app/core/deps.py` | `get_current_user` Bearer dependency |
| `backend/app/schemas/auth.py` | Request/response Pydantic models |

---

## Out of scope

- OAuth / SSO
- Password reset flow
- Rate limiting (may become BUG later)
- Any files under repository root `tests/` (see SENT-104-QA)

---

## Definition of Done

- [x] Acceptance criteria met
- [x] Documented in OpenAPI `/docs`
- [x] No test modules added outside `tests/`
- [x] Ticket ACs and DoD marked `[x]`, `Status: Done` added to metadata
- [x] `README.md` App implementation status updated for this ticket
- [x] Epic checklist ticked only if this was the last story in the epic
