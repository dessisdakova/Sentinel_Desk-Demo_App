"""Baseline seed data — users only (SENT-108).

Re-run safely: existing rows are skipped by email (idempotent).
"""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import AsyncSessionLocal
from app.core.security import hash_password
from app.models.user import User, UserRole
from app.services.user_service import get_user_by_email

logger = logging.getLogger("sentineldesk.seed")

SEED_PASSWORD = "DemoPass123!"


@dataclass(frozen=True, slots=True)
class SeedUserSpec:
    """One baseline portal user from TEST_DATA.md §2."""

    email: str
    role: UserRole
    display_name: str
    active: bool


BASELINE_USERS: tuple[SeedUserSpec, ...] = (
    SeedUserSpec(
        email="analyst@demo.local",
        role=UserRole.ANALYST,
        display_name="Alex Analyst",
        active=True,
    ),
    SeedUserSpec(
        email="lead@demo.local",
        role=UserRole.LEAD,
        display_name="Jordan Lead",
        active=True,
    ),
    SeedUserSpec(
        email="admin@demo.local",
        role=UserRole.ADMIN,
        display_name="Sam Admin",
        active=True,
    ),
    SeedUserSpec(
        email="inactive@demo.local",
        role=UserRole.ANALYST,
        display_name="Dana Inactive",
        active=False,
    ),
)


async def seed_users(session: AsyncSession) -> tuple[int, int]:
    """Insert baseline users that are not already present.

    Returns (inserted_count, skipped_count).
    """
    inserted = 0
    skipped = 0

    for spec in BASELINE_USERS:
        existing = await get_user_by_email(session, spec.email)
        if existing is not None:
            logger.info("skip existing user email=%s", spec.email)
            skipped += 1
            continue

        session.add(
            User(
                email=spec.email,
                password_hash=hash_password(SEED_PASSWORD),
                role=spec.role,
                display_name=spec.display_name,
                active=spec.active,
            )
        )
        logger.info(
            "insert user email=%s role=%s active=%s",
            spec.email,
            spec.role.value,
            spec.active,
        )
        inserted += 1

    await session.commit()
    return inserted, skipped


async def run_seed() -> None:
    """Open a DB session and seed baseline users."""
    async with AsyncSessionLocal() as session:
        inserted, skipped = await seed_users(session)
        logger.info(
            "seed complete inserted=%s skipped=%s total=%s",
            inserted,
            skipped,
            len(BASELINE_USERS),
        )


def main() -> None:
    """CLI entrypoint for ``python -m scripts.seed``."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )
    asyncio.run(run_seed())


if __name__ == "__main__":
    main()
