"""Alert ORM model and related enums."""

import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, String, func, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class AlertSource(enum.StrEnum):
    """Alert origin system — CONSTITUTION §5.3."""

    EDR = "EDR"
    IDS = "IDS"
    PHISHING_SIM = "PHISHING_SIM"
    USER_REPORT = "USER_REPORT"
    THREAT_INTEL_FEED = "THREAT_INTEL_FEED"


class AlertSeverity(enum.StrEnum):
    """Alert severity — CONSTITUTION §5.3."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class AlertStatus(enum.StrEnum):
    """SOC disposition on an alert — CONSTITUTION §5.2."""

    NEW = "NEW"
    TRIAGING = "TRIAGING"
    FALSE_POSITIVE = "FALSE_POSITIVE"
    TRUE_POSITIVE = "TRUE_POSITIVE"
    ESCALATED = "ESCALATED"
    CLOSED = "CLOSED"
    MERGED = "MERGED"


class EnrichmentStatus(enum.StrEnum):
    """Async worker enrichment lifecycle — separate from AlertStatus."""

    PENDING = "PENDING"
    COMPLETE = "COMPLETE"


class Alert(Base):
    """Ingested security event (triage, enrichment, audit in later epics)."""

    __tablename__ = "alerts"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    external_id: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    source: Mapped[AlertSource] = mapped_column(
        Enum(
            AlertSource,
            name="alert_source",
            native_enum=True,
            values_callable=lambda sources: [source.value for source in sources],
        ),
        nullable=False,
    )
    severity: Mapped[AlertSeverity] = mapped_column(
        Enum(
            AlertSeverity,
            name="alert_severity",
            native_enum=True,
            values_callable=lambda severities: [severity.value for severity in severities],
        ),
        nullable=False,
    )
    status: Mapped[AlertStatus] = mapped_column(
        Enum(
            AlertStatus,
            name="alert_status",
            native_enum=True,
            values_callable=lambda statuses: [status.value for status in statuses],
        ),
        nullable=False,
        default=AlertStatus.NEW,
    )
    enrichment_status: Mapped[EnrichmentStatus] = mapped_column(
        Enum(
            EnrichmentStatus,
            name="enrichment_status",
            native_enum=True,
            values_callable=lambda statuses: [status.value for status in statuses],
        ),
        nullable=False,
        default=EnrichmentStatus.PENDING,
    )
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    ioc_list: Mapped[list[dict[str, str]]] = mapped_column(
        JSONB,
        nullable=False,
        server_default=text("'[]'::jsonb"),
    )
    assigned_to_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True,
    )
    sla_due_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
