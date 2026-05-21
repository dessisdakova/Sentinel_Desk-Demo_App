# SentinelDesk (DemoApp)

**SecOps Alert Triage Portal** — a QA practice platform for E2E, API, and integration testing.

## Status

| Epic | Status |
|------|--------|
| E01 SENT-101 | Docker infrastructure (Postgres, Redis, MailHog) |
| E01 SENT-102+ | Planned — API, auth, frontend |

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
| MailHog SMTP | 1025 | Used by app later |
| MailHog UI | 8025 | Open http://localhost:8025 in a browser |

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

- **Backend:** Python (FastAPI) — coming in SENT-102+
- **Database:** PostgreSQL 16 (Docker)
- **Queue:** Redis 7 (Docker)
- **Email (dev):** MailHog (Docker)
- **Frontend:** React + Vite — coming in SENT-106+

## Next implementation ticket

**SENT-102** — FastAPI project structure and health endpoint.
