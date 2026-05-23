# Epic E10 — Test Harness & Bug Garden

**Epic key:** `SENT-E10`  
**Summary:** App test hooks (reset API, planted bugs) + QA harness extensions (fixtures, Selenium POM, xfail tests).  
**Business value:** Repeatable automation practice environment.

**Audience split:** Implementation agent → SENT-1001, SENT-1004 only ([IMPLEMENTATION_AGENT.md](../IMPLEMENTATION_AGENT.md)). QA engineer → all `-QA` tickets including SENT-1002-QA (no implement ticket).

**Prerequisite (QA):** E01 `-QA` foundation — `tests/`, `pytest.ini`, core `conftest.py` from SENT-101-QA / SENT-102-QA (CONSTITUTION §3.6).

---

## Acceptance criteria

### App (implementation agent)

- [ ] `POST /api/v1/test/reset` (admin, non-prod) — SENT-1001
- [ ] BUG-001 through BUG-008 planted in app code per BUG_GARDEN.md — SENT-1004

### QA harness (QA engineer only)

- [x] `tests/` structure: `api/`, `integration/`, `data/` (**E01 `-QA`** — do not recreate)
- [x] `pytest.ini` and E01 `conftest.py` fixtures (**E01 `-QA`** — do not recreate)
- [ ] Extend `conftest.py`: `admin_api_client`, `clean_db` — **SENT-1002-QA**
- [ ] Selenium POM standardized (Login, AlertQueue) — **SENT-1003-QA** (enhances bootstrap from SENT-107-QA)
- [ ] Example xfail tests for bug garden — **SENT-1004-QA**
- [ ] GitHub Actions optional (local-only OK)

---

## Stories

| Story key | Owner | Title |
|-----------|-------|-------|
| SENT-1001 | Implementation agent | Test reset endpoint |
| SENT-1002 | — | **Superseded** → [SENT-1002-QA](../tickets/E10/SENT-1002-QA.md) only |
| SENT-1003 | — | QA only → [SENT-1003-QA](../tickets/E10/SENT-1003-QA.md) (POM polish; bootstrap is SENT-107-QA) |
| SENT-1004 | Implementation agent | Plant bug garden (app defects) |

---

## QA notes

This epic is **for the QA engineer** — pair harness tickets with learning Selenium/pytest chapters. The implementation agent does not write or extend pytest code in E10.
