import pytest

from tests.constants import EXPECTED_MIGRATION_REVISION
from tests.support.db.inspector import PostgresInspector

pytestmark = [pytest.mark.integ, pytest.mark.reg]


def test_alembic_migration_is_at_head(db_inspector):
    """QA-103-2: Alembic ran and the DB is on the latest revision."""
    revision = db_inspector.get_alembic_revision()

    assert revision is not None, "alembic_version table is empty — migrations not applied"
    assert revision == EXPECTED_MIGRATION_REVISION, (
        f"Expected alembic head {EXPECTED_MIGRATION_REVISION}, got {revision!r}"
    )
