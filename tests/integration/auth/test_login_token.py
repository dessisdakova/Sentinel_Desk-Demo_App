import pytest

from tests.constants import SEED_ADMIN_USER, SEED_ANALYST_USER, SEED_LEAD_USER
from tests.integration.conftest import _decode_jwt_payload

pytestmark = [pytest.mark.integ, pytest.mark.reg]


@pytest.mark.parametrize("user", [
    pytest.param(SEED_ANALYST_USER, id="analyst"),
    pytest.param(SEED_LEAD_USER, id="lead"),
    pytest.param(SEED_ADMIN_USER, id="admin"),
])
def test_login_token_sub_matches_db_user_email(api_client, postgres_connection, user):
    """QA-104-8: JWT sub claim matches the users table email for each role."""
    response = api_client.post(
        "/api/v1/auth/login",
        json={"email": user["email"], "password": user["password"]},
    )
    assert response.status_code == 200, f"Login must succeed for {user['email']}."
    payload = _decode_jwt_payload(response.json()["access_token"])
    user_id = payload["sub"]
    with postgres_connection.cursor() as cur:
        cur.execute("SELECT email FROM users WHERE id = %s", (user_id,))
        row = cur.fetchone()
    assert row is not None, f"No user row found for sub={user_id!r}."
    assert row[0] == user["email"], (
        f"DB email {row[0]!r} does not match login email {user['email']!r}."
    )
