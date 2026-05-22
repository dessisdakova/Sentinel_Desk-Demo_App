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

## Test cases

| ID | Scenario | Test function | AC / notes |
|----|----------|---------------|------------|
| QA-102-1 | `GET /health` → 200, `{"status":"ok"}` | `test_health_returns_200_and_verify_response` | AC1 |
| QA-102-1 / AC3 | `X-Request-ID` sent and echoed in response header | Same test | AC3 |
| QA-102-2 | Unknown path → 404 | `test_unknown_path_returns_404` | API contract (ticket listed as integration; implemented as **api**) |

**AC2 (Docker):** Verified via `require_api` (TCP + `GET /health`) and running `docker compose`.

---

## Artifacts

| Path | Purpose |
|------|---------|
| `tests/api/test_health_endpoint.py` | **2** API tests |
| `tests/conftest.py` | API fixtures section |

---

## How to run

```powershell
docker compose up -d
pytest -m api -v
```

With API stopped: tests depending on `require_api` / `api_client` **skip** quickly.

---

## Definition of Done

- [x] Tests run with `pytest -m api`
- [x] AC1, AC3, QA-102-2 covered in current test file
- [x] Matches [TESTING_STRATEGY.md](../../TESTING_STRATEGY.md)

---

## Completion

| Date | Notes |
|------|-------|
| 2026-05-21 | 2 tests; AC1+AC3 combined in `test_health_returns_200_and_verify_response` |

**Next:** [SENT-103-QA](./SENT-103-QA.md)
