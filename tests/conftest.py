import os
import socket
from typing import Any
from urllib.parse import urlparse

import httpx
import psycopg2
import pytest
import redis
from dotenv import load_dotenv
from redis.backoff import NoBackoff
from redis.retry import Retry

load_dotenv()

# Seconds to wait for a TCP port check before treating a service as down.
PORT_CHECK_TIMEOUT = 0.5

# Default timeout (seconds) for Postgres, Redis, and MailHog probe clients.
CLIENT_TIMEOUT_SEC = 2

# Default timeout (seconds) for HTTP calls to the FastAPI application.
API_TIMEOUT_SEC = 5


def _env(name: str, default: str | None = None) -> str:
    """Read an environment variable or fail the test run with a clear message.

    :param name: Variable name as it appears in '.env' (e.g. 'POSTGRES_HOST').
    :param default: Value to use when the variable is unset.
    :return: Non-empty string value.
    :raises: pytest.Failed: When the variable is missing and no usable default exists.
    """
    value = os.getenv(name, default)
    if value is None or value == "":
        pytest.fail(f"Missing environment variable {name}. Copy .env.example to .env")
    return value


def _postgres_connect_kwargs(**overrides: Any) -> dict[str, Any]:
    """Build keyword arguments for db connection from environment variables.

    :param **overrides: Any key to replace in the base dict (e.g. password="wrong").
    :return: Dictionary of db keyword arguments.
    """
    base = {
        "host": _env("POSTGRES_HOST", "localhost"),
        "port": int(_env("POSTGRES_PORT", "5432")),
        "user": _env("POSTGRES_USER", "sentinel"),
        "password": _env("POSTGRES_PASSWORD", "sentinel"),
        "dbname": _env("POSTGRES_DB", "sentineldesk"),
    }
    base.update(overrides)
    return base


def _redis_connect_kwargs(**overrides: Any) -> dict[str, Any]:
    """Build keyword arguments for redis client with safe timeouts and no retries.
    Disabling retries avoids long hangs when Docker is stopped (redis-py 6+).

    :param **overrides: Any key to replace in the base dict.
    :return: Dictionary of redis client keyword arguments.
    """
    base = {
        "host": _env("REDIS_HOST", "localhost"),
        "port": int(_env("REDIS_PORT", "6379")),
        "password": os.getenv("REDIS_PASSWORD") or None,
        "socket_connect_timeout": CLIENT_TIMEOUT_SEC,
        "socket_timeout": CLIENT_TIMEOUT_SEC,
        "health_check_interval": 0,
        "retry": Retry(backoff=NoBackoff(), retries=0),
    }
    base.update(overrides)
    return base


def _port_is_open(host: str, port: int, timeout: float = PORT_CHECK_TIMEOUT) -> bool:
    """Check whether a TCP port accepts connections (fast pre-flight probe).

    :param host: Hostname or IP (e.g. localhost). Must not be a full URL.
    :param port: Port number (e.g. 5432, 8000).
    :param timeout: Maximum seconds to wait for a connection attempt.
    :return: True if the port accepted a connection; False on timeout or connection refused.
    """
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _api_host_and_port(base_url: str, fallback_port: int = 8000) -> tuple[str, int]:
    """Split an HTTP base URL into hostname and port.

    :param base_url: Full base URL (e.g. 'http://localhost:8000').
    :param fallback_port: Port used when the URL omits an explicit port.
    :return: Tuple (hostname, port) suitable for socket checks.
    """
    parsed = urlparse(base_url)
    host = parsed.hostname or "localhost"
    port = parsed.port if parsed.port is not None else fallback_port
    return host, port


def _can_connect_postgres() -> bool:
    """Probe PostgreSQL with a real connection and 'SELECT 1'.

    :return: True if Postgres is reachable and accepts a query; False otherwise.
    """
    kwargs = _postgres_connect_kwargs()
    if not _port_is_open(kwargs["host"], kwargs["port"]):
        return False
    try:
        with psycopg2.connect(connect_timeout=CLIENT_TIMEOUT_SEC, **kwargs) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
        return True
    except psycopg2.Error:
        return False


def _can_ping_redis() -> bool:
    """Probe Redis with 'PING'.

    :return: True if Redis responds to PING; False otherwise.
    """
    kwargs = _redis_connect_kwargs()
    if not _port_is_open(kwargs["host"], kwargs["port"]):
        return False
    client = redis.Redis(decode_responses=True, **kwargs)
    try:
        return client.ping() is True
    except redis.RedisError:
        return False
    finally:
        client.close()


def _can_reach_mailhog_ui() -> bool:
    """Probe MailHog web UI with an HTTP GET.

    :return: True if MailHog UI returns HTTP 200; False on network errors or other statuses.
    """
    url = _env("MAILHOG_UI_URL", "http://localhost:8025")
    try:
        with httpx.Client(timeout=CLIENT_TIMEOUT_SEC) as client:
            return client.get(url).status_code == 200
    except httpx.HTTPError:
        return False


@pytest.fixture(scope="session")
def require_infrastructure():
    """Skip integration tests when the Docker infrastructure stack is not running.
    Runs once per pytest session the first time a test needs this fixture.
    Checks Postgres, Redis, and MailHog using short timeouts.

    :return: None
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
def api_base_url() -> str:
    """Root URL of the FastAPI service.
    Shared between API tests (via ``api_client``) and E2E tests (via
    ``playwright_api_context``).

    :return: Base URL string with no trailing slash.
    """
    return _env("API_BASE_URL", "http://localhost:8000").rstrip("/")


@pytest.fixture(scope="session")
def require_api(api_base_url):
    """Skip tests when the FastAPI application is not running or unhealthy.
    Used by both ``tests/api/`` and ``tests/e2e/``. Performs a TCP probe
    first (fast), then an HTTP health check (confirms the app is up and
    responding correctly).

    :param api_base_url: Root URL of the FastAPI service.
    :return: None
    """
    host, port = _api_host_and_port(api_base_url, fallback_port=8000)
    if not _port_is_open(host, port):
        pytest.skip(
            f"API not available at {host}:{port} (from {api_base_url}). "
            "Run: docker compose up -d"
        )
    try:
        with httpx.Client(base_url=api_base_url, timeout=API_TIMEOUT_SEC) as client:
            response = client.get("/health")
            response.raise_for_status()
    except httpx.HTTPError:
        pytest.skip(
            f"API health check failed at {api_base_url}. Run: docker compose up -d"
        )


@pytest.fixture(scope="session")
def api_client(api_base_url, require_api) -> httpx.Client:
    """Synchronous HTTP client pointed at the SentinelDesk API.

    :param api_base_url: Root URL of the FastAPI service (from root conftest).
    :param require_api: Gate fixture — skips if the API is down or unhealthy.
    :yield: Configured ``httpx.Client`` with ``base_url`` and timeout set.
    """
    client = httpx.Client(base_url=api_base_url, timeout=API_TIMEOUT_SEC)
    yield client
    client.close()