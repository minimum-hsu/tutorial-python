from typing import Annotated
from pydantic import BaseModel
from pydantic import Field

class User(BaseModel):
    name: Annotated[str, Field(max_length=100)]
    age: Annotated[int, Field(ge=0)]
    email: Annotated[str, Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')]
