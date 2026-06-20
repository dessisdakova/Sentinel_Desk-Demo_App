"""Alerts and alert_events tables with enums and indexes.

Revision ID: 20260613_0002
Revises: 20260523_0001
Create Date: 2026-06-13

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "20260613_0002"
down_revision: Union[str, None] = "20260523_0001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

alert_source_enum = postgresql.ENUM(
    "EDR",
    "IDS",
    "PHISHING_SIM",
    "USER_REPORT",
    "THREAT_INTEL_FEED",
    name="alert_source",
    create_type=False,
)

alert_severity_enum = postgresql.ENUM(
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
    name="alert_severity",
    create_type=False,
)

alert_status_enum = postgresql.ENUM(
    "NEW",
    "TRIAGING",
    "FALSE_POSITIVE",
    "TRUE_POSITIVE",
    "ESCALATED",
    "CLOSED",
    "MERGED",
    name="alert_status",
    create_type=False,
)

enrichment_status_enum = postgresql.ENUM(
    "PENDING",
    "COMPLETE",
    name="enrichment_status",
    create_type=False,
)


def upgrade() -> None:
    bind = op.get_bind()
    alert_source_enum.create(bind, checkfirst=True)
    alert_severity_enum.create(bind, checkfirst=True)
    alert_status_enum.create(bind, checkfirst=True)
    enrichment_status_enum.create(bind, checkfirst=True)

    op.create_table(
        "alerts",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("external_id", sa.String(length=255), nullable=False),
        sa.Column("source", alert_source_enum, nullable=False),
        sa.Column("severity", alert_severity_enum, nullable=False),
        sa.Column(
            "status",
            alert_status_enum,
            nullable=False,
            server_default=sa.text("'NEW'::alert_status"),
        ),
        sa.Column(
            "enrichment_status",
            enrichment_status_enum,
            nullable=False,
            server_default=sa.text("'PENDING'::enrichment_status"),
        ),
        sa.Column("title", sa.String(length=500), nullable=False),
        sa.Column(
            "ioc_list",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
            server_default=sa.text("'[]'::jsonb"),
        ),
        sa.Column("assigned_to_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("sla_due_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["assigned_to_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_alerts_external_id", "alerts", ["external_id"], unique=True)
    op.create_index(
        "ix_alerts_status_severity_created_at",
        "alerts",
        ["status", "severity", sa.text("created_at DESC")],
    )
    op.create_index("ix_alerts_assigned_to_id", "alerts", ["assigned_to_id"])

    op.create_table(
        "alert_events",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("alert_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("event_type", sa.String(length=100), nullable=False),
        sa.Column(
            "payload",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
        ),
        sa.Column("created_by", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["alert_id"], ["alerts.id"]),
        sa.ForeignKeyConstraint(["created_by"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_alert_events_alert_id", "alert_events", ["alert_id"])


def downgrade() -> None:
    op.drop_index("ix_alert_events_alert_id", table_name="alert_events")
    op.drop_table("alert_events")

    op.drop_index("ix_alerts_assigned_to_id", table_name="alerts")
    op.drop_index("ix_alerts_status_severity_created_at", table_name="alerts")
    op.drop_index("ix_alerts_external_id", table_name="alerts")
    op.drop_table("alerts")

    bind = op.get_bind()
    enrichment_status_enum.drop(bind, checkfirst=True)
    alert_status_enum.drop(bind, checkfirst=True)
    alert_severity_enum.drop(bind, checkfirst=True)
    alert_source_enum.drop(bind, checkfirst=True)
