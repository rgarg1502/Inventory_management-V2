from typing import Annotated
from pydantic import Field

NameStr = Annotated[
    str,
    Field(
        min_length=2,
        max_length=100
    )
]

optionalDescriptionStr = Annotated[
    str | None,
    Field(
        max_length=500
    )
]


OptionalNameStr = Annotated[
    str | None,
    Field(
        min_length=2,
        max_length=100
    )
]


DescriptionStr = Annotated[
    str,
    Field(
        max_length=500
    )
]
