# tests/

All QA automation for SentinelDesk lives here. No test files exist under `backend/` or `frontend/`.

## Structure

| Folder | Layer | Tool |
|--------|-------|------|
| `api/` | HTTP contract tests | pytest + httpx |
| `integration/` | Cross-layer tests (API + DB/Redis/MailHog) | pytest + psycopg2 + redis-py |
| `e2e/` | Browser and Playwright API tests | pytest + pytest-playwright |
| `secrets/` | LocalStack Secrets Manager seed + provider | boto3 |
| `environments/` | Per-target env files (`local.env`, …) | python-dotenv |
| `data/` | Static test data files | — |

## Prerequisites

```powershell
copy .env.example .env                  # first time only
docker compose up -d                    # start all services
python -m venv .venv                    # create virtual environment (Windows)
.venv\Scripts\Activate.ps1              # activate virtual environment (Windows)
pip install -r requirements-test.txt    # install requirements
playwright install chromium             # first time only
```

## Running tests

```powershell
pytest -m api -v                        # API tests only
pytest -m integ -v                      # integration tests only
pytest -m e2e -v                        # Playwright browser tests only
pytest -m e2e --headed -v               # open a visible Chromium window
pytest -m e2e --headed --slowmo 500 -v  # slow each action by 500 ms
pytest -m smoke -v                      # quick sanity (infra + health + core schema)
pytest -m reg -v                        # full regression suite
pytest -m "api or integ" -v             # everything except browser
pytest -v                               # all tests
```

Tests skip automatically with a clear message if the required service is not running — no configuration needed to run a subset.

## LocalStack (test secrets)

The Docker stack includes a **LocalStack** container that simulates AWS Secrets Manager. It supplies seed-user credentials and the JWT signing key to token fixtures — it is part of the **test harness only**, not the application.

Secrets are seeded automatically when LocalStack starts (`tests/secrets/init/01-seed-secrets.sh` reads `tests/secrets/seed_data.json`). To re-seed without restarting the container:

```powershell
python -m tests.secrets.bootstrap
```

Tests load connection settings from `tests/environments/local.env` (default `--env local` in `pytest.ini`). App settings still come from repo-root `.env` — you do not need to copy AWS variables into `.env`.

## Allure reports

`allure-pytest` (in `requirements-test.txt`) writes raw result files during pytest. View the HTML report with the Allure CLI in Docker — **no local Allure CLI or Java install required**.

1. Run tests with an output directory:

```powershell
pytest -m smoke -v --alluredir=allure-results
```

Append `--alluredir=allure-results` to any command in [Running tests](#running-tests) above.

Failing E2E tests attach Playwright screenshots and traces to Allure automatically (see `tests/e2e/conftest.py`).

2. Open the report (requires Docker):

```powershell
.\scripts\allure-serve.ps1              # live server at http://localhost:5050
.\scripts\allure-generate.ps1           # static HTML in allure-report/
```

On Linux/macOS, use `scripts/allure-serve.sh` and `scripts/allure-generate.sh` instead.

The first run pulls `andgineer/allure:2.32.0`. `allure-results/` and `allure-report/` are gitignored.

## Markers

Each test file sets **layer + regression** at the top:

```python
pytestmark = [pytest.mark.integ, pytest.mark.reg]  # or api / e2e
```

Add `@pytest.mark.smoke` only on individual tests that belong in the quick sanity subset. Smoke tests inherit `reg` from the module — no need to repeat it.

| Marker | Where to apply | Purpose |
|--------|----------------|---------|
| `api` / `integ` / `e2e` | Module `pytestmark` | Layer (which stack the test needs) |
| `reg` | Module `pytestmark` | Every test in the file is regression |
| `smoke` | Function decorator | Fast subset only |

## Shared fixtures

`conftest.py` at this level defines fixtures available to all layers:

- `require_infrastructure` — skips if the Docker stack is down
- `api_base_url` — FastAPI root URL (shared by API and E2E layers)
- `api_session` — shared `ApiSession` (`base_url` + one `httpx.Client`)
- `require_api` — skips if the API is not reachable or unhealthy
- `analyst_token` / `lead_token` / `admin_token` — session-scoped JWTs from seed login
- `expired_token` — function-scoped synthetically expired JWT (SENT-106-QA; signing key from Secrets Manager)

Layer-specific fixtures live in the child `conftest.py` files inside each subfolder.

**Integration:** `run_seed_script` (SENT-108-QA) runs `docker compose exec api python -m scripts.seed` inside tests that verify idempotent re-seeding.

## Seed baseline

API and integration tests that log in as seed users need DB rows from the app seed script — run once per session. See [Seed data](../README.md#seed-data-sent-108) in the root README and [docs/TEST_DATA.md](../docs/TEST_DATA.md) §3.1.

## Ruff (linting and formatting)

```powershell
ruff check tests/               # check for issues without changing files
ruff check --fix tests/         # fix issues automatically
ruff format tests/              # format files
```