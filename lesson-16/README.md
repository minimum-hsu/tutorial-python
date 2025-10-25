# Lesson 16 - Data Models Evolution  <!-- omit in toc -->

This lesson covers the evolution of data modeling in Python, from basic dictionaries to modern data validation frameworks, demonstrating various approaches to structure and validate data.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. Dictionary-based Data Model](#01-dictionary-based-data-model)
  - [02. namedtuple Data Model](#02-namedtuple-data-model)
  - [03. Traditional Class Data Model](#03-traditional-class-data-model)
  - [04. Dataclass Data Model](#04-dataclass-data-model)
  - [05. Pydantic Data Model with Validation](#05-pydantic-data-model-with-validation)
- [Data Model Comparison](#data-model-comparison)
  - [Feature Comparison](#feature-comparison)
  - [When to Use Each](#when-to-use-each)
    - [Use Dictionary when:](#use-dictionary-when)
    - [Use namedtuple when:](#use-namedtuple-when)
    - [Use Traditional Classes when:](#use-traditional-classes-when)
    - [Use dataclasses when:](#use-dataclasses-when)
    - [Use Pydantic when:](#use-pydantic-when)
- [Advanced Data Modeling Patterns](#advanced-data-modeling-patterns)
  - [Enhanced dataclass Features](#enhanced-dataclass-features)
  - [Advanced Pydantic Features](#advanced-pydantic-features)
  - [Data Model with Methods](#data-model-with-methods)
- [Practical Examples](#practical-examples)
  - [User Management System](#user-management-system)
  - [Configuration Management](#configuration-management)
- [How to Run Examples](#how-to-run-examples)
  - [Dictionary Example](#dictionary-example)
  - [namedtuple Example](#namedtuple-example)
  - [Traditional Class Example](#traditional-class-example)
  - [Dataclass Example](#dataclass-example)
  - [Pydantic Example](#pydantic-example)
- [Validation and Error Handling](#validation-and-error-handling)
  - [Pydantic Validation Examples](#pydantic-validation-examples)
  - [Custom Validation](#custom-validation)
- [Best Practices](#best-practices)
  - [1. **Choose the Right Data Model**](#1-choose-the-right-data-model)
  - [2. **Use Type Hints Consistently**](#2-use-type-hints-consistently)
  - [3. **Validate Early and Often**](#3-validate-early-and-often)
  - [4. **Use Immutable Data When Possible**](#4-use-immutable-data-when-possible)
  - [5. **Handle Serialization Properly**](#5-handle-serialization-properly)
- [Performance Considerations](#performance-considerations)
  - [Memory Usage Comparison](#memory-usage-comparison)
- [Practice Suggestions](#practice-suggestions)
- [Common Pitfalls](#common-pitfalls)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Understand different data modeling approaches in Python
- Learn the evolution from dictionaries to modern data models
- Master namedtuples for simple structured data
- Understand traditional classes for data modeling
- Learn dataclasses for modern Python data structures
- Master Pydantic for data validation and serialization
- Compare different approaches and their use cases
- Choose the right tool for specific scenarios

## Course Content

### 01. Dictionary-based Data Model
**File:** `01/main.py`

Learn basic data modeling using Python dictionaries:

```python
#!/usr/bin/env python3

user = {
    'name': 'Alice',
    'age': 30,
    'email': 'alice@example.com'
}

if __name__ == '__main__':
    print('User Information:')
    print(f'name: {user["name"]}')
    print(f'age: {user["age"]}')
    print(f'email: {user["email"]}')
```

**Key Concepts:**
- Simple key-value data storage
- Flexible structure, can add/remove fields
- No type checking or validation
- Access via string keys (`user["name"]`)
- Mutable and dynamic
- Risk of typos in key names

### 02. namedtuple Data Model
**Files:** `02/main.py`, `02/model.py`

Learn structured data using namedtuples:

**Data Model (`02/model.py`)**
```python
from collections import namedtuple

User = namedtuple('User', ['name', 'age', 'email'])
```

**Application Code (`02/main.py`)**
```python
#!/usr/bin/env python3

from model import User

if __name__ == '__main__':
    user = User(name='Alice', age=30, email='alice@example.com')
    print('User Information:')
    print(f'name: {user.name}')
    print(f'age: {user.age}')
    print(f'email: {user.email}')
```

**Key Concepts:**
- Immutable data structures
- Attribute access with dot notation
- Memory efficient
- Built-in `__repr__` and comparison methods
- Tuple-like behavior with named fields
- Fixed structure, cannot add fields

### 03. Traditional Class Data Model
**Files:** `03/main.py`, `03/model.py`

Learn object-oriented data modeling with traditional classes:

**Data Model (`03/model.py`)**
```python
class User:

    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email
```

**Application Code (`03/main.py`)**
```python
#!/usr/bin/env python3

from model import User

if __name__ == '__main__':
    user = User(name='Alice', age=30, email='alice@example.com')
    print('User Information:')
    print(f'name: {user.name}')
    print(f'age: {user.age}')
    print(f'email: {user.email}')
```

**Key Concepts:**
- Full object-oriented capabilities
- Mutable by default
- Can add methods and properties
- Type hints for documentation
- Manual implementation of special methods
- Maximum flexibility and control

### 04. Dataclass Data Model
**Files:** `04/main.py`, `04/model.py`

Learn modern Python data modeling with dataclasses:

**Data Model (`04/model.py`)**
```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str
```

**Application Code (`04/main.py`)**
```python
#!/usr/bin/env python3

from model import User

if __name__ == '__main__':
    user = User(name='Alice', age=30, email='alice@example.com')
    print('User Information:')
    print(f'name: {user.name}')
    print(f'age: {user.age}')
    print(f'email: {user.email}')
```

**Key Concepts:**
- Automatic generation of `__init__`, `__repr__`, `__eq__`
- Type annotations are required
- Less boilerplate than traditional classes
- Can be made immutable with `frozen=True`
- Support for default values and field customization
- Python 3.7+ feature

### 05. Pydantic Data Model with Validation
**Files:** `05/main.py`, `05/model.py`, `05/requirements.txt`

Learn advanced data modeling with validation using Pydantic:

**Requirements (`05/requirements.txt`)**
```pip-requirements
pydantic
```

**Data Model (`05/model.py`)**
```python
from typing import Annotated
from pydantic import BaseModel
from pydantic import Field

class User(BaseModel):
    name: Annotated[str, Field(max_length=100)]
    age: Annotated[int, Field(ge=0)]
    email: Annotated[str, Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')]
```

**Application Code (`05/main.py`)**
```python
#!/usr/bin/env python3

from model import User

if __name__ == '__main__':
    user = User(name='Alice', age=30, email='alice@example.com')
    print('User Information:')
    print(f'name: {user.name}')
    print(f'age: {user.age}')
    print(f'email: {user.email}')
```

**Key Concepts:**
- Automatic data validation and type conversion
- Rich validation rules with `Field()`
- JSON serialization/deserialization
- Error handling for invalid data
- Integration with FastAPI and other frameworks
- Runtime type checking

## Data Model Comparison

### Feature Comparison

| Feature | Dict | namedtuple | Class | dataclass | Pydantic |
|---------|------|------------|-------|-----------|----------|
| **Mutability** | Mutable | Immutable | Mutable | Configurable | Immutable |
| **Type Hints** | No | No | Optional | Required | Required |
| **Validation** | No | No | Manual | No | Automatic |
| **Memory** | High | Low | Medium | Medium | Medium |
| **Boilerplate** | None | Low | High | Low | Low |
| **Methods** | No | Limited | Full | Auto-generated | Rich |
| **JSON Support** | Manual | Manual | Manual | Manual | Built-in |
| **Performance** | Fast | Fastest | Fast | Fast | Slower |

### When to Use Each

#### Use Dictionary when:
- Prototyping or simple scripts
- Dynamic structure needed
- Minimal requirements
- Data comes from external sources (JSON, APIs)

#### Use namedtuple when:
- Need immutable records
- Memory efficiency is important
- Simple data containers
- Replacing tuples with named access

#### Use Traditional Classes when:
- Need complex business logic
- Require inheritance
- Need custom methods and properties
- Maximum control required

#### Use dataclasses when:
- Modern Python (3.7+) projects
- Want automatic method generation
- Need type hints
- Don't need validation

#### Use Pydantic when:
- Data validation is critical
- Working with APIs (FastAPI, etc.)
- Need JSON serialization
- Runtime type checking required

## Advanced Data Modeling Patterns

### Enhanced dataclass Features
```python
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass(frozen=True)  # Immutable
class User:
    name: str
    age: int
    email: str
    created_at: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)
    active: bool = True

    def __post_init__(self):
        # Validation in post_init
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        if '@' not in self.email:
            raise ValueError("Invalid email format")
```

### Advanced Pydantic Features
```python
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum

class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    BANNED = "banned"

class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=0, le=150)
    email: str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    status: UserStatus = UserStatus.ACTIVE
    created_at: datetime = Field(default_factory=datetime.now)
    tags: List[str] = []

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.title()

    @validator('email')
    def email_must_be_lowercase(cls, v):
        return v.lower()

    @root_validator
    def validate_user(cls, values):
        name = values.get('name')
        age = values.get('age')

        if name == 'Admin' and age < 18:
            raise ValueError('Admin must be at least 18')

        return values

    class Config:
        # Enable ORM mode for database integration
        from_attributes = True
        # Custom JSON encoders
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
```

### Data Model with Methods
```python
from dataclasses import dataclass
from typing import List, Optional
import json

@dataclass
class User:
    name: str
    age: int
    email: str

    def is_adult(self) -> bool:
        return self.age >= 18

    def email_domain(self) -> str:
        return self.email.split('@')[1]

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'age': self.age,
            'email': self.email
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        return cls(**data)

    @classmethod
    def from_json(cls, json_str: str) -> 'User':
        return cls.from_dict(json.loads(json_str))
```

## Practical Examples

### User Management System
```python
from dataclasses import dataclass, field
from typing import List, Optional, Dict
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    MODERATOR = "moderator"

@dataclass
class Permission:
    name: str
    description: str

@dataclass
class User:
    username: str
    email: str
    role: UserRole = UserRole.USER
    created_at: datetime = field(default_factory=datetime.now)
    last_login: Optional[datetime] = None
    permissions: List[Permission] = field(default_factory=list)
    metadata: Dict[str, str] = field(default_factory=dict)

    def add_permission(self, permission: Permission):
        if permission not in self.permissions:
            self.permissions.append(permission)

    def has_permission(self, permission_name: str) -> bool:
        return any(p.name == permission_name for p in self.permissions)

    def login(self):
        self.last_login = datetime.now()

@dataclass
class UserManager:
    users: List[User] = field(default_factory=list)

    def add_user(self, user: User):
        if not any(u.username == user.username for u in self.users):
            self.users.append(user)

    def find_user(self, username: str) -> Optional[User]:
        return next((u for u in self.users if u.username == username), None)

    def get_admins(self) -> List[User]:
        return [u for u in self.users if u.role == UserRole.ADMIN]
```

### Configuration Management
```python
from pydantic import BaseModel, Field, validator
from typing import List, Dict, Optional
import os

class DatabaseConfig(BaseModel):
    host: str = "localhost"
    port: int = Field(5432, gt=0, lt=65536)
    name: str
    username: str
    password: str

    @validator('password')
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v

class RedisConfig(BaseModel):
    host: str = "localhost"
    port: int = Field(6379, gt=0, lt=65536)
    db: int = Field(0, ge=0)

class AppConfig(BaseModel):
    app_name: str = "MyApp"
    debug: bool = False
    secret_key: str = Field(..., min_length=32)
    database: DatabaseConfig
    redis: Optional[RedisConfig] = None
    allowed_hosts: List[str] = ["localhost"]
    environment_vars: Dict[str, str] = {}

    @validator('secret_key')
    def secret_key_from_env(cls, v):
        # Try to get from environment first
        return os.getenv('SECRET_KEY', v)

    @validator('debug')
    def debug_mode_warning(cls, v):
        if v:
            print("Warning: Debug mode is enabled")
        return v

    class Config:
        env_file = '.env'
        env_nested_delimiter = '__'
```

## How to Run Examples

### Dictionary Example
```bash
# Navigate to corresponding directory
cd lesson-16/01
python3 main.py
```

### namedtuple Example
```bash
cd lesson-16/02
python3 main.py
```

### Traditional Class Example
```bash
cd lesson-16/03
python3 main.py
```

### Dataclass Example
```bash
cd lesson-16/04
python3 main.py
```

### Pydantic Example
```bash
cd lesson-16/05

# Install requirements
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the script
python3 main.py
```

## Validation and Error Handling

### Pydantic Validation Examples
```python
from pydantic import BaseModel, Field, ValidationError
from typing import List

class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., ge=0, le=150)
    email: str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')

# Valid data
try:
    user = User(name="Alice", age=30, email="alice@example.com")
    print(f"Created user: {user}")
except ValidationError as e:
    print(f"Validation error: {e}")

# Invalid data
try:
    invalid_user = User(name="", age=-5, email="invalid-email")
except ValidationError as e:
    print("Validation errors:")
    for error in e.errors():
        print(f"  {error['loc']}: {error['msg']}")
```

### Custom Validation
```python
from pydantic import BaseModel, validator, root_validator

class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    email: str

    @validator('first_name', 'last_name')
    def names_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.title()

    @validator('email')
    def email_must_be_valid(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v.lower()

    @root_validator
    def check_age_email_consistency(cls, values):
        age = values.get('age')
        email = values.get('email')

        if age and age < 13 and email:
            raise ValueError('Users under 13 cannot have email')

        return values
```

## Best Practices

### 1. **Choose the Right Data Model**
```python
# Good: Use appropriate model for the use case
# Simple data transfer
user_data = {"name": "Alice", "age": 30}

# Structured data with validation
from pydantic import BaseModel
class User(BaseModel):
    name: str
    age: int

# Complex business logic
class UserAccount:
    def __init__(self, user: User):
        self.user = user
        self.balance = 0

    def deposit(self, amount: float):
        # Business logic here
        pass
```

### 2. **Use Type Hints Consistently**
```python
# Good: Consistent type hints
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class User:
    name: str
    age: int
    email: Optional[str] = None
    tags: List[str] = field(default_factory=list)

# Avoid: Missing or inconsistent types
@dataclass
class BadUser:
    name  # No type hint
    age: int
    email = None  # Type unclear
```

### 3. **Validate Early and Often**
```python
# Good: Validate at boundaries
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

    @validator('age')
    def age_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Age must be positive')
        return v

def process_user(user_data: dict):
    user = User(**user_data)  # Validation happens here
    # Process validated user
```

### 4. **Use Immutable Data When Possible**
```python
# Good: Immutable data prevents accidental modification
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float

# Good: Use namedtuple for simple immutable data
from collections import namedtuple
Coordinate = namedtuple('Coordinate', ['x', 'y'])
```

### 5. **Handle Serialization Properly**
```python
# Good: Explicit serialization methods
from dataclasses import dataclass, asdict
import json

@dataclass
class User:
    name: str
    age: int

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        return cls(**data)
```

## Performance Considerations

### Memory Usage Comparison
```python
import sys
from collections import namedtuple
from dataclasses import dataclass
from pydantic import BaseModel

# Dictionary
user_dict = {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}

# namedtuple
User = namedtuple('User', ['name', 'age', 'email'])
user_tuple = User('Alice', 30, 'alice@example.com')

# dataclass
@dataclass
class UserData:
    name: str
    age: int
    email: str

user_data = UserData('Alice', 30, 'alice@example.com')

# Pydantic
class UserModel(BaseModel):
    name: str
    age: int
    email: str

user_model = UserModel(name='Alice', age=30, email='alice@example.com')

# Compare memory usage
print(f"Dict size: {sys.getsizeof(user_dict)} bytes")
print(f"namedtuple size: {sys.getsizeof(user_tuple)} bytes")
print(f"dataclass size: {sys.getsizeof(user_data)} bytes")
print(f"Pydantic size: {sys.getsizeof(user_model)} bytes")
```

## Practice Suggestions

1. **User Profile System**: Create a comprehensive user profile with different data models
2. **Configuration Parser**: Build a configuration system using Pydantic
3. **Data Migration Tool**: Convert between different data model formats
4. **API Response Models**: Design API response structures with validation
5. **Settings Management**: Create application settings with environment variable support
6. **Data Processing Pipeline**: Build a pipeline that transforms data through different models

## Common Pitfalls

- **Over-engineering**: Don't use complex models for simple data
- **Missing validation**: Validate data at system boundaries
- **Mutability issues**: Be careful with mutable default arguments
- **Type hint neglect**: Use type hints consistently for better code quality
- **Serialization assumptions**: Don't assume all data models serialize the same way
- **Performance ignorance**: Consider memory and speed implications

## Related Resources

- [dataclasses Documentation](https://docs.python.org/3/library/dataclasses.html)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [namedtuple Documentation](https://docs.python.org/3/library/collections.html#collections.namedtuple)
- [Type Hints Documentation](https://docs.python.org/3/library/typing.html)
- [PEP 557 - Data Classes](https://peps.python.org/pep-0557/)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)