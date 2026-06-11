import base64
import json

import pytest

from tests.data.auth_seed import SEED_PASSWORD, SEED_USERS

pytestmark = [pytest.mark.integ, pytest.mark.reg]

ANALYST = next(u for u in SEED_USERS if u["role"] == "ANALYST")


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


def test_login_token_sub_matches_db_user_email(api_client, postgres_connection):
    """QA-104-8: JWT sub claim from analyst login matches the users table email."""
    response = api_client.post(
        "/api/v1/auth/login",
        json={"email": ANALYST["email"], "password": SEED_PASSWORD},
    )
    assert response.status_code == 200, "Analyst login must return 200."

    token = response.json()["access_token"]
    payload = _decode_jwt_payload(token)
    user_id = payload["sub"]

    with postgres_connection.cursor() as cur:
        cur.execute("SELECT email FROM users WHERE id = %s", (user_id,))
        row = cur.fetchone()

    assert row is not None, f"No user row found for sub={user_id!r}."
    assert row[0] == ANALYST["email"], (
        f"DB email {row[0]!r} does not match login email {ANALYST['email']!r}."
    )
