# SentinelDesk (DemoApp)

**SecOps Alert Triage Portal** — a QA practice platform for E2E, API, and integration testing.

## Status

### App implementation (implementation agent)

| Epic | Status |
|------|--------|
| E01 SENT-101 | ✅ Docker infrastructure (Postgres, Redis, MailHog) |
| E01 SENT-102 | ✅ FastAPI API + `/health` on port 8000 |
| E01 SENT-103 | ✅ User model + Alembic (`users` table, `user_role` enum) |
| E01 SENT-104 | ✅ JWT auth API (`/api/v1/auth/login`, `/me`, `/logout`) |
| E01 SENT-105 | ✅ RBAC `require_roles` dependency + `GET /api/v1/admin/ping` |
| E01 SENT-106 | ✅ React SPA shell, router, auth context, role nav (port 5173) |
| E01 SENT-107 | ✅ Login page with form validation and `data-testid` hooks |
| E01 SENT-108+ | Next — seed script |

### QA automation (QA engineer — separate workflow)

| Epic | Status |
|------|--------|
| E01 SENT-101-QA | ✅ Integration tests for infra |
| E01 SENT-102-QA | ✅ API tests for health + `X-Request-ID` |
| E01 SENT-103-QA | ✅ Integration tests for `users` schema, Alembic, enum constraints |
| E01 SENT-104-QA | ✅ API + integration auth tests (21 tests) |
| E01 SENT-105-QA | ✅ API + integration RBAC tests (5 tests) |
| E01 SENT-106-QA | ✅ API tests (3 tests) |
| E01 SENT-107-QA | ✅ E2E bootstrap — Playwright scaffold + 7 login tests |

**Implementation agents:** read [docs/IMPLEMENTATION_AGENT.md](docs/IMPLEMENTATION_AGENT.md) — do not modify `tests/` or implement `-QA` tickets.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows, macOS, or Linux)
- Python 3.12+ and IDE of your choice
- Node.js 20+ (frontend local dev without Docker)

## Local infrastructure (SENT-101)

### First-time setup

```powershell
# From repository root
copy .env.example .env
docker compose up -d
docker compose ps
```

### Start / stop

```powershell
# Start infrastructure in the background
docker compose up -d

# Stop containers (keep data volumes)
docker compose stop

# Stop and remove containers (keep volumes)
docker compose down

# Stop and remove containers AND data (fresh database)
docker compose down -v
```

### Verify services

| Service | Host port | Check |
|---------|-----------|--------|
| PostgreSQL 16 | 5432 | `docker compose exec postgres pg_isready -U sentinel -d sentineldesk` |
| Redis 7 | 6379 | `docker compose exec redis redis-cli ping` → `PONG` |
| **API (FastAPI)** | **8000** | `curl http://localhost:8000/health` → `{"status":"ok"}` |
| MailHog SMTP | 1025 | Used by app later |
| MailHog UI | 8025 | Open http://localhost:8025 in a browser |
| **Frontend (React SPA)** | **5173** | Open http://localhost:5173 in a browser |

## API (SENT-102)

### Run with Docker (recommended)

```powershell
docker compose up -d --build
curl http://localhost:8000/health
```

OpenAPI docs: http://localhost:8000/docs

### Run locally (without API container)

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
# from repo root, with infra up:
cd ..
uvicorn app.main:app --app-dir backend --host 0.0.0.0 --port 8000 --reload
```

Ensure `.env` is in the repo root (or export `ENVIRONMENT=local`). Logs include `request_id=` per request; responses include header `X-Request-ID`.

## Database (SENT-103)

After Postgres is up, apply migrations (from repo root):

```powershell
docker compose exec api alembic upgrade head
```

Fresh database volume:

```powershell
docker compose down -v
docker compose up -d
docker compose exec api alembic upgrade head
```

Access databade:

```powershell
docker compose exec postgres psql -U sentinel -d sentineldesk
```

Once you’re in the psql prompt, useful commands:

```powershell
\dt                                 # List tables
\d users                            # Describe users table
SELECT * FROM users;                # Select all users
SELECT id, email, role FROM users;  # Select id, email, role from users table
\q                                  # Quit psql
```

Schema: `users` table with `user_role` enum (`ANALYST`, `LEAD`, `ADMIN`). Seed users arrive in **SENT-108**.

## Auth API (SENT-104)

Requires seeded users (SENT-108) or manual rows in `users`. Example login:

```powershell
curl -s -X POST http://localhost:8000/api/v1/auth/login `
  -H "Content-Type: application/json" `
  -d '{\"email\":\"analyst@demo.local\",\"password\":\"DemoPass123!\"}'
```

Use the returned `access_token` as `Authorization: Bearer <token>` on `GET /api/v1/auth/me` and `POST /api/v1/auth/logout` (204). Token lifetime: `JWT_EXPIRE_HOURS` × 3600 seconds (default 28800).

## Frontend (SENT-106 / SENT-107)

### Run with Docker (recommended)

```powershell
docker compose up -d --build
```

Open the SPA: http://localhost:5173

Unauthenticated visitors are redirected to `/login`. Sign in with seed users (**SENT-108**) or rows you insert manually. Invalid credentials show an inline error (`data-testid="login-error"`); success redirects to `/dashboard`.

### Run locally (without frontend container)

```powershell
cd frontend
npm install
# Ensure repo root .env defines VITE_API_URL=http://localhost:8000
npm run dev
```

The Vite dev server listens on http://localhost:5173. JWT is stored in `sessionStorage` under `sentinel_access_token`.

### Connection defaults

Aligned with [.env.example](.env.example):

- **Postgres:** `sentinel` / `sentinel` @ `localhost:5432` / database `sentineldesk`
- **Redis:** `redis://localhost:6379/0`
- **MailHog UI:** http://localhost:8025

## Documentation map

| Document | Purpose |
|----------|---------|
| [docs/IMPLEMENTATION_AGENT.md](docs/IMPLEMENTATION_AGENT.md) | **Implementation agent charter** — scope, boundaries, what to ignore |
| [docs/CONSTITUTION.md](docs/CONSTITUTION.md) | Product vision, modules, pages, roles, NFRs |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Technical design, Docker, APIs, async |
| [docs/TEST_DATA.md](docs/TEST_DATA.md) | Seed users, stable IDs, reset guide (QA) |
| [docs/TESTING_STRATEGY.md](docs/TESTING_STRATEGY.md) | QA automation framework (QA engineer only) |
| [docs/BUG_GARDEN.md](docs/BUG_GARDEN.md) | Intentional defects |
| [docs/epics/README.md](docs/epics/README.md) | Implementation epics E01–E11 |
| [docs/tickets/](docs/tickets/) | Implementation + QA tickets per epic |

## Tech stack

- **Backend:** Python 3.12 + FastAPI + Uvicorn
- **Database:** PostgreSQL 16 (Docker)
- **Queue:** Redis 7 (Docker)
- **Email (dev):** MailHog (Docker)
- **Frontend:** React 19 + Vite + TypeScript + Tailwind (SENT-106+)

## Next implementation ticket

**SENT-108** — Seed script for users.
