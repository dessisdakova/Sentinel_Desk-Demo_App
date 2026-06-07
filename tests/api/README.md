# tests/api/

HTTP contract tests — status codes, response bodies, and headers. No database queries, no browser.

## Prerequisites

The FastAPI service must be running:

```powershell
docker compose up -d
```

Tests skip automatically if the API is not reachable.

## Running

```powershell
pytest -m api -v
```

## Fixtures (conftest.py)

| Fixture | Scope | Description |
|---------|-------|-------------|
| `api_client` | session | httpx `Client` pointed at the FastAPI base URL |

`api_base_url` and `require_api` come from the root `tests/conftest.py`.
