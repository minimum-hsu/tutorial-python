from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import RootModel
from pydantic import StringConstraints

#############################
# Regex Patterns
#############################
import re
PATTERN_EMAIL = re.compile(r"^([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22))*\x40([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d))*$")


#############################
# Typing
#############################
from typing import Annotated

Email = Annotated[str, StringConstraints(
    strip_whitespace=True,
    max_length=320,
    pattern=PATTERN_EMAIL,
)]


#############################
# Models
#############################
class User(BaseModel):
    id_: Annotated[int, Field(
        alias="id",
        title="User ID",
        description="The unique identifier for the user.",
        examples=["integer"],
    )]
    name: Annotated[str, Field(
        title="User Name",
        description="The name of the user.",
        examples=["string"],
    )]
    email: Annotated[Email, Field(
        title="User Email",
        description="The email address of the user.",
        examples=["alice@example.com"],
    )]

    model_config = ConfigDict(
        title="User",
        str_strip_whitespace=True,
        extra="ignore",
        use_enum_values=True,
        validate_assignment=True,
        regex_engine="python-re",
    )

class Users(RootModel[list[User]]):
    model_config = ConfigDict(
        title="Users",
        str_strip_whitespace=True,
        extra="ignore",
        use_enum_values=True,
        validate_assignment=True,
        regex_engine="python-re",
    )
