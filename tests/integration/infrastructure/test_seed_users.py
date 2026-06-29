import subprocess
from pathlib import Path

import pytest

from tests.constants import SEED_INACTIVE_USER, SEED_USERS
from tests.support.db.users import count_users_with_emails, get_user_field_by_email

pytestmark = [pytest.mark.integ, pytest.mark.reg]


def test_rerun_seed_does_not_duplicate_users(run_seed_script, postgres_connection):
    """QA-108-1: Re-running scripts.seed does not create duplicate seed users.

    Prerequisite: baseline seed applied at least once before test.
    """
    seed_emails = tuple(user["email"] for user in SEED_USERS)

    assert run_seed_script.returncode == 0, (
        "Seed script must exit 0 on idempotent re-run. "
        f"stderr={run_seed_script.stderr!r}"
    )

    total_rows = count_users_with_emails(postgres_connection, seed_emails)

    with postgres_connection.cursor() as cur:
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

    assert total_rows == len(SEED_USERS), (
        f"Expected {len(SEED_USERS)} seed user rows after re-run, got {total_rows}."
    )
    assert duplicate_emails == [], (
        f"Duplicate seed emails found after re-run: {duplicate_emails!r}"
    )


def test_inactive_seed_user_has_active_false(postgres_connection):
    """QA-108-2: inactive@demo.local is seeded with active = false (AC1).

    Prerequisite: baseline seed applied at least once before test.
    """
    active = get_user_field_by_email(
        postgres_connection, SEED_INACTIVE_USER["email"], "active"
    )

    assert active is not None, (
        f"No user row found for {SEED_INACTIVE_USER['email']!r}."
    )
    assert active is False, (
        f"Expected active=False for {SEED_INACTIVE_USER['email']!r}, got {active!r}."
    )


@pytest.mark.parametrize("user", [
    pytest.param(SEED_USERS[0], id="analyst"),
    pytest.param(SEED_USERS[1], id="lead"),
    pytest.param(SEED_USERS[2], id="admin"),
    pytest.param(SEED_USERS[3], id="inactive"),
])
def test_seed_user_password_hash_is_bcrypt(postgres_connection, user, password_for):
    """QA-108-3: Seed stores bcrypt password_hash, not plaintext (AC1).

    Prerequisite: baseline seed applied at least once before test.
    """
    password_hash = get_user_field_by_email(
        postgres_connection, user["email"], "password_hash"
    )

    assert password_hash is not None, f"No user row found for {user['email']!r}."
    assert password_hash, f"password_hash must not be empty for {user['email']!r}."
    assert password_hash.startswith("$2b$"), (
        f"Expected bcrypt hash for {user['email']!r}, got {password_hash!r}."
    )
    assert password_for(user["key"]) not in password_hash, (
        f"password_hash looks like plaintext for {user['email']!r}."
    )


def test_seed_users_count_is_four(postgres_connection):
    """QA-108-4: Exactly four baseline seed users exist in the database.

    Prerequisite: baseline seed applied at least once before test.
    """
    seed_emails = tuple(user["email"] for user in SEED_USERS)
    total_rows = count_users_with_emails(postgres_connection, seed_emails)

    assert total_rows == len(SEED_USERS), (
        f"Expected {len(SEED_USERS)} seed user rows, got {total_rows}."
    )


def test_seed_rerun_does_not_change_row_count(
    postgres_connection, require_infrastructure
):
    """QA-108-5: Second seed run inserts zero additional seed user rows.

    Prerequisite: baseline seed applied at least once before test.
    Compares row count before and after a second `scripts.seed` run.
    """
    seed_emails = tuple(user["email"] for user in SEED_USERS)
    repo_root = Path(__file__).resolve().parent.parent.parent.parent

    count_before = count_users_with_emails(postgres_connection, seed_emails)

    result = subprocess.run(
        ["docker", "compose", "exec", "-T", "api", "python", "-m", "scripts.seed"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
        timeout=60,
    )

    assert result.returncode == 0, (
        f"Seed script must exit 0. stderr={result.stderr!r}"
    )

    count_after = count_users_with_emails(postgres_connection, seed_emails)

    assert count_after == count_before, (
        f"Seed re-run changed row count: before={count_before}, after={count_after}."
    )
