import pytest

from tests.constants import SEED_ADMIN_USER
from tests.support.db.users import get_user_field_by_email

pytestmark = [pytest.mark.integ, pytest.mark.reg]


@pytest.mark.smoke
def test_matches_user_id_to_admin_uuid(postgres_connection, admin_client, admin_token):
    """QA-105-5: Admin ID from response matches admin UUID in db."""
    response = admin_client.ping(token=admin_token)

    assert response.status_code == 200

    admin_uuid_response = response.json()["user_id"]
    admin_uuid_db = get_user_field_by_email(
        postgres_connection, SEED_ADMIN_USER["email"], "id"
    )

    assert admin_uuid_response == str(admin_uuid_db)
