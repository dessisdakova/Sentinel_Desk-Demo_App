# SENT-102-QA — Test: FastAPI project structure and health endpoint

| Field | Value |
|-------|-------|
| **Type** | Test Story |
| **Status** | **Done** |
| **Epic** | SENT-E01 Platform Foundation |
| **Priority** | High |
| **Labels** | `qa`, `automation` |
| **Implements after** | [SENT-102](./SENT-102.md) |
| **Test location** | Repository root `tests/` **only** |

---

## Summary

Automated API coverage for **SENT-102** — `GET /health`, negative path, env contract, and AC3 `X-Request-ID`.

---

## Description

**As a** QA engineer  
**I want** automated coverage for this story  
**So that** regressions are caught before later epics build on this behavior

---

## Prerequisites

- [x] Implementation ticket **SENT-102** is complete and runnable
- [x] `docker compose up -d` (API on port 8000)
- [x] `.env` includes `API_BASE_URL=http://localhost:8000`

---

## Test scope

| Layer | Location | Used in this ticket |
|-------|----------|---------------------|
| **api** | `tests/api/` | All tests below |
| **integration** | `tests/integration/` | Not used (QA-102-2 implemented as API 404 test) |

---

## Test cases

| ID | Layer | Scenario | Implemented as | AC |
|----|-------|----------|----------------|-----|
| QA-102-1 | api | Health 200 + JSON body | `test_health_returns_200` | AC1 |
| QA-102-1 / AC3 | api | `X-Request-ID` present and echoed | Same test (custom header) | AC3 |
| QA-102-2 | api | Unknown path → 404 | `test_unknown_path_returns_404` | — |
| QA-102-3 | api | `API_BASE_URL` + `API_PORT` match documented defaults | `test_api_base_url_matches_documented_default` | — |

**QA-102-3 note:** Validates `.env` / `documented_local_defaults` (see `tests/conftest.py`), not `TEST_DATA.md` seed UUIDs (E02+).

**AC2 (Docker API service):** Verified operationally via `require_api` fixture + `docker compose`; not a separate pytest assertion.

---

## Artifacts

| Path | Purpose |
|------|---------|
| `tests/api/test_health_endpoint.py` | Three API tests |
| `tests/conftest.py` | `api_base_url`, `api_port`, `require_api`, `api_client` |

---

## How to run

```powershell
docker compose up -d
pytest -m api -v
# or
pytest tests/api/test_health_endpoint.py -v
```

With API stopped: tests using `require_api` skip quickly.

---

## Test data

- [TEST_DATA.md](../../TEST_DATA.md) — not used for assertions in this ticket
- [.env.example](../../../.env.example) — `API_BASE_URL`, `API_PORT`

---

## Out of scope

- Fixing application bugs (file defects under BUG_GARDEN if found)
- Adding tests under `backend/` or `frontend/`
- Log file assertions for `request_id=` in stdout (AC3 logs — manual/ops check optional)

---

## Definition of Done

- [x] Tests run with `pytest -m api`
- [x] No dependency on manual data unless documented in test docstring
- [x] Test file paths documented in this ticket
- [x] AC1, AC3, QA-102-2, QA-102-3 covered

---

## Completion

| Date | Notes |
|------|-------|
| 2026-05-21 | 3 tests passing; AC3 covered via `X-Request-ID` echo in `test_health_returns_200` |

**Next:** [SENT-103](./SENT-103.md) → [SENT-103-QA](./SENT-103-QA.md)
