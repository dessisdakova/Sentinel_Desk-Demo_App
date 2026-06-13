# tests/e2e/

End-to-end browser tests using Playwright. Full UI workflows using `page` fixtures. Require the React frontend running on port 5173. Added per page as the frontend is built.

## Prerequisites

```powershell
pip install -r requirements-test.txt
playwright install chromium          # first time only — downloads Chromium
docker compose up -d                 # API + DB + Redis
docker compose up -d --build         # OR rebuild containers after code changes
cd frontend && npm run dev           # Vite dev server on :5173 (browser tests)
```

## Running

```powershell
# All E2E tests (browser tests skip automatically if frontend is not running)
pytest tests/e2e -m e2e -v

# Login tests only
pytest tests/e2e/test_login_page.py -m e2e -v

# Smoke subset only
pytest tests/e2e -m "e2e and smoke" -v
```

### Watch the browser (headed mode)

```powershell
# Open a visible Chromium window for every test
pytest tests/e2e -m e2e --headed -v

# Slow down each action by 500 ms — useful for following what Playwright does
pytest tests/e2e -m e2e --headed --slowmo 500 -v

# Single test, headed + slow
pytest tests/e2e/test_login_page.py::test_valid_credentials_redirect_to_dashboard --headed --slowmo 500 -v
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
| `base_url` | session | React frontend root URL (`http://localhost:5173` by default) |
| `require_frontend` | session | Skips the test if the Vite dev server is not reachable on `:5173` |
| `login_page` | function | Navigates to `/login` and returns a ready `LoginPage` instance; implies `require_frontend` |

`browser`, `browser_context`, and `page` are provided automatically by `pytest-playwright`.

Root `tests/conftest.py` provides `require_api`, `require_infrastructure`, and the token fixtures (`analyst_token`, `lead_token`, `admin_token`) available to all layers including E2E.

## Page objects

Browser test helpers live in `pages/`. See [`pages/README.md`](pages/README.md).
