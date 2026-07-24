from sqlalchemy.orm import Mapped,mapped_column
from app.database.base import BaseModel
from sqlalchemy import String,Boolean

class User(BaseModel):
    __tablename__ = "users"

  
    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
        )
    email:Mapped[str] = mapped_column(
        String(255),
        index=True,
        unique=True,
        nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    mobile_no: Mapped[str | None] = mapped_column(
        String(15),
        default=None,
        nullable = True
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )