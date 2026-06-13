import subprocess
from pathlib import Path

import pytest

from tests.constants import SEED_INACTIVE_USER, SEED_USERS

pytestmark = [pytest.mark.integ, pytest.mark.reg]


def test_rerun_seed_does_not_duplicate_users(run_seed_script, postgres_connection):
    """QA-108-1: Re-running scripts.seed does not create duplicate seed users.

    Prerequisite: baseline seed applied at least once before test.
    """
    # Build a tuple of the four canonical seed emails.
    seed_emails = tuple(user["email"] for user in SEED_USERS)

    # The fixture already ran seed; confirm subprocess exited successfully.
    assert run_seed_script.returncode == 0, (
        "Seed script must exit 0 on idempotent re-run. "
        f"stderr={run_seed_script.stderr!r}"
    )

    with postgres_connection.cursor() as cur:
        # Count how many user rows match any of the four seed emails.
        cur.execute(
            "SELECT COUNT(*) FROM users WHERE email IN %s",
            (seed_emails,),
        )
        total_rows = cur.fetchone()[0]

        # Find emails that appear more than once — should be none.
        cur.execute(
            """
            SELECT email, COUNT(*) AS row_count
            FROM users
            WHERE email IN %s
            GROUP BY email
            HAVING COUNT(*) > 1
            """,
            (seed_emails,),
        )
        duplicate_emails = cur.fetchall()

    # AC2: re-run must not add extra rows — still exactly four seed users.
    assert total_rows == len(SEED_USERS), (
        f"Expected {len(SEED_USERS)} seed user rows after re-run, got {total_rows}."
    )

    # Stronger check: no seed email may appear twice in the users table.
    assert duplicate_emails == [], (
        f"Duplicate seed emails found after re-run: {duplicate_emails!r}"
    )


def test_inactive_seed_user_has_active_false(postgres_connection):
    """QA-108-2: inactive@demo.local is seeded with active = false (AC1).

    Prerequisite: baseline seed applied at least once before test.
    """
    # Query the active flag for the inactive seed persona only.
    with postgres_connection.cursor() as cur:
        cur.execute(
            "SELECT active FROM users WHERE email = %s",
            (SEED_INACTIVE_USER["email"],),
        )
        row = cur.fetchone()

    # Row must exist — seed created this user.
    assert row is not None, (
        f"No user row found for {SEED_INACTIVE_USER['email']!r}."
    )

    # inactive@demo.local must be stored with `active = false`.
    assert row[0] is False, (
        f"Expected active=False for {SEED_INACTIVE_USER['email']!r}, got {row[0]!r}."
    )


@pytest.mark.parametrize("user", [
    pytest.param(SEED_USERS[0], id="analyst"),
    pytest.param(SEED_USERS[1], id="lead"),
    pytest.param(SEED_USERS[2], id="admin"),
    pytest.param(SEED_USERS[3], id="inactive"),
])
def test_seed_user_password_hash_is_bcrypt(postgres_connection, user):
    """QA-108-3: Seed stores bcrypt password_hash, not plaintext (AC1).

    Prerequisite: baseline seed applied at least once before test.
    """
    # Read the stored hash for this seed email.
    with postgres_connection.cursor() as cur:
        cur.execute(
            "SELECT password_hash FROM users WHERE email = %s",
            (user["email"],),
        )
        row = cur.fetchone()

    # Row must exist — seed created this user.
    assert row is not None, f"No user row found for {user['email']!r}."

    password_hash = row[0]

    # Hash must be present and non-empty.
    assert password_hash, f"password_hash must not be empty for {user['email']!r}."

    # bcrypt hashes start with $2b$ (or $2a$ / $2y$); plaintext would not.
    assert password_hash.startswith("$2b$"), (
        f"Expected bcrypt hash for {user['email']!r}, got {password_hash!r}."
    )

    # Plaintext password must never appear in the hash column.
    assert user["password"] not in password_hash, (
        f"password_hash looks like plaintext for {user['email']!r}."
    )


def test_seed_users_count_is_four(postgres_connection):
    """QA-108-4: Exactly four baseline seed users exist in the database.

    Prerequisite: baseline seed applied at least once before test.
    """
    # Collect all four canonical seed emails.
    seed_emails = tuple(user["email"] for user in SEED_USERS)

    # Count rows matching any seed email.
    with postgres_connection.cursor() as cur:
        cur.execute(
            "SELECT COUNT(*) FROM users WHERE email IN %s",
            (seed_emails,),
        )
        total_rows = cur.fetchone()[0]

    # Seed must create exactly four baseline users.
    assert total_rows == len(SEED_USERS), (
        f"Expected {len(SEED_USERS)} seed user rows, got {total_rows}."
    )


def test_seed_rerun_does_not_change_row_count(
    postgres_connection, require_infrastructure):
    """QA-108-5: Second seed run inserts zero additional seed user rows.

    Prerequisite: baseline seed applied at least once before test.
    Compares row count before and after a second `scripts.seed` run.
    """
    # Same email set used across all SENT-108 integration tests.
    seed_emails = tuple(user["email"] for user in SEED_USERS)

    # Repo root: tests/integration/infrastructure/test_seed_users.py -> four parents up.
    repo_root = Path(__file__).resolve().parent.parent.parent.parent

    with postgres_connection.cursor() as cur:
        # Snapshot row count before the second seed run.
        cur.execute(
            "SELECT COUNT(*) FROM users WHERE email IN %s",
            (seed_emails,),
        )
        count_before = cur.fetchone()[0]

    # Run seed again (same command as run_seed_script fixture).
    result = subprocess.run(
        ["docker", "compose", "exec", "-T", "api", "python", "-m", "scripts.seed"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
        timeout=60,
    )

    # Seed CLI must succeed on idempotent re-run.
    assert result.returncode == 0, (
        f"Seed script must exit 0. stderr={result.stderr!r}"
    )

    with postgres_connection.cursor() as cur:
        # Snapshot row count after the second seed run.
        cur.execute(
            "SELECT COUNT(*) FROM users WHERE email IN %s",
            (seed_emails,),
        )
        count_after = cur.fetchone()[0]

    # Re-run must not insert any new seed user rows.
    assert count_after == count_before, (
        f"Seed re-run changed row count: before={count_before}, after={count_after}."
    )
