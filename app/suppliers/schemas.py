


from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class SupplierCreate(BaseModel):
    name: Annotated[str, Field(min_length=2,max_length=100)] 
    address: Annotated[str|None, Field(max_length=500)] = None
    contact_person:Annotated[str|None, Field(max_length=100)] = None
    mobile_no: Annotated[str|None, Field(max_length=20)] = None
    email:EmailStr | None = None

    model_config = ConfigDict(
        str_strip_whitespace=True
    )

class SupplierUpdate(BaseModel):
    ame: Annotated[str, Field(min_length=2,max_length=100)] = None
    address: Annotated[str|None, Field(max_length=500)] = None
    contact_person:Annotated[str|None, Field(max_length=100)] = None
    mobile_no: Annotated[str|None, Field(max_length=20)] = None
    email:EmailStr | None = None

    model_config = ConfigDict(
        str_strip_whitespace=True
    )

class SupplierResponse(BaseModel):
    id:int
    name:str
    address: str | None
    contact_person:str | None
    mobile_no:str | None
    email:EmailStr | None
    is_active:bool
    created_at:datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )