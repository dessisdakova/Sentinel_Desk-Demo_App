# SENT-101-QA — Test: Docker Compose for Postgres, Redis, MailHog

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Status** | **Done** |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-101](./SENT-101.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Automated integration coverage for **SENT-101** — PostgreSQL, Redis, and MailHog via Docker Compose.

---

## Test cases

| ID | Scenario | Test function | Fixtures |
|----|----------|---------------|----------|
| QA-101-1 | Postgres accepts `SELECT 1` | `test_postgres_accepts_connection` | `postgres_connection` |
| QA-101-2 | Redis PING | `test_redis_responds_to_ping` | `redis_client` |
| QA-101-3 | MailHog UI HTTP 200 | `test_mailhog_ui_is_reachable` | `mailhog_ui_url` (+ `httpx.get`) |
| QA-101-4 | Wrong credentials → `OperationalError` | `test_postgres_rejects_invalid_credentials` | `invalid_postgres_settings` |

**Docker down:** Tests using `require_infrastructure` **skip** quickly. Invalid-credentials test **skips** if Postgres port is closed (`PORT_CHECK_TIMEOUT`).

---

## Artifacts

| Path | Purpose |
|------|---------|
| `requirements-test.txt` | pytest, psycopg2-binary, redis, httpx, python-dotenv, ruff |
| `pytest.ini` | Markers: `integ`, `api`, `e2e`, … |
| `pyproject.toml` | Ruff + Google pydocstyle |
| `tests/conftest.py` | `require_infrastructure`, DB/Redis/MailHog fixtures |
| `tests/integration/test_infrastructure.py` | **4** integration tests |
| `tests/data/invalid_postgres.json` | Wrong credentials for QA-101-2 |

---

## How to run

```powershell
docker compose up -d
pytest -m integ -v

docker compose down
pytest -m integ -v   # expect skips, ~few seconds, no hang
```

---

## Definition of Done

- [x] Tests run with `pytest -m integ`
- [x] Skip behavior when Docker is stopped
- [x] Matches [TESTING_STRATEGY.md](../../TESTING_STRATEGY.md)

---

## Completion

| Date | Notes |
|------|-------|
| 2026-05-21 | Initial automation |
| 2026-05-21 | Framework aligned: httpx for MailHog, 4 tests, Ruff/Google docstrings |

**Next:** [SENT-102-QA](./SENT-102-QA.md)
