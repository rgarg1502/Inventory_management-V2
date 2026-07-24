from pydantic import BaseModel,ConfigDict, EmailStr, Field
from typing import Annotated
from datetime import datetime

class UserCreate(BaseModel):
    full_name: Annotated[str, Field(
        min_length=2,
        max_length=255
    )]
    email: EmailStr
    password:Annotated[
        str,
        Field(validation_alias="hasehd_password",min_length=8, max_length=128)
    ]
    mobile_no:Annotated[str | None,Field(min_length=10,max_length=15)] = None
    is_superuser:bool 

class UserUpdate(BaseModel):
    full_name : Annotated[str | None, Field(
        min_length=2,
        max_length=255
    )] = None
    mobile_no: Annotated[str | None,Field(min_length=10,max_length=15)] = None
    # is_superuser: bool | None = None

class UserRepsonse(BaseModel):
    id:int
    created_at: datetime 
    updated_at: datetime
    is_active: bool
    email: EmailStr
    mobile_no: str | None
    is_superuser:bool
    full_name: str

    model_config = ConfigDict(from_attributes=True)