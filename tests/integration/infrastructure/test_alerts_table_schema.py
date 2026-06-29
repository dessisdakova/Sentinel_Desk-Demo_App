import pytest

from tests.support.db.inspector import PostgresInspector

pytestmark = [pytest.mark.integ, pytest.mark.reg]


def test_alerts_table_has_expected_columns(db_inspector):
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

    columns = db_inspector.get_columns("alerts")
    assert [c.name for c in columns] == expected_columns, "Alerts table columns mismatch."


def test_alerts_table_columns_have_correct_data_type(db_inspector):
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
        ("timestamptz", "NO"),
    ]

    columns = db_inspector.get_columns("alerts")
    data_types = [(c.udt_name, c.is_nullable) for c in columns]

    assert data_types == expected_data_types, (
        "Alerts table column data type or nullability mismatch."
    )


def test_alerts_table_primary_key_is_correct(db_inspector):
    """QA-201-3: Alert table primary key is 'id'."""
    assert db_inspector.get_primary_key_columns("alerts") == ["id"], (
        "Primary key of alerts table is incorrect."
    )


def test_alerts_table_foreign_key_is_correct(db_inspector):
    """QA-201-4: Alert table foreign key is 'assigned_to_id' from users table."""
    assert db_inspector.get_foreign_keys("alerts") == [
        ("assigned_to_id", "users", "id"),
    ], "Foreign key of alerts table is incorrect."


def test_alert_events_table_has_expected_columns(db_inspector):
    """QA-201-5: Alert_events table exists with expected columns."""
    expected_columns = [
        "id",
        "alert_id",
        "event_type",
        "payload",
        "created_by",
        "created_at",
    ]

    columns = db_inspector.get_columns("alert_events")
    assert [c.name for c in columns] == expected_columns, (
        "Alert_events table columns mismatch."
    )


def test_alert_events_table_columns_have_correct_data_type(db_inspector):
    """QA-201-6: Alert_events table columns have correct data type."""
    expected_data_types = [
        ("uuid", "NO"),
        ("uuid", "NO"),
        ("varchar", "NO"),
        ("jsonb", "NO"),
        ("uuid", "YES"),
        ("timestamptz", "NO"),
    ]

    columns = db_inspector.get_columns("alert_events")
    data_types = [(c.udt_name, c.is_nullable) for c in columns]

    assert data_types == expected_data_types, (
        "Alert_events table column data type or nullability mismatch."
    )


def test_alert_events_table_primary_key_is_correct(db_inspector):
    """QA-201-7: Alert_events table primary key is 'id'."""
    assert db_inspector.get_primary_key_columns("alert_events") == ["id"], (
        "Primary key of alert_events table is incorrect."
    )


def test_alert_events_table_foreign_keys_are_correct(db_inspector):
    """QA-201-8: Alert_events table foreign keys are present."""
    assert db_inspector.get_foreign_keys("alert_events") == [
        ("alert_id", "alerts", "id"),
        ("created_by", "users", "id"),
    ], "Foreign keys of alert_events table are incorrect."


def test_alerts_table_has_expected_indexes(db_inspector):
    """QA-201-9: Composite and assigned_to_id indexes exist on alerts."""
    expected_indexes = {
        "ix_alerts_status_severity_created_at": [
            "status",
            "severity",
            "created_at desc",
        ],
        "ix_alerts_assigned_to_id": ["assigned_to_id"],
    }

    indexes = db_inspector.get_indexes("alerts")

    for index_name, expected_columns in expected_indexes.items():
        assert index_name in indexes, f"Index {index_name} is missing."
        index_def = indexes[index_name].lower()
        for column in expected_columns:
            assert column in index_def, (
                f"Column {column!r} missing from index {index_name!r}"
            )
