from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import BaseModel


class Supplier(BaseModel):
    __tablename__ = "suppliers"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )
    address:Mapped[str | None] = mapped_column(
        String(500)
    )
    contact_person:Mapped[str | None] = mapped_column(
        String(100)
    )
    mobile_no: Mapped[str | None] = mapped_column(
        String(20)
    )
    email: Mapped[str | None] = mapped_column(
        String(255)
    )