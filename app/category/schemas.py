from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.core.types import NameStr, optionalDescriptionStr, OptionalNameStr


class CategoryBase(BaseModel):
    name: NameStr

    description: optionalDescriptionStr = None

    model_config = ConfigDict(
        str_strip_whitespace=True
    )


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: OptionalNameStr = None

    description: optionalDescriptionStr = None

    model_config = ConfigDict(
        str_strip_whitespace=True
    )


class CategoryResponse(CategoryBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
