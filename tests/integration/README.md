# tests/integration/

Cross-layer tests that verify behaviour across the full Docker stack — API writes matched against real DB state, Redis checks, and MailHog email capture.

## Prerequisites

The full Docker stack must be running:

```powershell
docker compose up -d
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
| `redis_client` | session | redis-py `Redis` instance |
| `mailhog_ui_url` | session | MailHog web UI base URL |

`require_infrastructure` comes from the root `tests/conftest.py` and is a dependency of all fixtures above.
