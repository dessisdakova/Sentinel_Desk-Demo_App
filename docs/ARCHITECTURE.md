# SentinelDesk — Technical Architecture

**Audience — implementation agent:** Primary technical reference for `SENT-###` tickets. Read with [IMPLEMENTATION_AGENT.md](./IMPLEMENTATION_AGENT.md).  
**Audience — QA engineer:** Use integration-test patterns in §4.3 when writing `-QA` tickets.

Companion to [CONSTITUTION.md](./CONSTITUTION.md).

---

## 1. Architectural style

**Modular monolith** split into two deployable units for local dev:

- **API monolith** (FastAPI): all business logic, auth, persistence, job enqueue
- **SPA** (React): BFF-less; talks to API directly with CORS

No Kubernetes required. **Docker Compose** orchestrates API, worker, DB, Redis, MailHog, mock SIEM, and iframe embed host.

```mermaid
sequenceDiagram
  participant SIEM as Mock SIEM
  participant API as FastAPI
  participant Q as Redis Queue
  participant W as Celery Worker
  participant DB as PostgreSQL
  participant UI as React SPA
  participant MH as MailHog

  SIEM->>API: POST /alerts/ingest
  API->>DB: INSERT alert (NEW)
  API->>Q: enqueue enrich_alert
  API-->>SIEM: 202 Accepted
  W->>Q: dequeue
  W->>DB: UPDATE enrichment, SLA
  UI->>API: GET /alerts?status=NEW
  API->>DB: SELECT with filters
  UI->>API: PATCH /alerts/{id}
  API->>DB: UPDATE + audit log
  W->>MH: SMTP notify on ESCALATED
```

---

## 2. Backend layers (FastAPI)

| Layer | Responsibility | Test focus |
|-------|----------------|------------|
| `api/routes` | HTTP, status codes, auth deps | API tests |
| `schemas` | Request/response validation | contract / negative tests |
| `services` | Business rules, state transitions | integration tests |
| `models` | SQLAlchemy entities | DB assertions |
| `workers` | Side effects, retries | async integration |
| `core/config` | Settings from env | — |

**Rule:** Routes stay thin; no business logic in route handlers beyond orchestration.

---

## 3. Authentication & authorization

**Auth contract (canonical — do not mix cookie sessions or refresh tokens in E01):**

| Aspect | Choice |
|--------|--------|
| Token type | JWT **access token** only (HS256, `JWT_SECRET`) |
| Lifetime | **8 hours** — `JWT_EXPIRE_HOURS=8` in `.env`; login returns `expires_in` seconds (28800) |
| Transport | `Authorization: Bearer <access_token>` on API calls |
| SPA storage | In-memory React state + `sessionStorage` key `sentinel_access_token` |
| Refresh token | **Out of scope** until a future ticket explicitly adds it |
| Cookies | **Not used** for auth in this project (no HttpOnly session cookie) |
| Ingest / service | Separate **`X-API-Key`** header — not the user JWT |

### 3.1 Flow

1. `POST /api/v1/auth/login` with email/password → returns JWT access token + `expires_in` (seconds).
2. SPA stores token in memory + `sessionStorage` (`sentinel_access_token`); clears both on logout.
3. Each API request: `Authorization: Bearer <token>`.
4. FastAPI dependency `require_roles(["ANALYST"])` enforces RBAC from JWT claims.

### 3.2 Test users (seed)

See [TEST_DATA.md](./TEST_DATA.md).

### 3.3 Test-only endpoints

| Endpoint | Guard | When implemented |
|----------|-------|------------------|
| `POST /api/v1/test/reset` | `ADMIN` + `ENVIRONMENT != production` | **E10 / SENT-1001** — spec only until then |
| `POST /api/v1/dev/seed-bulk` | `ADMIN` + non-prod | **E11** |

**Implementation agent:** Do not add these routes before their tickets. QA uses CLI seed (`backend/scripts/seed.py`) until reset API exists.

---

## 4. Database (PostgreSQL)

### 4.1 Connection

- URL: `postgresql+asyncpg://sentinel:sentinel@localhost:5432/sentineldesk`
- Sync URL for Alembic: `postgresql://...`
- Migrations: Alembic only; no manual SSMS schema edits.

### 4.2 Indexing (performance-ready)

| Table | Index |
|-------|-------|
| `alerts` | `(status, severity, created_at DESC)` |
| `alerts` | `(assigned_to_id)` |
| `audit_logs` | `(created_at DESC)` |
| `webhook_deliveries` | `(subscription_id, created_at)` |

### 4.3 Integration test pattern

All tests live under repository root `tests/` (see CONSTITUTION §3.5). Example:

```python
# Pseudo-pattern — tests/integration/test_triage.py
def test_assign_alert_persists(client, db_session, analyst_token):
    resp = client.patch(f"/api/v1/alerts/{ALERT_001_ID}", json={"assigned_to": ANALYST_ID}, headers=auth(analyst_token))
    assert resp.status_code == 200
    row = db_session.get(Alert, ALERT_001_ID)
    assert row.assigned_to_id == ANALYST_ID
    audit = db_session.query(AuditLog).filter_by(entity_id=ALERT_001_ID).one()
    assert audit.action == "ALERT_ASSIGNED"
```

---

## 5. Async processing (Celery + Redis)

### 5.1 Tasks

| Task | Trigger | Duration (simulated) |
|------|---------|----------------------|
| `enrich_alert` | After ingest | 1–3 sec |
| `run_playbook` | User clicks Run | 2–5 sec per step |
| `deliver_webhook` | Alert status change | HTTP with retries |
| `send_email` | Escalation, assignment | SMTP → MailHog |

### 5.2 Async status — what to poll (canonical)

Do **not** expose a generic `GET /api/v1/jobs/{task_id}` for playbooks. Use domain endpoints only:

| Feature | Client polls | Status field / values | Terminal |
|---------|--------------|------------------------|----------|
| **Playbook run** | `GET /api/v1/playbook-runs/{id}` | `status`: `PENDING` → `RUNNING` → `SUCCESS` \| `FAILED` | `SUCCESS`, `FAILED` |
| **Alert enrichment** (ingest) | `GET /api/v1/alerts/{id}` | `enrichment_status`: `PENDING` → `COMPLETE` | `COMPLETE` |

**PlaybookRun `status` enum (API + DB + UI):** `PENDING`, `RUNNING`, `SUCCESS`, `FAILED` — never use Celery’s `FAILURE` in public JSON.

**Internal:** Celery `task_id` may be stored on `playbook_runs` for worker wiring — not returned to SPA and not a separate poll URL in E06.

**Enum separation:** Do not reuse status strings across entities — see [CONSTITUTION.md](./CONSTITUTION.md) §5.2 (`AlertStatus`, `CaseStatus`, `PlaybookRunStatus`).

**SPA playbook modal:** poll `GET /api/v1/playbook-runs/{playbook_run_id}` every 2s until terminal (see SENT-604).

### 5.3 Flakiness guidance for QA

- Prefer **explicit waits** on `data-testid="playbook-run-status-success"` with timeout 30s.
- Do not use `time.sleep(5)` fixed; use Selenium `WebDriverWait`.
- For API integration: poll `GET /api/v1/playbook-runs/{id}` or query `playbook_runs.status` in DB.

---

## 6. Frontend architecture (React)

| Concern | Choice |
|---------|--------|
| Routing | React Router v6 |
| Server state | TanStack Query (polling for queue + jobs) |
| Tables | TanStack Table + server-side pagination |
| Forms | React Hook Form + Zod |
| Dates | react-day-picker in filter bar |
| Modals | Headless UI or Radix Dialog |
| Iframe tab | Native `<iframe src="http://localhost:8090/embed?ioc=...">` |

### 6.1 Page ↔ API mapping

| Page | Main endpoints |
|------|----------------|
| Dashboard | `GET /api/v1/metrics/summary?from=&to=` |
| Alert queue | `GET /api/v1/alerts?page&size&filters` |
| Alert detail | `GET /api/v1/alerts/{id}`, `GET /api/v1/alerts/{id}/events` |
| Cases | `GET/POST/PATCH /api/v1/cases` |
| Playbooks | `GET /api/v1/playbooks`, `POST /api/v1/playbooks/{id}/run`, poll `GET /api/v1/playbook-runs/{id}` |
| Audit | `GET /api/v1/audit` |
| Admin | `GET/POST /api/v1/admin/*` |

---

## 7. External integrations (all local, free)

| Service | Port | Purpose |
|---------|------|---------|
| Mock SIEM | 8088 | Scripts POST sample alerts on timer |
| Threat intel embed | 8090 | Static HTML in iframe (fake VirusTotal-style) |
| MailHog SMTP | 1025 | Receive emails |
| MailHog UI | 8025 | QA verifies email content |

---

## 8. Docker Compose services

```yaml
# Conceptual — actual file created in E01
services:
  postgres:    # 5432
  redis:       # 6379
  api:         # 8000
  worker:      # celery
  frontend:    # 5173 (dev) or nginx 80 (optional)
  mailhog:     # 8025, 1025
  mock-siem:   # 8088
  intel-embed: # 8090
```

**Developer without Docker:** possible but unsupported in constitution; install Postgres + Redis locally and run processes manually.

---

## 9. Configuration (.env)

| Variable | Example | Notes |
|----------|---------|-------|
| `ENVIRONMENT` | `local` | `production` disables test reset |
| `DATABASE_URL` | postgresql+asyncpg://... | |
| `REDIS_URL` | redis://localhost:6379/0 | |
| `JWT_SECRET` | change-me | HS256 signing key |
| `JWT_EXPIRE_HOURS` | `8` | Access token lifetime; `expires_in` = hours × 3600 |
| `SMTP_HOST` | mailhog | |
| `SMTP_PORT` | 1025 | |
| `WEBHOOK_SIGNING_SECRET` | dev-secret | HMAC on outbound payloads |

---

## 10. API surface (version 1 summary)

Full OpenAPI generated at runtime. Grouped below for test planning.

### 10.1 Auth

- `POST /api/v1/auth/login`
- `POST /api/v1/auth/logout`
- `GET /api/v1/auth/me`

### 10.2 Alerts

- `POST /api/v1/alerts/ingest` (API key or service token)
- `GET /api/v1/alerts` (filters, pagination)
- `GET /api/v1/alerts/{id}`
- `PATCH /api/v1/alerts/{id}` (status, assignee, severity)
- `POST /api/v1/alerts/bulk` (bulk assign/disposition)
- `GET /api/v1/alerts/{id}/events`

### 10.3 Cases

- `GET /api/v1/cases`
- `POST /api/v1/cases`
- `GET /api/v1/cases/{id}`
- `PATCH /api/v1/cases/{id}`
- `POST /api/v1/cases/{id}/notes`
- `POST /api/v1/cases/{id}/alerts` (link)

### 10.4 Playbooks

- `GET /api/v1/playbooks`
- `POST /api/v1/playbooks/{id}/run` → `{ "playbook_run_id", "status": "PENDING" }`
- `GET /api/v1/playbook-runs/{id}` → `{ "status": "PENDING|RUNNING|SUCCESS|FAILED", "steps_completed", ... }`

No generic `/api/v1/jobs/{task_id}` in E06 — see ARCHITECTURE §5.2.

### 10.5 Webhooks (admin)

- `CRUD /api/v1/admin/webhooks`
- `GET /api/v1/admin/webhook-deliveries`

### 10.6 Audit & metrics

- `GET /api/v1/audit`
- `GET /api/v1/metrics/summary`

### 10.7 Test/dev

- `POST /api/v1/test/reset`
- `POST /api/v1/dev/seed-bulk?count=N`

---

## 11. Security notes (for later security testing practice)

- Passwords hashed with bcrypt
- Service ingest uses `X-API-Key` separate from user JWT
- Outbound webhooks signed with `X-Sentinel-Signature: sha256=...`
- CORS allowed only for `http://localhost:5173`

**Bug garden may include:** missing rate limit on login, verbose error leakage — documented, not fixed initially.

---

## 12. Observability (local)

- Structured JSON logs to stdout (`request_id`, `user_id`)
- Optional: correlation id header `X-Request-ID` for tracing one ingest → webhook chain in integration tests

---

## 13. Sample file references

| File | Purpose |
|------|---------|
| [TEST_DATA.md](./TEST_DATA.md) | Seed IDs, reset instructions |
| [BUG_GARDEN.md](./BUG_GARDEN.md) | Intentional defects |
| [epics/README.md](./epics/README.md) | Epic index |
| [tickets/E01–E11/](./tickets/) | Implementation and QA tickets per epic |
