"""SentinelDesk automated test suite (QA-owned).

This package contains all pytest automation for the DemoApp project.
Application code under 'backend/' and 'frontend/' does **not** include tests;
developers focus on unit tests there, while QA owns everything under 'tests/'.

Directory layout:
    tests/
        conftest.py       Shared fixtures and helpers (loaded automatically by pytest).
        api/              HTTP/REST tests against the FastAPI app (marker: 'api').
        integration/      Tests that talk to real services (DB, Redis, MailHog; marker: 'integ').
        data/             Static JSON used for negative cases (not secrets from '.env').

How to run:
    pytest -m integ -v          # infrastructure integration tests only
    pytest -m api -v            # API tests only (requires API on port 8000)
    pytest -v                   # all tests

Prerequisites:
    1. Copy '.env.example' to '.env' at the repository root:

        copy .env.example .env

    2. Start Docker:

        docker compose up -d

    3. Create a virtual environment, activate it and install dependencies:

        python -m venv .venv
        .venv\Scripts\Activate.ps1
        pip install -r requirements-test.txt

Ruff (linting and formatting):
    1. Check for issues without changing files:

        ruff check tests/

    2. Fix issues automatically:

        ruff check --fix tests/

    3. Format files:

        ruff format tests/

See Also:
    docs/TESTING_STRATEGY.md: Overall test pyramid and tooling.
    docs/TEST_DATA.md: Stable seed IDs (used from E02 onward).
    pytest.ini: Markers and testpaths.
    pyproject.toml: Ruff lint + pydocstyle (Google).
"""
