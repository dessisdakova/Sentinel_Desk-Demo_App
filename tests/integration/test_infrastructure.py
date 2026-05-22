import psycopg2
import pytest
import requests

from tests.conftest import _port_is_open

# Only tests that need live Docker use require_infrastructure (avoids hanging on negative test).
pytestmark = pytest.mark.integ


def test_postgres_accepts_connection(require_infrastructure, postgres_connection):
    """QA-101-1: Postgres connection is opened and eccepts queries."""
    with postgres_connection.cursor() as cur:
        cur.execute("SELECT 1")
        assert cur.fetchone()[0] == 1 , "Postgres connection must accept queries."


def test_redis_responds_to_ping(require_infrastructure, redis_client):
    """QA-101-1: Redis answers PING."""
    assert redis_client.ping() is True, "Redis must answer PING."


def test_mailhog_ui_is_reachable(require_infrastructure, mailhog_ui_url):
    """QA-101-1: MailHog UI returns HTTP 200."""
    response = requests.get(mailhog_ui_url, timeout=5)

    assert response.status_code == 200, "MailHog UI must return HTTP 200."
    assert "MailHog" in response.text, "MailHog UI must contain 'MailHog' in the response text."


def test_postgres_rejects_invalid_credentials(invalid_postgres_settings):
    """
    QA-101-2: Wrong credentials raise OperationalError.

    Does not use require_infrastructure so pytest does not probe Redis/MailHog first.
    """
    host = invalid_postgres_settings["host"]
    port = invalid_postgres_settings["port"]
    if not _port_is_open(host, port):
        pytest.skip("PostgreSQL not running; start Docker to test invalid credentials.")

    with pytest.raises(psycopg2.OperationalError):
        psycopg2.connect(connect_timeout=2, **invalid_postgres_settings)


def test_local_settings_match_documented_defaults(
    require_infrastructure,
    postgres_settings,
    redis_settings,
    mailhog_ui_url,
    documented_local_defaults,
):
    """
    QA-101-3 (SENT-101 scope): .env-backed settings match .env.example / README defaults.

    TEST_DATA.md stable UUIDs are validated after seed exists (SENT-206-QA, SENT-1001-QA).
    """
    expected = documented_local_defaults

    assert postgres_settings["user"] == expected["postgres_user"]
    assert postgres_settings["dbname"] == expected["postgres_db"]
    assert postgres_settings["host"] == expected["postgres_host"]
    assert postgres_settings["port"] == expected["postgres_port"]
    assert redis_settings["host"] == expected["redis_host"]
    assert redis_settings["port"] == expected["redis_port"]
    assert mailhog_ui_url == expected["mailhog_ui"]
