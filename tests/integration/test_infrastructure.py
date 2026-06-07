import socket

import httpx
import psycopg2
import pytest

from tests.conftest import API_TIMEOUT_SEC, CLIENT_TIMEOUT_SEC, PORT_CHECK_TIMEOUT

pytestmark = [pytest.mark.integ, pytest.mark.reg]


@pytest.mark.smoke
def test_postgres_accepts_connection(postgres_connection):
    """QA-101-1: Postgres accepts a connection and runs SELECT 1."""
    # Run the simplest possible query to prove the database is alive.
    with postgres_connection.cursor() as cur:
        cur.execute("SELECT 1")
        assert cur.fetchone()[0] == 1, "Postgres connection must accept queries."


@pytest.mark.smoke
def test_redis_responds_to_ping(redis_client):
    """QA-101-2: Redis responds to PING."""
    assert redis_client.ping() is True, "Redis must answer PING."


@pytest.mark.smoke
def test_mailhog_ui_is_reachable(mailhog_ui_url):
    """QA-101-3: MailHog web UI returns HTTP 200 and contains expected content."""
    # Open the MailHog inbox page in the browser (HTTP GET).
    response = httpx.get(mailhog_ui_url, timeout=API_TIMEOUT_SEC)

    assert response.status_code == 200, "MailHog UI must return HTTP 200."
    assert "MailHog" in response.text, (
        "MailHog UI must contain 'MailHog' in the response text."
    )


def test_postgres_rejects_invalid_credentials(invalid_postgres_settings):
    """QA-101-4: Wrong PostgreSQL credentials raise OperationalError."""
    host = invalid_postgres_settings["host"]
    port = invalid_postgres_settings["port"]

    # Only run this negative test when Postgres is actually listening on the port.
    try:
        with socket.create_connection((host, port), timeout=PORT_CHECK_TIMEOUT):
            pass
    except OSError:
        pytest.skip(
            "PostgreSQL not running; start Docker to test invalid credentials."
        )
    with pytest.raises(psycopg2.OperationalError):
        psycopg2.connect(connect_timeout=CLIENT_TIMEOUT_SEC, **invalid_postgres_settings)
