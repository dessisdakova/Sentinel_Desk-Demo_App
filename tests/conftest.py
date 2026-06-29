import time
from pathlib import Path

import httpx
import jwt
import pytest
from dotenv import load_dotenv

from tests.secrets.provider import get_jwt_secret, get_user_secret
from tests.support.api_session import ApiSession
from tests.support.auth import _login_as
from tests.support.clients import AdminClient, AuthClient, HealthClient
from tests.support.connectivity import (
    _postgres_connect_kwargs,
    _redis_connect_kwargs,
    _api_host_and_port,
    _can_connect_postgres,
    _can_ping_redis,
    _can_reach_mailhog_ui,
    _port_is_open,
)
from tests.support.env import _env

API_TIMEOUT_SEC = 5  # FastAPI
ROLE_TO_USER_KEY = {"ANALYST": "analyst", "LEAD": "lead", "ADMIN": "admin"}


def pytest_addoption(parser):
    """Add command-line option to select environment."""
    parser.addoption(
        "--env",
        action="store",
        default="local",
        choices=["local", "qa", "staging"],
        help="Target environment (default: local)",
    )


@pytest.fixture(scope="session", autouse=True)
def load_environment(request):
    """Load environment file based on command-line option."""
    env = request.config.getoption("--env")
    env_file = Path(__file__).parent / "environments" / f"{env}.env"
    if not env_file.exists():
        pytest.fail(f"Environment file {env_file} not found")
    load_dotenv(dotenv_path=env_file, override=True)


@pytest.fixture(scope="session", autouse=True)
def announce_environment(request):
    """Announce the environment being tested."""
    env_name = request.config.getoption("--env")
    print(f"\n>>> Running tests against environment: {env_name.upper()} <<<\n")


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

    Shared between API tests (via ``api_session``) and E2E tests (via
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
def api_session(api_base_url, require_api) -> ApiSession:
    """Shared API config and HTTP client for the pytest session.

    :param api_base_url: Root URL of the FastAPI service (from root conftest).
    :param require_api: Gate fixture — skips if the API is down or unhealthy.
    :yield: ``ApiSession`` with ``base_url`` and a single ``httpx.Client``.
    """
    client = httpx.Client(base_url=api_base_url, timeout=API_TIMEOUT_SEC)
    session = ApiSession(base_url=api_base_url, client=client)
    yield session
    session.close()


@pytest.fixture(scope="session")
def auth_client(api_session) -> AuthClient:
    """Unauthenticated auth API wrapper (no default JWT)."""
    return AuthClient(api_session)


@pytest.fixture(scope="session")
def admin_client(api_session) -> AdminClient:
    """Unauthenticated admin API wrapper (no default JWT)."""
    return AdminClient(api_session)


@pytest.fixture(scope="session")
def health_client(api_session) -> HealthClient:
    """Health probe API wrapper."""
    return HealthClient(api_session)


@pytest.fixture(scope="session")
def analyst_auth_client(api_session, analyst_token) -> AuthClient:
    """Auth API wrapper with ANALYST JWT bound at construction."""
    return AuthClient(api_session, token=analyst_token)


@pytest.fixture(scope="session")
def lead_auth_client(api_session, lead_token) -> AuthClient:
    """Auth API wrapper with LEAD JWT bound at construction."""
    return AuthClient(api_session, token=lead_token)


@pytest.fixture(scope="session")
def admin_auth_client(api_session, admin_token) -> AuthClient:
    """Auth API wrapper with ADMIN JWT bound at construction."""
    return AuthClient(api_session, token=admin_token)


@pytest.fixture(scope="session")
def authenticated_admin_client(api_session, admin_token) -> AdminClient:
    """Admin API wrapper with ADMIN JWT bound at construction."""
    return AdminClient(api_session, token=admin_token)


@pytest.fixture(scope="session")
def password_for(load_environment):
    """Return a lookup that fetches a seed user's password by logical key.

    :param load_environment: Ensures AWS_* env vars are loaded first.
    :return: Callable mapping a user key (e.g. "analyst") to its password.
    """

    def _lookup(user_key: str) -> str:
        return get_user_secret(user_key)["password"]

    return _lookup


@pytest.fixture(scope="session")
def analyst_credentials(load_environment) -> dict[str, str]:
    """Email + password for ANALYST user from Secrets Manager."""
    return get_user_secret("analyst")


@pytest.fixture(scope="session")
def analyst_token(api_session, analyst_credentials) -> str:
    """Session-scoped JWT for ANALYST user."""
    return _login_as("ANALYST", api_session, analyst_credentials)


@pytest.fixture(scope="session")
def lead_credentials(load_environment) -> dict[str, str]:
    """Email + password for LEAD user from Secrets Manager."""
    return get_user_secret("lead")


@pytest.fixture(scope="session")
def lead_token(api_session, lead_credentials) -> str:
    """Session-scoped JWT for LEAD user."""
    return _login_as("LEAD", api_session, lead_credentials)


@pytest.fixture(scope="session")
def admin_credentials(load_environment) -> dict[str, str]:
    """Email + password for ADMIN user from Secrets Manager."""
    return get_user_secret("admin")


@pytest.fixture(scope="session")
def admin_token(api_session, admin_credentials) -> str:
    """Session-scoped JWT for ADMIN user."""
    return _login_as("ADMIN", api_session, admin_credentials)


@pytest.fixture(scope="session")
def token(request, api_session, load_environment) -> str:
    """Log in as the requested role and return the access token.

    :param request: pytest request object; request.param is the role string.
    :return: JWT access token string.
    """
    user_key = ROLE_TO_USER_KEY[request.param]
    return _login_as(request.param, api_session, get_user_secret(user_key))


@pytest.fixture(scope="function")
def expired_token(load_environment) -> str:
    """Mints a synthetically expired JWT token and returns it."""
    jwt_secret = get_jwt_secret()
    return jwt.encode({"exp": time.time() - 10}, jwt_secret, algorithm="HS256")
