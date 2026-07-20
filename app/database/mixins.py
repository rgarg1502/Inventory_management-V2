from sqlalchemy import BigInteger, DateTime, Boolean, Identity
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime, timezone


class IDMixin:
    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(),
        primary_key=True
    )


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default_factory=lambda: DateTime.now(timezone.utc),
        onupdate=lambda: DateTime.now(timezone.utc),
        nullable=False
    )


class ActiveMixin:
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )
