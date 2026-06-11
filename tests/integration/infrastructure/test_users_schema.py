import uuid

import psycopg2
import pytest

pytestmark = [pytest.mark.integ, pytest.mark.reg]

EXPECTED_ROLES = ("ANALYST", "LEAD", "ADMIN")


@pytest.mark.smoke
def test_users_table_has_expected_columns(postgres_connection):
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

    # Ask database which columns exist on public.users and how each is defined.
    with postgres_connection.cursor() as cur:
        cur.execute(
            """
            SELECT column_name, data_type, udt_name, is_nullable
            FROM information_schema.columns
            WHERE table_schema = 'public' AND table_name = 'users'
            ORDER BY ordinal_position
            """
        )
        # Build a lookup: column name -> (data_type, udt_name, is_nullable).
        cols = {row[0]: (row[1], row[2], row[3]) for row in cur.fetchall()}

    # No missing or extra columns compared to the schema.
    assert set(cols) == set(expected_columns), (
        "Users table columns mismatch." /
        f"expected={set(expected_columns)!r}, actual={set(cols)!r}")

    # Each column must have the expected type and must not allow NULL.
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


def test_users_table_has_primary_key_on_id(postgres_connection):
    """QA-103-1: users.id is the primary key."""
    # Look up which column(s) Postgres marked as the table's primary key.
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

    # Exactly one primary key column: id.
    assert pk_columns == {"id"}, (
        f"Users table primary key must be on id, got {pk_columns!r}")


def test_users_email_has_unique_index(postgres_connection):
    """QA-103-1: Email cannot be duplicated (unique index on email)."""
    # List all indexes on public.users.
    with postgres_connection.cursor() as cur:
        cur.execute(
            """
            SELECT indexname, indexdef
            FROM pg_indexes
            WHERE schemaname = 'public' AND tablename = 'users'
            """
        )
        indexes = {row[0]: row[1] for row in cur.fetchall()}

    # Migration must create a named unique index on email.
    assert "ix_users_email" in indexes, (
        f"unique index ix_users_email missing; indexes={list(indexes)!r}"
    )

    # Confirm that index is UNIQUE and targets the email column.
    email_index_def = indexes["ix_users_email"].lower()
    assert "unique" in email_index_def and "email" in email_index_def, (
        "ix_users_email must be a UNIQUE index on email"
    )


def test_user_role_enum_has_expected_values(postgres_connection):
    """QA-103-3: user_role enum contains exactly ANALYST, LEAD, ADMIN."""
    # Read the allowed labels for the user_role enum type.
    with postgres_connection.cursor() as cur:
        cur.execute(
            """
            SELECT e.enumlabel
            FROM pg_type t
            JOIN pg_enum e ON t.oid = e.enumtypid
            WHERE t.typname = 'user_role'
            ORDER BY e.enumsortorder
            """
        )
        roles = tuple(row[0] for row in cur.fetchall())

    assert roles == EXPECTED_ROLES


def test_invalid_role_insert_fails(postgres_write_connection):
    """QA-103-4: Postgres rejects a role value outside the enum."""
    with postgres_write_connection.cursor() as cur:
        # Try to insert a row with an invalid role — Postgres must reject it.
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
    email = f"test103-valid-{role.lower()}@example.com"

    with postgres_write_connection.cursor() as cur:
        # Insert one row using a valid enum value (ANALYST, LEAD, or ADMIN).
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

        # Read the row back in the same transaction to confirm role was stored.
        cur.execute("SELECT role FROM users WHERE email = %s", (email,))

        assert cur.fetchone() == (role,)


def test_duplicate_email_insert_fails(postgres_write_connection):
    """QA-103-6: Postgres rejects a duplicate email address."""
    email = "test103-duplicate-email@example.com"

    with postgres_write_connection.cursor() as cur:
        # First insert with this email should succeed.
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

        # Second insert with the same email must hit the unique index.
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
