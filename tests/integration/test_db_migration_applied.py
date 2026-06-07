import pytest

pytestmark = [pytest.mark.integ, pytest.mark.reg]

# Revision ID from backend/alembic/versions/20260523_0001_initial_users_table.py
EXPECTED_MIGRATION_REVISION = "20260523_0001"


def test_alembic_migration_is_at_head(postgres_connection):
    """QA-103-2: Alembic ran and the DB is on the latest revision."""
    # Alembic stores the current revision in this small table.
    with postgres_connection.cursor() as cur:
        cur.execute("SELECT version_num FROM alembic_version")
        row = cur.fetchone()

    # Migrations must have run at least once, and match our initial users migration.
    assert row is not None, "alembic_version table is empty — migrations not applied"
    assert row[0] == EXPECTED_MIGRATION_REVISION
