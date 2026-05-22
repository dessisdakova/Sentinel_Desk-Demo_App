"""
Shared pytest fixtures for SentinelDesk QA automation.

Loads .env from the repository root (copy .env.example to .env first).
Infrastructure fixtures target SENT-101-QA (Postgres, Redis, MailHog).
API/auth clients are added in later epics (SENT-102-QA onward).
"""

import json
import os
import socket
from pathlib import Path
from urllib.parse import urlparse

import httpx
import psycopg2
import pytest
import redis
from dotenv import load_dotenv
from redis.backoff import NoBackoff
from redis.retry import Retry

load_dotenv()

# Seconds to wait for a TCP port before treating a service as down (Docker stopped).
_PORT_CHECK_TIMEOUT = 0.5
_CLIENT_TIMEOUT_SEC = 2
_API_TIMEOUT_SEC = 5


def _env(name: str, default: str) -> str:
    """Read a required env var; fail the run with a helpful message if missing."""
    value = os.getenv(name, default)
    if value is None or value == "":
        pytest.fail(f"Missing environment variable {name}. Copy .env.example to .env")
    return value


def _port_is_open(host: str, port: int, timeout: float = _PORT_CHECK_TIMEOUT) -> bool:
    """Fast check: is anything listening on host:port? Fails quickly when Docker is down."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _api_host_and_port(base_url: str, fallback_port: int = 8000) -> tuple[str, int]:
    """Parse API_BASE_URL into hostname and port for socket checks (not the full URL string)."""
    parsed = urlparse(base_url)
    host = parsed.hostname or "localhost"
    port = parsed.port if parsed.port is not None else fallback_port
    return host, port


def _postgres_connect_kwargs(**overrides) -> dict:
    """Build psycopg2.connect kwargs from env; overrides for negative tests."""
    base = {
        "host": _env("POSTGRES_HOST", "localhost"),
        "port": int(_env("POSTGRES_PORT", "5432")),
        "user": _env("POSTGRES_USER", "sentinel"),
        "password": _env("POSTGRES_PASSWORD", "sentinel"),
        "dbname": _env("POSTGRES_DB", "sentineldesk"),
    }
    base.update(overrides)
    return base


def _redis_client(**overrides) -> redis.Redis:
    """Redis client with short timeouts and no connection retries (avoids pytest hang)."""
    settings = {
        "host": _env("REDIS_HOST", "localhost"),
        "port": int(_env("REDIS_PORT", "6379")),
        "password": os.getenv("REDIS_PASSWORD") or None,
        "socket_connect_timeout": _CLIENT_TIMEOUT_SEC,
        "socket_timeout": _CLIENT_TIMEOUT_SEC,
        "health_check_interval": 0,
        # redis-py 6+: use Retry instead of deprecated retry_on_timeout=False
        "retry": Retry(backoff=NoBackoff(), retries=0),
    }
    settings.update(overrides)
    return redis.Redis(decode_responses=True, **settings)


def _can_connect_postgres() -> bool:
    host = _env("POSTGRES_HOST", "localhost")
    port = int(_env("POSTGRES_PORT", "5432"))
    if not _port_is_open(host, port):
        return False
    try:
        with psycopg2.connect(
            connect_timeout=_CLIENT_TIMEOUT_SEC, **_postgres_connect_kwargs()
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
        return True
    except psycopg2.Error:
        return False


def _can_ping_redis() -> bool:
    host = _env("REDIS_HOST", "localhost")
    port = int(_env("REDIS_PORT", "6379"))
    if not _port_is_open(host, port):
        return False
    client = _redis_client()
    try:
        return client.ping() is True
    except redis.RedisError:
        return False
    finally:
        client.close()


def _can_reach_mailhog_ui() -> bool:
    url = os.getenv("MAILHOG_UI_URL", "http://localhost:8025")
    try:
        with httpx.Client(timeout=_CLIENT_TIMEOUT_SEC) as client:
            return client.get(url).status_code == 200
    except httpx.HTTPError:
        return False


# DATABASE FIXTURES
@pytest.fixture(scope="session")
def require_infrastructure():
    """
    Session gate: skip integration tests when Docker stack is not running.

    Checks Postgres, Redis, and MailHog with short TCP/HTTP timeouts so pytest
    does not hang when ``docker compose`` is stopped (redis-py retries are disabled).

    Requires: ``docker compose up -d``
    """
    missing = []
    if not _can_connect_postgres():
        missing.append("PostgreSQL (localhost:5432)")
    if not _can_ping_redis():
        missing.append("Redis (localhost:6379)")
    if not _can_reach_mailhog_ui():
        missing.append("MailHog UI (http://localhost:8025)")
    if missing:
        pytest.skip(
            "Infrastructure not available: "
            + ", ".join(missing)
            + ". Run: docker compose up -d"
        )


@pytest.fixture(scope="session")
def postgres_settings():
    """
    Valid PostgreSQL connection kwargs for the local Docker stack.

    Maps to .env / .env.example: POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER,
    POSTGRES_PASSWORD, POSTGRES_DB. Uses psycopg2 parameter name ``dbname``.
    """
    return _postgres_connect_kwargs()


@pytest.fixture(scope="function")
def postgres_connection(postgres_settings, require_infrastructure):
    """
    One database connection per test function.

    Function scope keeps tests isolated; depends on require_infrastructure so
    tests skip instead of blocking when Docker is down.
    """
    conn = psycopg2.connect(connect_timeout=_CLIENT_TIMEOUT_SEC, **postgres_settings)
    yield conn
    conn.close()


@pytest.fixture(scope="session")
def invalid_postgres_settings():
    """
    Deliberately wrong DB credentials for negative tests (QA-101-2).

    Loaded from tests/data/invalid_postgres.json — never from .env.
    """
    path = Path(__file__).parent / "data" / "invalid_postgres.json"
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    data["port"] = int(data["port"])
    return data


# REDIS FIXTURES
@pytest.fixture(scope="session")
def redis_settings():
    """
    Connection parameters for Redis from environment (.env).

    Local Docker Redis has no password; REDIS_PASSWORD may be empty.
    """
    return {
        "host": _env("REDIS_HOST", "localhost"),
        "port": int(_env("REDIS_PORT", "6379")),
        "password": os.getenv("REDIS_PASSWORD") or None,
    }


@pytest.fixture(scope="session")
def redis_client(redis_settings, require_infrastructure):
    """
    Shared Redis client for integration tests.

    Uses short socket timeouts and no retry loop (see ``_redis_client``).
    """
    client = _redis_client()
    yield client
    client.close()


# MAILHOG FIXTURES
@pytest.fixture(scope="session")
def mailhog_ui_url():
    """MailHog web UI base URL for inbox inspection (default http://localhost:8025)."""
    return os.getenv("MAILHOG_UI_URL", "http://localhost:8025")


@pytest.fixture(scope="session")
def documented_local_defaults():
    """
    Expected local connection defaults from .env.example (QA-101-3 for SENT-101).

    Not TEST_DATA.md seed UUIDs — those apply after the app seed script exists (E02+).
    """
    return {
        "postgres_user": "sentinel",
        "postgres_db": "sentineldesk",
        "postgres_host": "localhost",
        "postgres_port": 5432,
        "redis_host": "localhost",
        "redis_port": 6379,
        "mailhog_ui": "http://localhost:8025",
        "api_base_url": "http://localhost:8000",
    }


# API FIXTURES
@pytest.fixture(scope="session")
def api_base_url():
    """Base URL for HTTP tests; must match .env.example for local Docker."""
    return os.getenv("API_BASE_URL", "http://localhost:8000").rstrip("/")

@pytest.fixture(scope="session")
def api_port():
    """API port for HTTP tests; must match .env.example for local Docker."""
    return int(os.getenv("API_PORT", "8000"))

@pytest.fixture(scope="session")
def require_api(api_base_url, api_port):
    """Session gate: skip API tests when API is not running."""
    host, port = _api_host_and_port(api_base_url, fallback_port=api_port)
    if not _port_is_open(host, port):
        pytest.skip(
            f"API not available at {host}:{port} (from {api_base_url}). Run: docker compose up -d"
        )
    try:
        with httpx.Client(base_url=api_base_url, timeout=_API_TIMEOUT_SEC) as client:
            response = client.get("/health")
            response.raise_for_status()
    except httpx.HTTPError:
        pytest.skip(f"API health check failed at {api_base_url}. Run: docker compose up -d")


@pytest.fixture(scope="session")
def api_client(api_base_url, require_api):
    """Sync HTTP client for REST API tests."""
    client = httpx.Client(base_url=api_base_url, timeout=_API_TIMEOUT_SEC)
    yield client
    client.close()

