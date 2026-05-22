"""Integration tests for local Docker infrastructure.

These tests verify that PostgreSQL, Redis, and MailHog are reachable when you run
``docker compose up -d``. They are **not** full end-to-end UI tests (those live
under ``tests/e2e/`` in later epics).

Difference from ``tests/api/``:
    - **integration (integ):** Direct clients (psycopg2, redis, httpx to MailHog UI).
    - **api:** HTTP calls to the SentinelDesk FastAPI service on port 8000.

Marker:
    Use ``@pytest.mark.integ`` on tests in this package.

Run:
    pytest -m integ -v
"""
