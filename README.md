# SentinelDesk (DemoApp)

**SecOps Alert Triage Portal** — a QA practice platform for E2E, API, and integration testing.

## Status

📋 **Specification phase** — no application code yet. Start with the constitution and epics.

## Documentation map

| Document | Purpose |
|----------|---------|
| [docs/CONSTITUTION.md](docs/CONSTITUTION.md) | Product vision, modules, pages, roles, NFRs |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Technical design, Docker, APIs, async |
| [docs/TEST_DATA.md](docs/TEST_DATA.md) | Seed users, stable IDs, **reset guide** |
| [docs/TESTING_STRATEGY.md](docs/TESTING_STRATEGY.md) | How you will test by layer |
| [docs/BUG_GARDEN.md](docs/BUG_GARDEN.md) | Intentional defects |
| [docs/epics/README.md](docs/epics/README.md) | Implementation epics E01–E11 |
| [docs/tickets/](docs/tickets/) | Implementation + QA tickets per epic (E01–E11) |

## Tech Stack

- **Product:** SecOps alert triage (#1), security-themed
- **Backend:** Python (FastAPI)
- **Database:** PostgreSQL via **Docker**
- **Email:** MailHog (free, local)
- **Roles:** Analyst, Lead, Admin
- **Async:** Celery + Redis, polling UI, webhooks

## Prerequisites (when implementing)

- Docker Desktop
- Python 3.12+
- Node.js 20+ (frontend)

