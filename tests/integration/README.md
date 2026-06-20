# tests/integration/

Cross-layer tests that verify behaviour across the full Docker stack — database schema, Redis, MailHog, seed script side effects, and (in later epics) API writes matched against real DB state.

## Prerequisites

The full Docker stack must be running. For database schema tests (SENT-103-QA), migrations must be applied. For seed tests (SENT-108-QA), baseline users must be seeded at least once:

```powershell
docker compose up -d
docker compose exec api alembic upgrade head
docker compose exec api python -m scripts.seed
docker compose ps       # confirm no "Exit" status
```

Tests skip automatically if any required service is not reachable.

## Running

```powershell
pytest -m integ -v
pytest tests/integration/infrastructure/test_seed_users.py -v   # SENT-108-QA only
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
| `run_seed_script` | function | Runs `docker compose exec -T api python -m scripts.seed` (SENT-108-QA) |

`require_infrastructure` comes from the root `tests/conftest.py` and is a dependency of all fixtures above.

## Seed tests (SENT-108-QA)

`tests/integration/infrastructure/test_seed_users.py` asserts:

- Idempotent re-run does not duplicate seed emails (QA-108-1, QA-108-5)
- `inactive@demo.local` has `active = false` (QA-108-2)
- Password hashes are bcrypt (QA-108-3)
- Exactly four seed user rows exist (QA-108-4)

HTTP-level seed persona checks live in SENT-104-QA (`tests/api/auth/test_login.py`, `test_me.py`).
