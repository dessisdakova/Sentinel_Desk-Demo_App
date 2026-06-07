# tests/

All QA automation for SentinelDesk lives here. No test files exist under `backend/` or `frontend/`.

## Structure

| Folder | Layer | Tool |
|--------|-------|------|
| `api/` | HTTP contract tests | pytest + httpx |
| `integration/` | Cross-layer tests (API + DB/Redis/MailHog) | pytest + psycopg2 + redis-py |
| `e2e/` | Browser and Playwright API tests | pytest + pytest-playwright |
| `data/` | Test data | — |

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
pytest -m api -v                # API tests only
pytest -m integ -v              # integration tests only
pytest -m e2e -v                # Playwright tests only
pytest -m smoke -v              # quick sanity (infra + health + core schema)
pytest -m reg -v                # full regression suite
pytest -m "api or integ" -v     # everything except browser
pytest -v                       # all tests
```

Tests skip automatically with a clear message if the required service is not running — no configuration needed to run a subset.

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
- `require_api` — skips if the API is not reachable or unhealthy

Layer-specific fixtures live in the child `conftest.py` files inside each subfolder.

## Ruff (linting and formatting)

```powershell
ruff check tests/               # check for issues without changing files
ruff check --fix tests/         # fix issues automaticall
ruff format tests/              # format files
```