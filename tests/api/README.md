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

Seed persona HTTP checks (login + `/auth/me` for `tests/constants.py` users) live in `auth/test_login.py` and `auth/test_me.py` (SENT-104-QA). DB seed contract tests are in `tests/integration/infrastructure/test_seed_users.py` (SENT-108-QA).

## Fixtures (conftest.py)

| Fixture | Scope | Description |
|---------|-------|-------------|
| `api_session` | session | ``ApiSession`` — shared ``base_url`` + single ``httpx.Client`` |
| `auth_client` | session | ``AuthClient`` — login, me, logout (no default JWT) |
| `admin_client` | session | ``AdminClient`` — admin ping |
| `health_client` | session | ``HealthClient`` — health and routing probes |

API tests call **service client methods** (e.g. ``auth_client.login(...)``) — not raw URLs.
`api_base_url`, `require_api`, and token fixtures come from the root `tests/conftest.py`.
