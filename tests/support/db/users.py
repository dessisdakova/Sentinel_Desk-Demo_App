import psycopg2.extensions


_ALLOWED_FIELDS = frozenset({"id", "email", "active", "password_hash", "role"})

def _validate_field(field: str) -> None:
    if field not in _ALLOWED_FIELDS:
        raise ValueError(f"Unsupported field: {field!r}")

def get_user_field_by_email(
    conn: psycopg2.extensions.connection,
    email: str,
    field: str,
) -> object | None:
    """Return one column value for a user row, or None if missing."""
    _validate_field(field)
    with conn.cursor() as cur:
        cur.execute(f"SELECT {field} FROM users WHERE email = %s", (email,))
        row = cur.fetchone()
    return None if row is None else row[0]


def get_user_email_by_id(
    conn: psycopg2.extensions.connection,
    user_id: str,
) -> str | None:
    with conn.cursor() as cur:
        cur.execute("SELECT email FROM users WHERE id = %s", (user_id,))
        row = cur.fetchone()
    return None if row is None else row[0]


def count_users_with_emails(
    conn: psycopg2.extensions.connection,
    emails: tuple[str, ...],
) -> int:
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM users WHERE email IN %s", (emails,))
        return cur.fetchone()[0]