import pytest

pytestmark = [pytest.mark.integ, pytest.mark.reg]

from tests.constants import EXPECTED_MIGRATION_REVISION


def test_alerts_table_has_expected_columns(postgres_connection):
    """QA-201-1: Alert table exists with expected columns."""
    expected_columns = [
        "id",
        "external_id",
        "source",
        "severity",
        "status",
        "enrichment_status",
        "title",
        "ioc_list",
        "assigned_to_id",
        "sla_due_at",
        "created_at",
        "updated_at",
    ]

    with postgres_connection.cursor() as cur:
        cur.execute("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = 'alerts'
            ORDER BY ordinal_position
        """)
        columns = [row[0] for row in cur.fetchall()]

    assert columns == expected_columns, "Alerts table columns mismatch."


def test_alerts_table_columns_have_correct_data_type(postgres_connection):
    """QA-201-2: Alert table columns have correct data type."""
    expected_data_types = [
        ("uuid", "NO"),
        ("varchar", "NO"),
        ("alert_source", "NO"),
        ("alert_severity", "NO"),
        ("alert_status", "NO"),
        ("enrichment_status", "NO"),
        ("varchar", "NO"),
        ("jsonb", "NO"),
        ("uuid", "YES"),
        ("timestamptz", "YES"),
        ("timestamptz", "NO"),
        ("timestamptz", "NO")
    ]

    with postgres_connection.cursor() as cur:
        cur.execute("""
            SELECT udt_name, is_nullable
            FROM information_schema.columns
            WHERE table_name = 'alerts'
            ORDER BY ordinal_position
        """)
        data_types = [(row[0], row[1]) for row in cur.fetchall()]

    assert data_types == expected_data_types, (
        "Alerts table column data type or nullability mismatch.")


def test_alerts_table_primary_key_is_correct(postgres_connection):
    """QA-201-3: Alert table primary key is 'id'."""
    expected_pk = ["id"]

    with postgres_connection.cursor() as cur:
        cur.execute("""
            SELECT kcu.column_name
            FROM information_schema.table_constraints tc
            JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_name = kcu.table_name
            WHERE tc.table_name = 'alerts'
                AND tc.constraint_type = 'PRIMARY KEY'
        """)
        primary_key = [row[0] for row in cur.fetchall()]

    assert primary_key == expected_pk, "Primary key of alerts table is incorrect."


def test_alerts_table_foreign_key_is_correct(postgres_connection):
    """QA-201-4: Alert table foreign key is 'assigned_to_id' from users table."""
    expected_fk = [("assigned_to_id", "users", "id")]

    with postgres_connection.cursor() as cur:
        cur.execute("""
            SELECT kcu.column_name, ccu.table_name, ccu.column_name
            FROM information_schema.table_constraints tc
            JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_schema = kcu.table_schema
                AND tc.table_name = kcu.table_name
            JOIN information_schema.constraint_column_usage ccu
                ON tc.constraint_name = ccu.constraint_name
                AND tc.table_schema = ccu.table_schema
            WHERE tc.table_schema = 'public'
                AND tc.table_name = 'alerts'
                AND tc.constraint_type = 'FOREIGN KEY'
            ORDER BY kcu.column_name
        """)
        foreign_key = [(row[0], row[1], row[2]) for row in cur.fetchall()]

    assert foreign_key == expected_fk, (
        "Foreign key of alerts table is incorrect.")


def test_alert_events_table_has_expected_columns(postgres_connection):
    """QA-201-5: Alert_events table exists with expected columns."""
    expected_columns = [
        "id",
        "alert_id",
        "event_type",
        "payload",
        "created_by",
        "created_at",
    ]

    with postgres_connection.cursor() as cur:
        cur.execute("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = 'alert_events'
            ORDER BY ordinal_position
        """)
        columns = [row[0] for row in cur.fetchall()]

    assert columns == expected_columns, "Alert_events table columns mismatch."


def test_alert_events_table_columns_have_correct_data_type(postgres_connection):
    """QA-201-6: Alert_events table columns have correct data type."""
    expected_data_types = [
        ("uuid", "NO"),
        ("uuid", "NO"),
        ("varchar", "NO"),
        ("jsonb", "NO"),
        ("uuid", "YES"),
        ("timestamptz", "NO")
    ]

    with postgres_connection.cursor() as cur:
        cur.execute("""
            SELECT udt_name, is_nullable
            FROM information_schema.columns
            WHERE table_name = 'alert_events'
            ORDER BY ordinal_position
        """)
        data_types = [(row[0], row[1]) for row in cur.fetchall()]

    assert data_types == expected_data_types, (
        "Alert_events table column data type or nullability mismatch.")


def test_alert_events_table_primary_key_is_correct(postgres_connection):
    """QA-201-7: Alert_events table primary key is 'id'."""
    expected_pk = ["id"]

    with postgres_connection.cursor() as cur:
        cur.execute("""
            SELECT kcu.column_name
            FROM information_schema.table_constraints tc
            JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_name = kcu.table_name
            WHERE tc.table_name = 'alert_events'
                AND tc.constraint_type = 'PRIMARY KEY'
        """)
        primary_key = [row[0] for row in cur.fetchall()]

    assert primary_key == expected_pk, "Primary key of alert_events table is incorrect."


def test_alert_events_table_foreign_keys_are_correct(postgres_connection):
    """QA-201-8: Alert_events table foreign keys are present."""
    expected_fk = [
        ("alert_id", "alerts", "id"),
        ("created_by", "users", "id"),
    ]

    with postgres_connection.cursor() as cur:
        cur.execute("""
            SELECT kcu.column_name, ccu.table_name, ccu.column_name
            FROM information_schema.table_constraints tc
            JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_schema = kcu.table_schema
                AND tc.table_name = kcu.table_name
            JOIN information_schema.constraint_column_usage ccu
                ON tc.constraint_name = ccu.constraint_name
                AND tc.table_schema = ccu.table_schema
            WHERE tc.table_schema = 'public'
                AND tc.table_name = 'alert_events'
                AND tc.constraint_type = 'FOREIGN KEY'
            ORDER BY kcu.column_name
        """)
        foreign_keys = [(row[0], row[1], row[2]) for row in cur.fetchall()]

    assert foreign_keys == expected_fk, (
        "Foreign keys of alert_events table are incorrect.")


def test_alerts_table_has_expected_indexes(postgres_connection):
    """QA-201-9: Composite and assigned_to_id indexes exist on alerts."""
    expected_indexes = {
        "ix_alerts_status_severity_created_at": ["status", "severity", "created_at desc"],
        "ix_alerts_assigned_to_id": ["assigned_to_id"],
    }

    with postgres_connection.cursor() as cur:
        cur.execute(
            """
            SELECT indexname, indexdef
            FROM pg_indexes
            WHERE schemaname = 'public' AND tablename = 'alerts'
            """
        )
        indexes = {row[0]: row[1] for row in cur.fetchall()}

    for index_name, expected_columns in expected_indexes.items():
        assert index_name in indexes, f"Index {index_name} is missing."
        index_def = indexes[index_name].lower()
        for column in expected_columns:
            assert column in index_def, (
                f"Column {column!r} missing from index {index_name!r}"
            )


def test_alembic_migration_is_at_head(postgres_connection):
    """QA-201-10: Alembic ran and the DB is on the latest revision."""
    with postgres_connection.cursor() as cur:
        cur.execute("SELECT version_num FROM alembic_version")
        row = cur.fetchone()

    assert row is not None, "alembic_version table is empty — migrations not applied."
    assert row[0] == expected_migration_revision, (
        f"Expected alembic head {expected_migration_revision}, got {row[0]!r}"
    )
