"""SentinelDesk automated test suite (QA-owned).

This package contains all pytest automation for the DemoApp project.
Application code under ``backend/`` and ``frontend/`` does **not** include tests;
developers focus on unit tests there, while QA owns everything under ``tests/``.

Directory layout:
    tests/
        conftest.py       Shared fixtures and helpers (loaded automatically by pytest).
        api/              HTTP/REST tests against the FastAPI app (marker: ``api``).
        integration/      Tests that talk to real services (DB, Redis, MailHog; marker: ``integ``).
        data/             Static JSON used for negative cases (not secrets from ``.env``).

How to run:
    pytest -m integ -v          # infrastructure integration tests only
    pytest -m api -v            # API tests only (requires API on port 8000)
    pytest -v                   # all tests

Prerequisites:
    Copy ``.env.example`` to ``.env`` at the repository root, then start Docker::

        docker compose up -d

See Also:
    docs/TESTING_STRATEGY.md: Overall test pyramid and tooling.
    docs/TEST_DATA.md: Stable seed IDs (used from E02 onward).
    pytest.ini: Markers and ``testpaths``.
"""
