import json
from pathlib import Path

import psycopg2
import pytest
import redis

from tests.conftest import (
    CLIENT_TIMEOUT_SEC,
    _env,
    _postgres_connect_kwargs,
    _redis_connect_kwargs,
)


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
