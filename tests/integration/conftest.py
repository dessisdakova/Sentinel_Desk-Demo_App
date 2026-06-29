import base64
import json
import subprocess
from pathlib import Path

import psycopg2
import pytest
import redis

from tests.conftest import (
    _env,
    _postgres_connect_kwargs,
    _redis_connect_kwargs,
)
from tests.constants import CLIENT_TIMEOUT_SEC
from tests.support.db.inspector import PostgresInspector


def _decode_jwt_payload(token: str) -> dict:
    """Decode the payload segment of a JWT without verifying the signature.

    :param token: Raw JWT string (three base64url segments joined by '.').
    :return: Deserialized payload dictionary.
    """
    payload_segment = token.split(".")[1]
    # base64url uses '-' and '_'; standard base64 uses '+' and '/'.
    # Add '==' padding — base64.b64decode ignores extra padding.
    padded = payload_segment.replace("-", "+").replace("_", "/") + "=="
    return json.loads(base64.b64decode(padded).decode())


@pytest.fixture(scope="session")
def postgres_settings() -> dict:
    """Valid PostgreSQL connection settings read from ``.env``.

    :return: Dictionary of keyword arguments suitable for ``psycopg2.connect()``.
    """
    return _postgres_connect_kwargs()


@pytest.fixture(scope="session")
def invalid_postgres_settings() -> dict:
    """Intentionally wrong PostgreSQL credentials for negative testing.

    Loaded from ``tests/data/invalid_postgres.json`` so the bad credentials
    are never hardcoded in the test itself.

    :return: Dictionary of keyword arguments with wrong user/password values.
    """
    path = Path(__file__).parent.parent / "data" / "invalid_postgres.json"
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    data["port"] = int(data["port"])
    return data


@pytest.fixture(scope="function")
def postgres_connection(
    postgres_settings,
    require_infrastructure,
) -> psycopg2.extensions.connection:
    """Open one PostgreSQL connection for a single test function.

    :param postgres_settings: Valid connection kwargs from ``.env``.
    :param require_infrastructure: Gate fixture — skips if Docker is down.
    :yield: Open ``psycopg2`` connection; closed automatically after the test.
    """
    conn = psycopg2.connect(connect_timeout=CLIENT_TIMEOUT_SEC, **postgres_settings)
    yield conn
    conn.close()


@pytest.fixture
def db_inspector(postgres_connection) -> PostgresInspector:
    """Schema introspection helper bound to the test's Postgres connection."""
    return PostgresInspector(postgres_connection)


@pytest.fixture(scope="function")
def postgres_write_connection(
    postgres_connection
) -> psycopg2.extensions.connection:
    """PostgreSQL connection for tests that INSERT or UPDATE data.

    psycopg2 does not auto-commit, so uncommitted rows are invisible to other
    connections. This fixture always rolls back after the test so no test data
    is left in the database.

    :param postgres_connection: Base connection from ``postgres_connection``.
    :yield: Same connection; transaction rolled back in teardown.
    """
    yield postgres_connection
    postgres_connection.rollback()


@pytest.fixture(scope="session")
def redis_client(require_infrastructure) -> redis.Redis:
    """Shared Redis client for the test session.

    :param require_infrastructure: Gate fixture — skips if Docker is down.
    :yield: Connected ``redis.Redis`` instance; closed after the session.
    """
    client = redis.Redis(decode_responses=True, **_redis_connect_kwargs())
    yield client
    client.close()


@pytest.fixture(scope="session")
def mailhog_ui_url(require_infrastructure) -> str:
    """Base URL of the MailHog web inbox.

    :param require_infrastructure: Gate fixture — skips if Docker is down.
    :return: MailHog UI URL string (e.g. ``http://localhost:8025``).
    """
    return _env("MAILHOG_UI_URL", "http://localhost:8025")


@pytest.fixture(scope="function")
def run_seed_script(require_infrastructure) -> subprocess.CompletedProcess[str]:
    """Run `python -m scripts.seed` inside the api Docker container.

    :param require_infrastructure: Gate fixture — skips if Docker is down.
    :return: Completed subprocess result (stdout/stderr captured for failures).
    """
    # Resolve repository root: tests/integration/conftest.py -> three parents up.
    repo_root = Path(__file__).resolve().parent.parent.parent

    # Run the same CLI documented in README / TEST_DATA.md §3.1.
    # -T disables TTY allocation so pytest/CI does not hang waiting for a terminal.
    result = subprocess.run(
        ["docker", "compose", "exec", "-T", "api", "python", "-m", "scripts.seed"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
        timeout=60,
    )
    return result
