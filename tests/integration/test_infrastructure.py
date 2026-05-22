import socket

import httpx
import psycopg2
import pytest

from tests.conftest import API_TIMEOUT_SEC, CLIENT_TIMEOUT_SEC, PORT_CHECK_TIMEOUT

pytestmark = pytest.mark.integ


def test_postgres_accepts_connection(postgres_connection):
    """Postgres accepts a connection and runs SELECT 1 (QA-101-1)."""
    with postgres_connection.cursor() as cur:
        cur.execute("SELECT 1")
        assert cur.fetchone()[0] == 1, "Postgres connection must accept queries."


def test_redis_responds_to_ping(redis_client):
    """Redis responds to PING (QA-101-1)."""
    assert redis_client.ping() is True, "Redis must answer PING."


def test_mailhog_ui_is_reachable(mailhog_ui_url):
    """MailHog web UI returns HTTP 200 and contains expected content (QA-101-1)."""
    response = httpx.get(mailhog_ui_url, timeout=API_TIMEOUT_SEC)

    assert response.status_code == 200, "MailHog UI must return HTTP 200."
    assert "MailHog" in response.text, (
        "MailHog UI must contain 'MailHog' in the response text."
    )


def test_postgres_rejects_invalid_credentials(invalid_postgres_settings):
    """Wrong PostgreSQL credentials raise OperationalError (QA-101-2)."""
    host = invalid_postgres_settings["host"]
    port = invalid_postgres_settings["port"]
    try:
        with socket.create_connection((host, port), timeout=PORT_CHECK_TIMEOUT):
            pass
    except OSError:
        pytest.skip(
            "PostgreSQL not running; start Docker to test invalid credentials."
        )
    with pytest.raises(psycopg2.OperationalError):
        psycopg2.connect(connect_timeout=CLIENT_TIMEOUT_SEC, **invalid_postgres_settings)
