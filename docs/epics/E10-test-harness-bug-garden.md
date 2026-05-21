# Epic E10 — Test Harness & Bug Garden

**Epic key:** `SENT-E10`  
**Summary:** pytest layout, reset endpoint, Selenium base fixtures, plant intentional bugs.  
**Business value:** Repeatable automation practice environment.

---

## Acceptance criteria

- [ ] `POST /api/v1/test/reset` (admin, non-prod)
- [ ] `tests/` structure: `api/`, `integration/`, `e2e/`
- [ ] `conftest.py` with `admin_api_client`, `clean_db` fixture
- [ ] Selenium: base page objects for Login, AlertQueue
- [ ] `pytest.ini` markers: `e2e`, `api`, `integration`, `bug`
- [ ] BUG-001 through BUG-008 planted per BUG_GARDEN.md
- [ ] Example xfail tests demonstrating failures
- [ ] GitHub Actions optional (local-only OK)

---

## Stories

| Story key | Title |
|-----------|-------|
| SENT-1001 | test reset endpoint |
| SENT-1002 | pytest api + integration samples |
| SENT-1003 | Selenium conftest + Login/Queue POM |
| SENT-1004 | Plant bug garden + xfail tests |

---

## QA notes

This epic is **for you** — pair with learning Selenium/pytest chapters.
