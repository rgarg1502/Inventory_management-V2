from sqlalchemy.orm import mapped_column, Mapped
from app.database.base import BaseModel
from sqlalchemy import String


class Category(BaseModel):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )
