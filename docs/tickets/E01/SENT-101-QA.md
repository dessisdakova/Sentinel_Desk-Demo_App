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

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [x] Implementation ticket **SENT-101** is complete and runnable
- [x] `copy .env.example .env` and `docker compose up -d` for passing (non-skip) runs
- [x] `pip install -r requirements-test.txt` in project venv

---

## Test scope

- **integration** — `tests/integration/`
- **fixtures** — `tests/conftest.py`
- **negative test data** — `tests/data/invalid_postgres.json`

---

## Test cases

| ID | Layer | Scenario | Implemented as | Result |
|----|-------|----------|----------------|--------|
| QA-101-1 | integration | Postgres, Redis, MailHog healthy when Docker is up | `test_postgres_accepts_connection`, `test_redis_responds_to_ping`, `test_mailhog_ui_is_reachable` | Pass (with stack up) |
| QA-101-2 | integration | Wrong DB credentials fail correctly | `test_postgres_rejects_invalid_credentials` + `invalid_postgres.json` | Pass (or skip if Postgres port closed) |
| QA-101-3 | integration | Config matches documented local defaults | `test_local_settings_match_documented_defaults` | Pass (with stack up) |

**QA-101-3 note (SENT-101 scope):** `TEST_DATA.md` stable UUIDs and seed rows are **not** applicable until the app seed script exists. Covered later in **SENT-206-QA** / **SENT-1001-QA**. For this ticket, QA-101-3 means `.env` / fixture values align with `.env.example` and README defaults.

**Docker down behavior:** Tests that depend on `require_infrastructure` **skip** quickly (no hang). Invalid-credentials test **skips** if Postgres port is not open.

---

## Artifacts created

| Path | Purpose |
|------|---------|
| `requirements-test.txt` | pytest, psycopg2-binary, redis, httpx, requests, python-dotenv |
| `pytest.ini` | `testpaths`, markers (`integ`, `api`, `e2e`, …) |
| `tests/conftest.py` | `require_infrastructure`, DB/Redis/MailHog fixtures, fast port checks |
| `tests/integration/test_infrastructure.py` | Five integration tests (see table above) |
| `tests/data/invalid_postgres.json` | Wrong credentials for QA-101-2 (not in `.env`) |

---

## How to run

```powershell
# Infrastructure up → expect passes
docker compose up -d
pytest -m integ -v

# Infrastructure down → expect skips (fast), not a hang
docker compose down
pytest -m integ -v
```

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md) — referenced for **future** seed/UUID checks; not used in SENT-101-QA assertions
- [.env.example](../../../.env.example) — source of truth for QA-101-3 defaults

---

## Out of scope

- Fixing application bugs (file defects under BUG_GARDEN if found)
- Adding tests under `backend/` or `frontend/`
- FastAPI `/health`, auth tokens (SENT-102-QA onward)

---

## Definition of Done

- [x] Tests run with `pytest -m integ` (marker `integ` in `pytest.ini`)
- [x] No dependency on manual data unless documented in test docstring
- [x] Test file paths documented in this ticket (see **Artifacts created**)
- [x] Skip behavior when Docker is stopped (no indefinite hang)

---

## Completion

| Date | Notes |
|------|-------|
| 2026-05-21 | QA automation implemented; ticket marked Done |

**Next:** [SENT-102](./SENT-102.md) (FastAPI health) → [SENT-102-QA](./SENT-102-QA.md)
