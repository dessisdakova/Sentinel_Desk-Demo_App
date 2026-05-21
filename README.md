# SentinelDesk (DemoApp)

**SecOps Alert Triage Portal** — a QA practice platform for E2E, API, and integration testing.

## Status

| Epic | Status |
|------|--------|
| E01 SENT-101 | ✅ Docker infrastructure (Postgres, Redis, MailHog) |
| E01 SENT-101-QA | ✅ Integration tests for infra |
| E01 SENT-102 | ✅ FastAPI API + `/health` on port 8000 |
| E01 SENT-102-QA | Next — API tests for health |
| E01 SENT-103+ | Planned — DB models, auth, frontend |

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows, macOS, or Linux)
- **Later epics:** Python 3.12+, Node.js 20+

Optional database GUI: [DBeaver](https://dbeaver.io/) or [pgAdmin](https://www.pgadmin.org/) connecting to `localhost:5432`.

## Local infrastructure (SENT-101)

### First-time setup

```powershell
# From repository root
cd d:\Personal-Projects\DemoApp
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

### Connection defaults

Aligned with [.env.example](.env.example):

- **Postgres:** `sentinel` / `sentinel` @ `localhost:5432` / database `sentineldesk`
- **Redis:** `redis://localhost:6379/0`
- **MailHog UI:** http://localhost:8025

## Documentation map

| Document | Purpose |
|----------|---------|
| [docs/CONSTITUTION.md](docs/CONSTITUTION.md) | Product vision, modules, pages, roles, NFRs |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Technical design, Docker, APIs, async |
| [docs/TEST_DATA.md](docs/TEST_DATA.md) | Seed users, stable IDs, reset guide |
| [docs/TESTING_STRATEGY.md](docs/TESTING_STRATEGY.md) | How you will test by layer |
| [docs/BUG_GARDEN.md](docs/BUG_GARDEN.md) | Intentional defects |
| [docs/epics/README.md](docs/epics/README.md) | Implementation epics E01–E11 |
| [docs/tickets/](docs/tickets/) | Implementation + QA tickets per epic |

## Tech stack

- **Backend:** Python 3.12 + FastAPI + Uvicorn
- **Database:** PostgreSQL 16 (Docker)
- **Queue:** Redis 7 (Docker)
- **Email (dev):** MailHog (Docker)
- **Frontend:** React + Vite — coming in SENT-106+

## Next implementation ticket

**SENT-103** — User model and Alembic initial migration.
