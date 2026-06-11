import pytest

from tests.api.constants import SEED_ADMIN_USER

pytestmark = [pytest.mark.integ, pytest.mark.reg]


@pytest.mark.smoke
def test_matches_user_id_to_admin_uuid(postgres_connection, api_client, admin_token):
    """QA-105-5: Admin ID from response matches admin UUID in db."""
    response = api_client.get(
        "/api/v1/admin/ping",
        headers={"Authorization": f"Bearer {admin_token}"})

    assert response.status_code == 200

    admin_uuid_response = response.json()["user_id"]
    with postgres_connection.cursor() as cur:
        cur.execute(
            "SELECT id FROM users WHERE email = %s", (SEED_ADMIN_USER["email"],))
        admin_uuid_db = cur.fetchone()[0]

    assert admin_uuid_response == str(admin_uuid_db)
