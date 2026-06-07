# tests/integration/

Cross-layer tests that verify behaviour across the full Docker stack — database schema, Redis, MailHog, and (in later epics) API writes matched against real DB state.

## Prerequisites

The full Docker stack must be running. For database schema tests (SENT-103-QA), migrations must be applied:

```powershell
docker compose up -d
docker compose exec api alembic upgrade head
docker compose ps       # confirm no "Exit" status
```

Tests skip automatically if any required service is not reachable.

## Running

```powershell
pytest -m integ -v
```

## Fixtures (conftest.py)

| Fixture | Scope | Description |
|---------|-------|-------------|
| `postgres_settings` | session | Connection kwargs for PostgreSQL from `.env` |
| `invalid_postgres_settings` | session | Wrong credentials loaded from `tests/data/invalid_postgres.json` |
| `postgres_connection` | function | Fresh psycopg2 connection per test; closed after each test |
| `postgres_write_connection` | function | Same connection; **rolls back** after INSERT/UPDATE tests so no data persists |
| `redis_client` | session | redis-py `Redis` instance |
| `mailhog_ui_url` | session | MailHog web UI base URL |

`require_infrastructure` comes from the root `tests/conftest.py` and is a dependency of all fixtures above.
