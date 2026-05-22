# SentinelDesk — QA Testing Strategy

## 1. Purpose and scope

This document defines the testing approach for the SentinelDesk QA automation framework.
It covers what is tested, at which level, with which tools, and under what conditions.
It is a living document: each epic updates the relevant sections as new functionality is implemented.

**In scope:**
- API layer (FastAPI REST endpoints)
- Integration layer (API ↔ PostgreSQL, API ↔ Redis, API ↔ Celery, email via MailHog)
- E2E UI layer (React SPA via Selenium)
- Non-functional: performance practice (Locust, E11+) and security-adjacent (bug garden)

**Out of scope:**
- Unit tests — developer-owned; not part of this QA framework
- Frontend component tests (React Testing Library) — developer-owned
- Real production environments — local Docker stack only
- Load testing in CI — manual/local execution only

---

## 2. Test objectives

Following ISTQB principles, testing in this project aims to:

1. **Confirmation testing** — verify each implemented feature matches its acceptance criteria
2. **Defect detection** — find defects before they become embedded in downstream epics
3. **Integration validation** — verify cross-layer behaviour (API ↔ DB, worker ↔ DB, API ↔ MailHog)
4. **Regression confidence** — catch regressions as features evolve across epics
5. **Defect documentation** — record intentional bugs (bug garden) and practice the red → green cycle

---

## 3. Test pyramid

```text
               ┌──────────────┐
               │    E2E UI    │  Few — critical user paths only
               │   Selenium   │
          ┌────┴──────────────┴────┐
          │    Integration tests   │  Medium — API + DB assertions,
          │  API + DB + Celery     │  async job completion, email
     ┌────┴────────────────────────┴────┐
     │           API tests              │  Many — endpoint contracts,
     │    pytest + httpx (REST layer)   │  negative cases, RBAC, schema
     └──────────────────────────────────┘
Unit tests: developer-owned — outside QA framework scope
```

**Rationale:**
API tests are cheapest to write and run — no browser, no DB queries.
They should cover the most cases. Integration tests verify that the full stack behaves
correctly end-to-end at the HTTP + DB level. E2E tests cover critical user journeys only —
they are the most expensive and the most fragile.

---

## 4. Test levels

### 4.1 API tests (`tests/api/`)

| Attribute | Detail |
|-----------|--------|
| Scope | FastAPI route layer — HTTP contract, status codes, JSON schema, headers, RBAC |
| Tool | pytest + httpx (`api_client` fixture) |
| Gate fixture | `require_api` — skips if API is not reachable |
| Characteristics | No browser, no DB queries — pure HTTP in/out |
| Starts | SENT-102-QA; expands each epic |

### 4.2 Integration tests (`tests/integration/`)

| Attribute | Detail |
|-----------|--------|
| Scope | Cross-layer behaviour — API writes matched to DB state, Celery job completion, MailHog email capture, Redis state |
| Tool | pytest + httpx + psycopg2 + redis-py |
| Gate fixture | `require_infrastructure` — skips if Docker stack is down |
| Characteristics | Makes real DB queries to verify side effects; may poll for async completion |
| Starts | SENT-101-QA (infrastructure); SENT-202-QA (ingest + DB row) |

**Standard integration pattern (from ARCHITECTURE.md §4.3):**

```python
# Call API → assert DB state directly
resp = api_client.patch(f"/api/v1/alerts/{ALERT_001_ID}", json={"assigned_to": ANALYST_ID})
assert resp.status_code == 200
row = db_session.execute(select(Alert).where(Alert.id == ALERT_001_ID)).scalar_one()
assert row.assigned_to_id == ANALYST_ID
audit = db_session.execute(
    select(AuditLog).where(AuditLog.entity_id == ALERT_001_ID)
).scalar_one()
assert audit.action == "ALERT_ASSIGNED"
```

### 4.3 E2E tests (`tests/e2e/`)

| Attribute | Detail |
|-----------|--------|
| Scope | Full browser workflows — login, queue, alert detail, modals, playbook polling, email |
| Tool | Selenium 4 + WebDriver Manager + pytest; Page Object Model under `tests/e2e/pages/` |
| Gate | `require_infrastructure` + `require_api` + browser available |
| Characteristics | Slowest tier; critical paths only; always use `WebDriverWait`, never `time.sleep()` |
| Starts | SENT-303-QA (React frontend implemented) |

### 4.4 Performance tests (`tests/performance/`) — E11+

| Attribute | Detail |
|-----------|--------|
| Scope | Queue list p95 latency, ingest burst throughput |
| Tool | Locust |
| CI | Not included — manual/local execution against bulk-seeded dataset |
| Pass criteria | p95 < 500ms at 20 concurrent users on queue list; 100 ingest/min without 5xx |

---

## 5. Test types

| Type | Layer | Examples |
|------|-------|---------|
| Functional (positive) | API, integration, E2E | Login returns token, ingest returns 202, playbook completes |
| Functional (negative) | API | 401 without token, 403 wrong role, 409 duplicate `external_id`, 404 unknown path |
| Integration | integration/ | DB row created after POST, audit log written after PATCH, Celery updates `enrichment_status` |
| Regression | All layers | Full marker suite re-run after each epic |
| Bug verification | API, integration, E2E | `@pytest.mark.xfail` tests for BUG-001 through BUG-008 |
| Security-adjacent | API | RBAC bypass (BUG-004), webhook signature validation (BUG-006), login rate limit |
| Performance | performance/ | Locust queue and ingest scenarios |

---

## 6. Tooling

| Tool | Purpose | Status |
|------|---------|--------|
| pytest | Runner, fixtures, markers, parametrize | Active |
| httpx | Sync HTTP client for API and integration tests | Active |
| psycopg2-binary | Direct PostgreSQL queries in integration tests | Active |
| redis-py | Direct Redis checks in integration tests | Active |
| python-dotenv | Load `.env` into `os.environ` before tests | Active |
| ruff | Linting and formatting (replaces flake8 + isort + Black) | Active |
| Selenium 4 + WebDriver Manager | E2E browser automation | Planned (SENT-303-QA+) |
| pytest-asyncio | Async test support if async DB sessions are needed | Planned (E02+) |
| freezegun | Freeze time for dashboard timezone bug (BUG-007) | Planned (E08-QA) |
| Locust | Performance load testing | Planned (E11) |

**Not used:** `requests` (replaced by httpx), `flake8` (replaced by ruff),
`Black` (replaced by `ruff format`), `unittest` (pytest-native assertions preferred).

---

## 7. Test directory structure

```text
tests/
├── conftest.py              # All shared fixtures: gate fixtures, HTTP clients, DB clients
├── data/                    # Static test data files (never credentials from .env)
│   └── invalid_postgres.json
├── api/                     # HTTP contract tests — no direct DB queries
│   ├── __init__.py
│   └── test_health_endpoint.py
├── integration/             # Cross-layer tests: API + DB, async jobs, email
│   ├── __init__.py
│   └── test_infrastructure.py
├── e2e/                     # Browser tests — added in SENT-303-QA
│   ├── __init__.py
│   └── pages/               # Page Object Model classes
└── performance/             # Locust scenarios — added in E11
```

**Policy:** No `tests/` folders under `backend/` or `frontend/`.
All QA automation lives exclusively under the root `tests/`.

**Naming conventions:**

| Element | Convention | Example |
|---------|------------|---------|
| Test files | `test_<feature_or_module>.py` | `test_alert_ingest.py` |
| Test functions | `test_<verb>_<subject>_<condition>` | `test_ingest_alert_returns_202` |
| Page objects | `<PageName>Page` class | `LoginPage`, `AlertQueuePage` |
| Fixtures | `snake_case`, noun or noun phrase | `api_client`, `postgres_connection` |

---

## 8. Markers and selective execution

Markers are declared in `pytest.ini`. Use them to run subsets without modifying source files.

| Marker | Scope | When to use |
|--------|-------|------------|
| `api` | `tests/api/` | REST API tests requiring the live API service |
| `integ` | `tests/integration/` | Tests requiring the live Docker infrastructure stack |
| `e2e` | `tests/e2e/` | Browser tests requiring full stack + Selenium |
| `smoke` | Subset of api + integ | Minimal sanity check — health, connectivity, login |
| `reg` | All layers | Full regression suite — run before closing an epic |
| `bug` | Any layer | Tests targeting bug garden defects (paired with `xfail`) |
| `perf` | `tests/performance/` | Locust performance scenarios |
| `sec` | `tests/api/` | Security-adjacent API tests |

```powershell
pytest -m api                      # API tests only
pytest -m integ                    # Integration tests only
pytest -m "api or integ"           # All non-browser tests
pytest -m "integ and not bug"      # Integration, skip known failing bugs
pytest -m smoke                    # Quick sanity check
pytest -m bug --runxfail           # Run bug tests to check if any are now fixed
```

---

## 9. Test data management

Full reference: `docs/TEST_DATA.md`. Summary of rules:

**Stable seed IDs:**
Fixed UUIDs written by `scripts/seed.py`. Always use these constants in assertions.

| Constant | UUID | Used for |
|----------|------|---------|
| `ALERT_OPEN_HIGH` | `11111111-...01` | Default queue E2E |
| `ALERT_ESCALATED` | `11111111-...02` | Lead approval tests |
| `ALERT_FOR_PLAYBOOK` | `11111111-...03` | Async playbook run |
| `CASE_ACTIVE` | `22222222-...01` | Case detail navigation |
| `PLAYBOOK_ISOLATE` | `33333333-...01` | Run playbook modal |

**Reset before E2E suites** via the planned `clean_db` fixture (added in E10):

```python
# tests/conftest.py — added in E10 when reset API exists
@pytest.fixture(scope="function")
def clean_db(admin_api_client):
    """Reset database to seed state before each test."""
    admin_api_client.post("/api/v1/test/reset")
    yield
```

**Rules:**

1. Use seed UUIDs from `TEST_DATA.md` for assertions — never hardcode random UUIDs.
2. If a test creates data, delete it in teardown or call reset.
3. API tests should be read-only where possible; use function-scoped fixtures for write tests.
4. Never depend on data created by a previous test run.
5. Never use personal email addresses, phone numbers, or real credentials.

---

## 10. Bug garden strategy

All bugs in `docs/BUG_GARDEN.md` are intentional defects for QA practice.

**Workflow:**

1. Write a test that targets the bug — it will fail on a correct first run.
2. Mark it with `@pytest.mark.xfail(strict=True, reason="BUG-NNN: description")`.
3. The test is reported as `XFAIL` (expected failure), not `FAILED`.
4. When the bug is fixed, remove `@xfail` — it becomes a permanent regression guard.
5. Mark the bug `FIXED` in `BUG_GARDEN.md`.

```python
@pytest.mark.bug
@pytest.mark.api
@pytest.mark.xfail(
    strict=True,
    reason="BUG-001: severity filter ignores CRITICAL when combined with date range",
)
def test_severity_filter_with_date_range_returns_only_critical(api_client):
    response = api_client.get("/api/v1/alerts", params={"severity": "CRITICAL", "from": "..."})
    assert response.status_code == 200
    alerts = response.json()["items"]
    assert all(a["severity"] == "CRITICAL" for a in alerts)
```

`strict=True` means if the test unexpectedly passes (bug silently fixed), pytest reports
`XPASS` and fails the run — preventing untracked fixes.

---

## 11. Test environment

| Service | Port | Required by |
|---------|------|------------|
| PostgreSQL 16 | 5432 | Integration, E2E |
| Redis 7 | 6379 | Integration, E2E |
| FastAPI (API) | 8000 | API, integration, E2E |
| MailHog UI | 8025 | Integration (email assertions) |
| MailHog SMTP | 1025 | App only — not accessed directly by tests |
| React frontend | 5173 | E2E only |
| Mock SIEM | 8088 | Integration ingest tests (E02+) |
| Threat Intel embed | 8090 | E2E iframe tests (E04-QA+) |

**Start all services:**

```powershell
docker compose up -d
docker compose ps      # confirm no "Exit" status
```

---

## 12. Entry and exit criteria

### Entry criteria (before testing an epic)

- Implementation ticket is merged and the feature is deployed to local Docker.
- `docker compose ps` shows no stopped containers.
- `pytest -m smoke` passes with no failures.
- Seed data is in place (or `POST /api/v1/test/reset` succeeds when available).

### Exit criteria (before marking a QA ticket complete)

- All test cases in the QA ticket pass, or are `XFAIL` with a documented bug reference.
- No new ruff lint errors in `tests/` (`ruff check tests/`).
- Test output shows no unexpected `FAILED` or `ERROR` entries.
- New fixtures added to `conftest.py` include Google-style docstrings.

---

## 13. CI pipeline design

Local-first until E11. When CI is introduced:

```yaml
# Conceptual pipeline structure (GitHub Actions or equivalent)
jobs:
  lint:
    steps:
      - ruff check tests/
      - ruff format --check tests/

  api-and-integration:
    steps:
      - docker compose up -d
      - pytest -m "api or integ" --tb=short

  e2e:
    steps:
      - docker compose up -d
      - pytest -m e2e --tb=short  # headless Chrome
```

**Not in CI:** Performance tests (Locust), bug garden xfail tests (run on demand with `--runxfail`).

---

## 14. Session checklist

Run before any focused test session:

1. `docker compose up -d` — start all containers
2. `docker compose ps` — confirm no "Exit" status
3. `pytest -m smoke` — baseline health check
4. When available: `POST /api/v1/test/reset` — restore seed state
5. Open MailHog at http://localhost:8025 — clear inbox if email tests follow
6. Run targeted suite: `pytest -m api -v` or `pytest tests/integration/ -v`
