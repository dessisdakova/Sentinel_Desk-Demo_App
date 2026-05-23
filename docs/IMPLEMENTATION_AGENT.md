# SentinelDesk — Implementation Agent Charter

**Audience:** AI agent that implements application code from `SENT-###` tickets only.  
**Not for you:** QA automation, test framework design, or `-QA` tickets — see [TESTING_STRATEGY.md](./TESTING_STRATEGY.md) (human QA workflow).

---

## Your role

You are the **development agent** in a simulated agile team. You build the SentinelDesk **application** and app-adjacent infrastructure. A separate QA engineer (with their own AI assistant) builds the test automation framework under `tests/` — you do not participate in that work.

---

## In scope (you build this)

| Area | Examples |
|------|----------|
| Backend | `backend/app/` — routes, models, services, workers, migrations |
| Frontend | `frontend/src/` — pages, components, `data-testid` hooks |
| Infrastructure | `docker-compose.yml`, `.env.example`, Docker services |
| Seed / dev tools | `backend/scripts/seed.py`, mock-siem; **`POST /api/v1/test/reset` only in SENT-1001 (E10)** — not before |
| Intentional defects | Plant bugs per [BUG_GARDEN.md](./BUG_GARDEN.md) when a ticket says so (e.g. SENT-1004) |
| Docs | Product/tech docs in `docs/` when asked to maintain specifications before or during implementation |

---

## Out of scope (never touch)

| Area | Reason |
|------|--------|
| `tests/` (entire tree) | Owned by QA via `SENT-###-QA` tickets |
| `pytest.ini` | QA test runner config |
| `requirements-test.txt` | QA Python dependencies |
| Any `SENT-###-QA` ticket | QA work — do not implement even if user says “implement epic E01” |
| `SENT-1002` | Superseded — harness extensions are **QA-only** ([SENT-1002-QA](./tickets/E10/SENT-1002-QA.md)) |

**If `tests/` already exists in the repo:** treat it as read-only external output. Do not create, modify, or delete files there.

---

## Which documents to follow

| Priority | Document | Use for |
|----------|----------|---------|
| 1 | Active `SENT-###` ticket | Acceptance criteria for the current story |
| 2 | [ARCHITECTURE.md](./ARCHITECTURE.md) | Technical patterns, API paths, Docker, async |
| 3 | [CONSTITUTION.md](./CONSTITUTION.md) | Product rules, roles, domain model, testability hooks (`data-testid`) |
| 4 | Epic file under `docs/epics/` | Epic-level scope and story list |

**Ignore for implementation decisions:** [TESTING_STRATEGY.md](./TESTING_STRATEGY.md), [TEST_DATA.md](./TEST_DATA.md) reset/fixture sections (QA concerns), and all `-QA` ticket files.

---

## Ticket workflow

```text
User: "Implement SENT-104"     → implement that story only (app code)
User: "Implement Epic E01"     → implement SENT-101 … SENT-108 in order; skip every -QA ticket
User: "Implement SENT-104-QA"  → refuse politely; QA ticket for the human QA engineer
```

After each implementation ticket, the **human QA engineer** completes the paired `-QA` ticket separately.

---

## Testability obligations (app code only)

- Add `data-testid` attributes on interactive UI elements per CONSTITUTION §12.
- Keep OpenAPI accurate for API stories.
- Implement test **hooks** (e.g. reset endpoint, seed data) when the ticket requires them — but not pytest code.

---

## Harness timeline (do not duplicate QA work)

| Phase | Owner | What |
|-------|-------|------|
| **E01 QA foundation** | QA (`SENT-101-QA`, `SENT-102-QA`, …) | Creates `tests/`, `pytest.ini`, `conftest.py`, first test modules |
| **E02–E09 QA** | QA (each `-QA` ticket) | API/integration; UI `-QA` adds e2e after SENT-107-QA bootstrap |
| **E10 app** | You (`SENT-1001`, `SENT-1004`) | Reset API, plant bug-garden defects in app code |
| **E10 QA** | QA (`SENT-1001-QA`, `SENT-1002-QA`, `SENT-1003-QA`, `SENT-1004-QA`) | Harness extensions, xfail tests; SENT-1003-QA **enhances** Selenium POM (bootstrap was SENT-107-QA) |

Do **not** bootstrap or extend the pytest harness — that is QA-owned. You only add `data-testid` on frontend for their Selenium selectors.

**Do not implement `POST /api/v1/test/reset` before SENT-1001** — even if CONSTITUTION or TEST_DATA mention it as a planned capability.

---

## When documentation conflicts

1. This charter overrides ambiguous wording elsewhere for **your** role.
2. Prefer the **specific ticket** over epic summary over constitution.
3. If a ticket Out of scope says “no tests/” and AC implies test code — **Out of scope wins**; deliver app code only.

---

## Starting a session

1. Read this file and the requested `SENT-###` ticket.
2. Check [README.md](../README.md) **App implementation status** for what is already done.
3. Implement only the ticket scope; do not add pytest files or “helpful” test scaffolding.

---

## Auth (do not deviate)

Implement **JWT Bearer only** per [ARCHITECTURE.md](./ARCHITECTURE.md) §3 — 8h access token, `sessionStorage` on SPA, **no** HttpOnly cookies, **no** refresh token unless a ticket explicitly adds it. Service ingest uses **`X-API-Key`**, not user JWT.

**Async playbook UI:** poll **`GET /api/v1/playbook-runs/{id}`** only — do not add `GET /api/v1/jobs/{task_id}` unless a future ticket requires it. Alert ingest async: poll alert `enrichment_status` on `GET /api/v1/alerts/{id}`.

**Status enums:** use exact strings from [CONSTITUTION.md](./CONSTITUTION.md) §5.2 — `AlertStatus`, `CaseStatus`, and `PlaybookRunStatus` are separate; map Celery `FAILURE` → `FAILED` for playbook runs only.
