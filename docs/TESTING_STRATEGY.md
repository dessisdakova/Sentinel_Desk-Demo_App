# SentinelDesk — QA Testing Strategy (for you)

This document maps **what to test** to **where in the app** — aligned with your priorities (E2E, API, integration first).

---

## 1. Test pyramid (your version)

```text
        ┌─────────────┐
        │  E2E UI     │  Selenium + pytest — critical paths
        │  (few)      │
        ├─────────────┤
        │ Integration │  API + DB + worker completion
        │  (medium)   │
        ├─────────────┤
        │ REST API    │  pytest + httpx — many cases
        │  (many)     │
        └─────────────┘
Unit tests: dev-owned — skip unless you experiment
```

---

## 2. Tooling (recommended)

| Tool | Purpose |
|------|---------|
| pytest | Runner, markers, fixtures |
| httpx or requests | API tests |
| Selenium 4 + WebDriver Manager | E2E browser |
| pytest-xdist | Optional parallel API tests |
| freezegun | Time-based dashboard tests (BUG-007) |
| MailHog API | Assert email without real SMTP |
| Locust (E11) | Performance practice |

---

## 3. Test layout (QA-owned — root `tests/` only)

**Policy:** No `tests/` folders under `backend/` or `frontend/`. Implementation agents do not add test files.

```text
tests/                    # created/evolved per SENT-###-QA tickets
├── conftest.py           # fixtures (reset, tokens) — SENT-1002 / 1002-QA
├── pytest.ini
├── api/
├── integration/
└── e2e/
    └── pages/            # Page Object Model
```

Work **ticket-by-ticket**: after `SENT-104` is implemented, complete `SENT-104-QA` before moving on (or in parallel if you prefer).

---

## 4. Priority test scenarios by module

### M1 Auth
- Login per role; forbidden pages return redirect or 403 page
- Token expiry handling (optional)

### M2 Ingest
- Ingest with API key → 202 → DB row → worker completes enrichment
- Duplicate external_id → 409

### M3 Queue
- Pagination: page 2 different from page 1
- Filter severity + date (BUG-001 when active)
- Bulk assign (BUG-002 when active)
- Sort by SLA

### M4 Alert detail
- Tab navigation; timeline events order
- Escalation approval by lead only (BUG-004)
- Iframe IOC param (BUG-008)

### M5 Cases
- Create, link alert, add note, close as lead

### M6 Playbooks
- Poll until success; handle FAILURE path (BUG-003)

### M7 Webhooks
- Delivery row after status change; retries on 500

### M8 Dashboard / Audit
- Metrics change after seed actions
- CSV export row count (BUG-005)

### M9 Admin
- Create user; rule applies tag on new ingest

### M11 Notifications
- MailHog receives escalation email

---

## 5. Non-functional (when ready)

| Scenario | Tool | Pass criteria (initial) |
|----------|------|-------------------------|
| Queue list with 10k alerts | Locust | p95 < 500ms at 20 users |
| Ingest burst | Locust | 100/min without 5xx |
| Login brute force | Manual/script | Document lack of rate limit (BUG candidate) |

---

## 6. Accessibility / visual (optional time)

- Spot-check: every `data-testid` button has `aria-label` (E11)
- Playwright screenshot compare — optional, not in MVP

---

## 7. Using AI for daily QA work (practice prompts)

| Task | Example prompt |
|------|----------------|
| Test cases from AC | “Generate pytest API tests from SENT-104 acceptance criteria” |
| Page Object | “Create Selenium POM for alert queue using data-testid list in CONSTITUTION” |
| Integration | “Write test: ingest alert then poll DB until enrichment_status=COMPLETE” |
| Bug report | “Given failing test bulk_assign, write Jira bug description” |
| Data setup | “Add curl commands to reset DB before e2e suite” |

---

## 8. CI (optional)

Local-first is fine. When adding CI:

- Job 1: `pytest tests/api tests/integration` (no browser)
- Job 2: `pytest tests/e2e` with headless Chrome
- Start services: `docker compose up -d` in pipeline

---

## 9. Session checklist before testing

1. `docker compose up -d`
2. `POST /api/v1/test/reset` (when available)
3. Confirm MailHog http://localhost:8025
4. Run targeted pytest marker: `pytest -m api`
