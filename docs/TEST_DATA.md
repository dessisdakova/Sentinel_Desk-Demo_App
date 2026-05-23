# SentinelDesk — Test Data & Reset Guide

**Audience — QA engineer:** Primary reference for assertions, reset workflows, and stable IDs.  
**Audience — implementation agent:** Use seed personas and entity counts when implementing `seed.py` and reset API; do not create pytest code from this doc.

## 1. What “resettable test data” means (short version)

Automation needs the database to return to the **same starting picture** every run. SentinelDesk provides a **seed script** and a **reset API** so you never depend on leftover manual triage.

---

## 2. Seed personas (fixed — do not change without updating tests)

| Email | Password | Role | Display name |
|-------|----------|------|--------------|
| `analyst@demo.local` | `DemoPass123!` | ANALYST | Alex Analyst |
| `lead@demo.local` | `DemoPass123!` | LEAD | Jordan Lead |
| `admin@demo.local` | `DemoPass123!` | ADMIN | Sam Admin |

**Service account (ingest only):**

| Name | API Key (local only) |
|------|----------------------|
| `mock-siem` | `dev-ingest-key-change-in-prod` |

---

## 3. Stable entity IDs (canonical — do not change without updating tests)

**Two identifiers per seeded alert:**

| Field | Used for | Example |
|-------|----------|---------|
| **`id` (UUID)** | API paths (`/alerts/{id}`), DB assertions, E2E | `11111111-1111-4111-8111-111111111101` |
| **`external_id` (string)** | Ingest API, duplicate-key tests, SIEM correlation | `seed-edr-001` |

**QA constants** name the primary seed rows (use in tests and `seed.py`):

| Constant | UUID (`id`) | `external_id` | Purpose |
|----------|-------------|---------------|---------|
| `ALERT_OPEN_HIGH` | `11111111-1111-4111-8111-111111111101` | `seed-edr-001` | Default queue E2E; title *Suspicious PowerShell on WORKSTATION-12* |
| `ALERT_ESCALATED` | `11111111-1111-4111-8111-111111111102` | `seed-phish-002` | Lead approval tests; title *User reported phishing URL* |
| `ALERT_FOR_PLAYBOOK` | `11111111-1111-4111-8111-111111111103` | `seed-edr-playbook-003` | Async playbook run |
| `CASE_ACTIVE` | `22222222-2222-4222-8222-222222222201` | — | Case detail navigation |
| `PLAYBOOK_ISOLATE` | `33333333-3333-4333-8333-333333333301` | — | Run playbook modal |

**Implementation agent:** `backend/scripts/seed.py` must insert rows with exactly these UUIDs and `external_id` values for the three alert constants above.

### 3.1 Seed script — file path and run commands

| Context | Location |
|---------|----------|
| **Repo file** | `backend/scripts/seed.py` (package: `backend/scripts/__init__.py` + `seed.py`) |
| **Docker (api container)** | `docker compose exec api python -m scripts.seed` — WORKDIR `/app` = `backend/` |
| **Local (no Docker api)** | From repo root: `cd backend && python -m scripts.seed` |

`POST /api/v1/test/reset` (SENT-1001) re-runs the same seed logic — import or call shared functions from `backend/scripts/seed.py`, do not duplicate seed data elsewhere.

**Ingest samples (non-seed):** dynamic payloads may use other `external_id` values (e.g. `siem-demo-20260521-001` in `docs/tickets/E02/sample-ingest-payload.json`) — do not reuse seed `external_id` strings except to test duplicate `409`.

---

## 4. Seed dataset summary

After seed or reset:

| Entity | Count | Notes |
|--------|-------|-------|
| Users | 3 | +1 service account |
| Alerts | 12 | Mix of statuses/severities |
| Cases | 2 | One linked to 3 alerts |
| Playbooks | 3 | Isolate host, Notify owner, Escalate to lead |
| Webhook subscriptions | 1 | Points to mock SIEM callback |
| Audit log rows | ≥20 | Historical seed entries |
| Notifications | 2 | Sample email rows (not sent until triggered) |

---

## 5. How to reset (by phase)

### Before E10 — no reset API

Use **Option B (CLI seed)** or **Option C (nuclear volume reset)** below. The reset API does not exist until the app implements **SENT-1001**.

### After SENT-1001 — Option A (preferred for pytest)

```bash
# 1. Login as admin
curl -s -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@demo.local","password":"DemoPass123!"}'

# 2. Use access_token from response
curl -X POST http://localhost:8000/api/v1/test/reset \
  -H "Authorization: Bearer <access_token>"
```

### Option B — CLI seed (E01+; works before and after reset API)

```bash
docker compose exec api python -m scripts.seed
```

From repo root without the api container: `cd backend && python -m scripts.seed`

### Option C — Nuclear (fresh DB volume)

```bash
docker compose down -v
docker compose up -d
docker compose exec api alembic upgrade head
docker compose exec api python -m scripts.seed
```

---

## 6. Pytest fixture pattern (after SENT-1001 + SENT-1002-QA)

Not available before the reset API and `admin_api_client` fixture exist.

```python
# tests/conftest.py — add in SENT-1002-QA after SENT-1001 reset API ships
import pytest

@pytest.fixture(scope="function")
def clean_db(admin_api_client):
    admin_api_client.post("/api/v1/test/reset")
    yield
    # optional second reset for isolation
```

- **function scope:** each test starts clean (slower, safest for E2E).
- **session scope:** reset once before E2E suite (faster; tests must not mutate shared IDs).

---

## 7. Bulk data for performance practice (portfolio)

```bash
curl -X POST "http://localhost:8000/api/v1/dev/seed-bulk?count=10000" \
  -H "Authorization: Bearer <admin_token>"
```

Use for pagination/filter perf tests only — not for daily E2E.

---

## 8. MailHog verification

After escalating `ALERT_ESCALATED`:

1. Open http://localhost:8025  
2. Expect subject containing `Escalation` and recipient `@demo.local`  
3. No real domains required

---

## 9. Rules for writing tests

1. Use seed UUID constants and `external_id` values from **section 3 above** — never invent ad-hoc IDs (e.g. not `alert-seed-001`).  
2. If a test creates data, delete it or call reset in teardown.  
3. Never use your personal email or phone in tests.  
4. Parallel E2E: prefer separate docker stack per worker OR strict function-scoped reset.
