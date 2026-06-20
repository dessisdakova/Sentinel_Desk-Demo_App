# SENT-106 — React app shell, router, auth context

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Story Points** | 5 |
| **Status** | Done |
| **Labels** | `frontend`, `implementation` |
| **Paired QA ticket** | [SENT-106-QA](./SENT-106-QA.md) |

---

## Summary

React app shell, router, auth context.

---

## Description

**As a** SOC analyst  
**I want** a React SPA scaffold with JWT-based auth context and role-aware navigation  
**So that** I am redirected to login when unauthenticated and see only the nav items my role permits

---

## Acceptance criteria

### AC1 — Vite + React scaffold

- [x] Vite + React + TypeScript scaffold exists in `frontend/`

### AC2 — Router with auth guard

- [x] Routes: `/login` (public), protected layout with outlet; unauthenticated users are redirected to `/login`

### AC3 — Auth context and token handling

- [x] `AuthContext` stores JWT in React state and `sessionStorage` key `sentinel_access_token`
- [x] API client attaches `Authorization: Bearer <token>` on every request; clears storage on logout
- [x] Redirects unauthenticated users to `/login`

### AC4 — Role-based navigation placeholders

- [x] Nav renders role-appropriate items; Dashboard and Alerts links are present but disabled until later epics ship

### AC5 — Docker frontend service

- [x] `frontend` service in `docker-compose.yml` on port `5173` (Vite dev server)
- [x] `docker compose up -d --build` starts the frontend container
- [x] README documents the SPA at http://localhost:5173

---

## Technical notes

- Follow [ARCHITECTURE.md](../../ARCHITECTURE.md) §3 auth contract — JWT Bearer + sessionStorage only
- Follow [ARCHITECTURE.md](../../ARCHITECTURE.md) §8 — add `frontend` to compose (dev image with Vite on `5173`; production nginx is out of scope for E01)
- API CORS must allow `http://localhost:5173` when the API service is updated for frontend (SENT-104 or this ticket if CORS not yet wired)
- Set `VITE_API_URL=http://localhost:8000` (or equivalent) in `.env.example` for the SPA build/dev server
- No alert pages yet.

## Artifacts

| Path | Purpose |
|------|---------|
| `frontend/` | Vite + React + TypeScript scaffold |
| `frontend/Dockerfile` | Frontend dev container |
| `docker-compose.yml` | `frontend` service |
| `.env.example` | `VITE_API_URL` (and related frontend vars) |

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
