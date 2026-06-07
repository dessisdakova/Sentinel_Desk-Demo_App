# tests/e2e/

End-to-end tests using Playwright. This layer covers two use cases:

- **Playwright API tests** — use `playwright_api_context` to call the FastAPI service without a browser. Available now, before the React frontend exists.
- **Browser tests** — full UI workflows using `page` fixtures. Require the React frontend running on port 5173. Added per page as the frontend is built.

## Prerequisites

```powershell
pip install -r requirements-test.txt
playwright install chromium
docker compose up -d            # for all tests
cd frontend && npm run dev      # for browser tests only
```

## Running

```powershell
# Playwright API tests (no browser, no frontend needed)
pytest tests/e2e/test_health_api.py -m e2e -v

# All E2E tests (browser tests skip if frontend is not running)
pytest tests/e2e -m e2e -v

# Headed mode — watch the browser during a test run
pytest tests/e2e -m e2e --headed -v
```

## Debugging failures

When a browser test fails, Playwright saves a trace file automatically (configured in `pytest.ini`):

```powershell
playwright show-trace test-results/<test-name>/trace.zip
```

The trace viewer replays the test step-by-step with screenshots, network calls, and DOM snapshots.

## Key conventions

- **No `time.sleep()`** — Playwright auto-waits before every action.
- **`expect(locator)`** for UI assertions — retries automatically for up to 5 s.
- **`assert`** for non-UI values (status codes, JSON bodies).
- **Selectors**: prefer `page.get_by_test_id("x")` → `page.get_by_role(...)` → `page.locator("css")`.
- Every test in this folder must be marked `@pytest.mark.e2e`.
- Browser tests must declare `require_frontend` as a fixture parameter.

## Fixtures (conftest.py)

| Fixture | Scope | Description |
|---------|-------|-------------|
| `base_url` | session | React frontend root URL; used by the `page` fixture for relative navigation |
| `require_frontend` | session | Skips the test if the Vite dev server is not running |
| `playwright_api_context` | session | Playwright `APIRequestContext` pointed at the FastAPI service |

`browser`, `browser_context`, and `page` are provided automatically by `pytest-playwright`.

## Page objects

Browser test helpers live in `pages/`. See [`pages/README.md`](pages/README.md).
