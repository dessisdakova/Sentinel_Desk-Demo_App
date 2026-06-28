import pytest

pytestmark = [pytest.mark.integ, pytest.mark.reg]

from tests.constants import EXPECTED_MIGRATION_REVISION


def test_alembic_migration_is_at_head(postgres_connection):
    """QA-103-2: Alembic ran and the DB is on the latest revision."""
    # Alembic stores the current revision in this small table.
    with postgres_connection.cursor() as cur:
        cur.execute("SELECT version_num FROM alembic_version")
        row = cur.fetchone()

    # Migrations must have run at least once, and match the current Alembic head.
    assert row is not None, "alembic_version table is empty — migrations not applied"
    assert row[0] == EXPECTED_MIGRATION_REVISION, (
        f"Expected alembic head {EXPECTED_MIGRATION_REVISION}, got {row[0]!r}"
    )
