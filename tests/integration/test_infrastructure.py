import psycopg2
import pytest
import httpx
import socket

from conftest import CLIENT_TIMEOUT_SEC, API_TIMEOUT_SEC

pytestmark = pytest.mark.integ


def test_postgres_accepts_connection(postgres_connection):
    """QA-101-1: Postgres connection is opened and eccepts queries."""
    with postgres_connection.cursor() as cur:
        cur.execute("SELECT 1")
        assert cur.fetchone()[0] == 1 , "Postgres connection must accept queries."


def test_redis_responds_to_ping(redis_client):
    """QA-101-1: Redis answers PING."""
    assert redis_client.ping() is True, "Redis must answer PING."


def test_mailhog_ui_is_reachable(mailhog_ui_url):
    """QA-101-1: MailHog UI returns HTTP 200."""
    response = httpx.get(mailhog_ui_url, timeout=API_TIMEOUT_SEC)

    assert response.status_code == 200, "MailHog UI must return HTTP 200."
    assert "MailHog" in response.text, "MailHog UI must contain 'MailHog' in the response text."


def test_postgres_rejects_invalid_credentials(invalid_postgres_settings):
    """
    QA-101-2: Wrong credentials raise OperationalError.
    """
    host = invalid_postgres_settings["host"]
    port = invalid_postgres_settings["port"]
    try:
        with socket.create_connection((host, port), timeout=CLIENT_TIMEOUT_SEC):
            pass
    except OSError:
        pytest.skip("PostgreSQL not running; start Docker to test invalid credentials.")
    with pytest.raises(psycopg2.OperationalError):
        psycopg2.connect(connect_timeout=2, **invalid_postgres_settings)
