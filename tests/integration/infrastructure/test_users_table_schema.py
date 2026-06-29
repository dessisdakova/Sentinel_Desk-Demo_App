import uuid

import psycopg2
import pytest

from tests.support.db.inspector import ColumnInfo

pytestmark = [pytest.mark.integ, pytest.mark.reg]

EXPECTED_ROLES = ("ANALYST", "LEAD", "ADMIN")


@pytest.mark.smoke
def test_users_table_has_expected_columns(db_inspector):
    """QA-103-1: Users table exists with the correct column names and types."""
    expected_columns = (
        "id",
        "email",
        "password_hash",
        "role",
        "display_name",
        "active",
        "created_at",
        "updated_at",
    )

    cols = db_inspector.get_column_map("users")

    assert set(cols) == set(expected_columns), (
        f"Users table columns mismatch: "
        f"expected={set(expected_columns)!r}, actual={set(cols)!r}"
    )
    assert cols["id"] == ColumnInfo("id", "uuid", "uuid", "NO"), "id must be uuid NOT NULL"
    assert cols["email"] == ColumnInfo("email", "character varying", "varchar", "NO")
    assert cols["password_hash"] == ColumnInfo(
        "password_hash", "character varying", "varchar", "NO"
    )
    assert cols["display_name"] == ColumnInfo(
        "display_name", "character varying", "varchar", "NO"
    )
    assert cols["role"] == ColumnInfo("role", "USER-DEFINED", "user_role", "NO"), (
        "role must use user_role enum NOT NULL"
    )
    assert cols["active"] == ColumnInfo("active", "boolean", "bool", "NO")
    assert cols["created_at"] == ColumnInfo(
        "created_at", "timestamp with time zone", "timestamptz", "NO"
    )
    assert cols["updated_at"] == ColumnInfo(
        "updated_at", "timestamp with time zone", "timestamptz", "NO"
    )


def test_users_table_has_primary_key_on_id(db_inspector):
    """QA-103-1: users.id is the primary key."""
    pk_columns = db_inspector.get_primary_key_columns("users")
    assert pk_columns == ["id"], (
        f"Users table primary key must be on id, got {pk_columns!r}"
    )


def test_users_email_has_unique_index(db_inspector):
    """QA-103-1: Email cannot be duplicated (unique index on email)."""
    indexes = db_inspector.get_indexes("users")

    assert "ix_users_email" in indexes, (
        f"unique index ix_users_email missing; indexes={list(indexes)!r}"
    )
    email_index_def = indexes["ix_users_email"].lower()
    assert "unique" in email_index_def and "email" in email_index_def, (
        "ix_users_email must be a UNIQUE index on email"
    )


def test_user_role_enum_has_expected_values(db_inspector):
    """QA-103-3: user_role enum contains exactly ANALYST, LEAD, ADMIN."""
    assert db_inspector.get_enum_labels("user_role") == EXPECTED_ROLES


def test_invalid_role_insert_fails(postgres_write_connection):
    """QA-103-4: Postgres rejects a role value outside the enum."""
    with postgres_write_connection.cursor() as cur:
        with pytest.raises(psycopg2.errors.InvalidTextRepresentation):
            cur.execute(
                """
                INSERT INTO users (id, email, password_hash, role, display_name, active)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    str(uuid.uuid4()),
                    "test103-invalid-role@example.com",
                    "fake-hash",
                    "SUPERUSER",
                    "Bad Role User",
                    True,
                ),
            )


@pytest.mark.parametrize("role", EXPECTED_ROLES)
def test_valid_role_insert_succeeds(postgres_write_connection, role):
    """QA-103-5: Postgres accepts each valid user_role enum value."""
    email = f"test103-valid-{role}@example.com"

    with postgres_write_connection.cursor() as cur:
        cur.execute(
            """
            INSERT INTO users (id, email, password_hash, role, display_name, active)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                str(uuid.uuid4()),
                email,
                "fake-hash",
                role,
                f"Valid {role} User",
                True,
            ),
        )
        assert cur.rowcount == 1

        cur.execute("SELECT role FROM users WHERE email = %s", (email,))
        assert cur.fetchone() == (role,)


def test_duplicate_email_insert_fails(postgres_write_connection):
    """QA-103-6: Postgres rejects a duplicate email address."""
    email = "test103-duplicate-email@example.com"

    with postgres_write_connection.cursor() as cur:
        cur.execute(
            """
            INSERT INTO users (id, email, password_hash, role, display_name, active)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                str(uuid.uuid4()),
                email,
                "fake-hash",
                "ANALYST",
                "Duplicate Email User",
                True,
            ),
        )
        assert cur.rowcount == 1

        with pytest.raises(psycopg2.errors.UniqueViolation):
            cur.execute(
                """
                INSERT INTO users (id, email, password_hash, role, display_name, active)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    str(uuid.uuid4()),
                    email,
                    "fake-hash",
                    "ANALYST",
                    "Duplicate Email User 2",
                    True,
                ),
            )
