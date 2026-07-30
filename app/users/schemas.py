from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Annotated
from datetime import datetime


class UserCreate(BaseModel):
    full_name: Annotated[str, Field(
        min_length=2,
        max_length=255
    )]
    email: EmailStr
    hashed_password: Annotated[
        str,
        Field(validation_alias="password", min_length=8, max_length=128)
    ]
    mobile_no: Annotated[str | None, Field(
        min_length=10, max_length=15)] = None
    is_superuser: bool | None = False


class UserUpdate(BaseModel):
    full_name: Annotated[str | None, Field(
        min_length=2,
        max_length=255
    )] = None
    mobile_no: Annotated[str | None, Field(
        min_length=10, max_length=15)] = None
    is_superuser: bool | None = None
    is_active: bool | None = None

class UserLogin(BaseModel):
    email:EmailStr
    password: Annotated[str, Field(
        min_length=8, max_length=15
    )
    ]

class ChangePassword(BaseModel):
    old_password: Annotated[str, Field(
        min_length=8, max_length=15
    )
    ]
    new_password: Annotated[str, Field(
        min_length=8, max_length=15
    )
    ]

class ResetPassword(BaseModel):
    new_password: Annotated[str, Field(
        min_length=8, max_length=15
    )]

class UserResponse(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool
    email: EmailStr
    mobile_no: str | None
    is_superuser: bool
    full_name: str

    model_config = ConfigDict(from_attributes=True)


