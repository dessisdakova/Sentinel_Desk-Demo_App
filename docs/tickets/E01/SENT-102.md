# SENT-102 — FastAPI project structure and health endpoint

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Status** | **Done** |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Story Points** | 3 |
| **Labels** | `backend`, `implementation` |
| **Paired QA ticket** | [SENT-102-QA](./SENT-102-QA.md) |

---

## Summary

FastAPI project structure and health endpoint.

---

## Description

**As a** SentinelDesk user or operator  
**I want** this capability built in the application  
**So that** the platform meets the epic goal for Platform Foundation

---

## Acceptance criteria

### AC1 — Health endpoint

- [x] `GET /health` returns `200` with body `{ "status": "ok" }`

### AC2 — Docker API service

- [x] `api` service in `docker-compose.yml` on port `8000`
- [x] `docker compose up -d --build` starts the API

### AC3 — Structured logging

- [x] `RequestIdMiddleware` sets `X-Request-ID` on responses
- [x] Logs include `request_id=` per request

---

## Technical notes

Skeleton: `backend/app/main.py`, `core/config`, `api/router`, `routes/health.py`.

---

## Artifacts

| Path | Purpose |
|------|---------|
| `backend/requirements.txt` | FastAPI, Uvicorn, pydantic-settings |
| `backend/Dockerfile` | API container image |
| `backend/app/main.py` | Application entry |
| `backend/app/api/routes/health.py` | `GET /health` |
| `docker-compose.yml` | `api` service |

---

## Out of scope

- Any files under repository root `tests/` (see paired QA ticket)
- Developer unit tests inside `backend/` or `frontend/`

---

## Definition of Done

- [x] Acceptance criteria met
- [x] OpenAPI at `/docs`
- [x] No test modules added outside `tests/`
