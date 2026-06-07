import pytest

pytestmark = pytest.mark.integ

EXPECTED_COLUMNS = (
    "id",
    "email",
    "password_hash",
    "role",
    "display_name",
    "active",
    "created_at",
    "updated_at",
)


def test_users_table_has_expected_columns_and_constraints(postgres_connection):
    """QA-103-1: Users table has expected columns and constraints."""
    with postgres_connection.cursor() as cur:
        cur.execute(
            """
            SELECT column_name, data_type, udt_name, is_nullable
            FROM information_schema.columns
            WHERE table_schema = 'public' AND table_name = 'users'
            ORDER BY ordinal_position
            """
        )
        cols = {row[0]: (row[1], row[2], row[3]) for row in cur.fetchall()}
    assert set(cols) == set(EXPECTED_COLUMNS), (
        f"users columns mismatch. expected={set(EXPECTED_COLUMNS)!r}, actual={set(cols)!r}"
    )
    assert cols["id"] == ("uuid", "uuid", "NO"), "id must be uuid NOT NULL"
    assert cols["email"] == ("character varying", "varchar", "NO")
    assert cols["password_hash"] == ("character varying", "varchar", "NO")
    assert cols["display_name"] == ("character varying", "varchar", "NO")
    assert cols["role"] == ("USER-DEFINED", "user_role", "NO"), (
        "role must use user_role enum NOT NULL"
    )
    assert cols["active"] == ("boolean", "bool", "NO")
    assert cols["created_at"] == ("timestamp with time zone", "timestamptz", "NO")
    assert cols["updated_at"] == ("timestamp with time zone", "timestamptz", "NO")
    with postgres_connection.cursor() as cur:
        cur.execute(
            """
            SELECT kcu.column_name
            FROM information_schema.table_constraints tc
            JOIN information_schema.key_column_usage kcu
              ON tc.constraint_schema = kcu.constraint_schema
             AND tc.constraint_name = kcu.constraint_name
            WHERE tc.table_schema = 'public'
              AND tc.table_name = 'users'
              AND tc.constraint_type = 'PRIMARY KEY'
            """
        )
        pk_columns = {row[0] for row in cur.fetchall()}
    assert pk_columns == {"id"}, f"users primary key must be on id, got {pk_columns!r}"
    with postgres_connection.cursor() as cur:
        cur.execute(
            """
            SELECT indexname, indexdef
            FROM pg_indexes
            WHERE schemaname = 'public' AND tablename = 'users'
            """
        )
        indexes = {row[0]: row[1] for row in cur.fetchall()}
    assert "ix_users_email" in indexes, (
        f"unique index ix_users_email missing; indexes={list(indexes)!r}"
    )
    email_index_def = indexes["ix_users_email"].lower()
    assert "unique" in email_index_def and "email" in email_index_def, (
        "ix_users_email must be a UNIQUE index on email"
    )
