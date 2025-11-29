# Lesson 17 - Database Operations  <!-- omit in toc -->

This lesson covers comprehensive database operations in Python, from basic SQLite usage to modern ORM frameworks and NoSQL databases, demonstrating various approaches to data persistence.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. SQLite Database Operations](#01-sqlite-database-operations)
  - [02. SQLAlchemy ORM with SQLite](#02-sqlalchemy-orm-with-sqlite)
  - [03. SQLAlchemy with MySQL and Docker](#03-sqlalchemy-with-mysql-and-docker)
  - [04. DynamoDB with PynamoDB](#04-dynamodb-with-pynamodb)
  - [05. InfluxDB Time Series Operations](#05-influxdb-time-series-operations)
- [Database Technology Comparison](#database-technology-comparison)
  - [Feature Comparison](#feature-comparison)
  - [When to Use Each](#when-to-use-each)
    - [Use SQLite when:](#use-sqlite-when)
    - [Use SQLAlchemy + SQLite when:](#use-sqlalchemy--sqlite-when)
    - [Use SQLAlchemy + MySQL when:](#use-sqlalchemy--mysql-when)
    - [Use PynamoDB + DynamoDB when:](#use-pynamodb--dynamodb-when)
    - [Use InfluxDB when:](#use-influxdb-when)
- [Advanced Database Patterns](#advanced-database-patterns)
  - [Connection Pool Management](#connection-pool-management)
  - [Database Migrations](#database-migrations)
  - [Advanced SQLAlchemy Queries](#advanced-sqlalchemy-queries)
  - [DynamoDB Advanced Operations](#dynamodb-advanced-operations)
- [How to Run Examples](#how-to-run-examples)
  - [SQLite Example](#sqlite-example)
  - [SQLAlchemy + SQLite Example](#sqlalchemy--sqlite-example)
  - [SQLAlchemy + MySQL Example](#sqlalchemy--mysql-example)
  - [DynamoDB Example](#dynamodb-example)
  - [InfluxDB Example](#influxdb-example)
- [Database Best Practices](#database-best-practices)
  - [1. **Connection Management**](#1-connection-management)
  - [2. **Error Handling**](#2-error-handling)
  - [3. **Query Optimization**](#3-query-optimization)
  - [4. **Configuration Management**](#4-configuration-management)
  - [5. **Schema Design**](#5-schema-design)
- [Performance Optimization](#performance-optimization)
  - [Database Indexing](#database-indexing)
  - [Query Batching](#query-batching)
  - [Connection Pooling](#connection-pooling)
- [Common Pitfalls](#common-pitfalls)
- [Practice Suggestions](#practice-suggestions)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Master SQLite database operations with Python
- Learn SQLAlchemy ORM for relational databases
- Understand database relationships and migrations
- Work with MySQL and other relational databases
- Explore NoSQL databases with DynamoDB
- Compare different database approaches and use cases
- Handle database connections and error management
- Design scalable database architectures

## Course Content

### 01. SQLite Database Operations
**File:** `01/main.py`

Learn basic database operations using Python's built-in SQLite support:

```python
#!/usr/bin/env python3

from pathlib import Path
import sqlite3

if __name__ == '__main__':
    workdir = Path(__file__).parent
    # Create a new database connection
    con = sqlite3.connect(workdir / 'tutorial.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE user(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
    cur.execute('INSERT INTO user (name, age) VALUES (?, ?)', ('Alice', 30))
    cur.execute('INSERT INTO user (name, age) VALUES (?, ?)', ('Bob', 25))
    cur.execute('INSERT INTO user (name, age) VALUES (?, ?)', ('Charlie', 35))
    con.commit()  # Save (commit) the changes

    # Query the database
    cur.execute('SELECT name, age FROM user WHERE age >= 30')
    rows = cur.fetchall()
    for row in rows:
        print('Name: {}, Age: {}'.format(row[0], row[1]))

    # Close the connection
    con.close()

    # Clean up the database file after execution
    (workdir / 'tutorial.db').unlink()
```

**Key Concepts:**
- `sqlite3.connect()` for database connections
- Raw SQL execution with parameterized queries
- `commit()` for transaction management
- `fetchall()` for result retrieval
- File-based database storage
- No external dependencies required

### 02. SQLAlchemy ORM with SQLite
**Files:** `02/main.py`, `02/model.py`, `02/requirements.txt`

Learn modern database operations using SQLAlchemy ORM:

**Requirements (`02/requirements.txt`)**
```pip-requirements
SQLAlchemy
```

**Data Models (`02/model.py`)**
```python
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] = mapped_column()

    addresses: Mapped[list["Address"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, age={self.age!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
```

**Application Code (`02/main.py`)**
```python
#!/usr/bin/env python3

from model import User, Address, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Create an SQLite database in memory
    engine = create_engine('sqlite+pysqlite:///:memory:', echo=False)

    # Create all tables defined in the model
    Base.metadata.create_all(engine)

    # Create a new session
    with Session(engine) as session:
        # Create new User and Address instances
        alice = User(
            name='alice',
            age=30,
            addresses=[Address(email_address='alice@example.com')]
        )
        bob = User(
            name='bob',
            age=25,
            addresses=[Address(email_address='bob@example.com')]
        )
        charlie = User(
            name='charlie',
            age=35,
            addresses=[Address(email_address='charlie@example.com')]
        )

        # Add the instances to the session and commit
        session.add_all([alice, bob, charlie])
        session.commit()

    # Query users aged 30 or older
    with Session(engine) as session:
        stmt = session.query(User).filter(User.age >= 30)
        for user in stmt:
            print(user)
            for address in user.addresses:
                print("  ", address)
```

**Key Concepts:**
- `DeclarativeBase` for model definition
- `Mapped` type annotations for modern SQLAlchemy
- One-to-many relationships with `relationship()`
- Session management with context managers
- Object-relational mapping (ORM) abstraction
- Type-safe database operations

### 03. SQLAlchemy with MySQL and Docker
**Files:** `03/main.py`, `03/model.py`, `03/docker-compose.yml`, `03/requirements.txt`

Learn to work with MySQL database using Docker for development:

**Docker Configuration (`03/docker-compose.yml`)**
```yaml
version: '3.8'

services:
  mysql:
    image: mysql:8.0
    container_name: mysql-server
    environment:
      MYSQL_ROOT_PASSWORD: password123
      MYSQL_DATABASE: demo
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

**Requirements (`03/requirements.txt`)**
```pip-requirements
SQLAlchemy
pymysql
cryptography
```

**Application Code (`03/main.py`)**
```python
#!/usr/bin/env python3

from model import User, Address, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# MySQL Database Settings
USERNAME = 'root'
PASSWORD = 'password123'
HOST = 'localhost'
PORT = 3306
DATABASE = 'demo'

if __name__ == '__main__':
    # Create a MySQL database connection
    engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}', echo=False)

    # Create all tables defined in the model
    Base.metadata.create_all(engine)

    # Create a new session
    with Session(engine) as session:
        # Create new User and Address instances
        alice = User(
            name='alice',
            age=30,
            addresses=[Address(email_address='alice@example.com')]
        )
        bob = User(
            name='bob',
            age=25,
            addresses=[Address(email_address='bob@example.com')]
        )
        charlie = User(
            name='charlie',
            age=35,
            addresses=[Address(email_address='charlie@example.com')]
        )

        # Add the instances to the session and commit
        session.add_all([alice, bob, charlie])
        session.commit()

    # Query users aged 30 or older
    with Session(engine) as session:
        stmt = session.query(User).filter(User.age >= 30)
        for user in stmt:
            print(user)
            for address in user.addresses:
                print('  ', address)
```

**Key Concepts:**
- MySQL connection strings with PyMySQL driver
- Docker Compose for development databases
- Environment-specific database configuration
- Same ORM code works across different databases
- Production-ready database setup

### 04. DynamoDB with PynamoDB
**Files:** `04/main.py`, `04/model.py`, `04/requirements.txt`

Learn NoSQL database operations with Amazon DynamoDB:

**Requirements (`04/requirements.txt`)**
```pip-requirements
pynamodb
```

**Data Model (`04/model.py`)**
```python
from pynamodb.attributes import NumberAttribute
from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model

class User(Model):
    """
    A DynamoDB User
    """

    class Meta:
        table_name = 'user'
        region = 'us-west-1'

    email = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()
    age = NumberAttribute()
```

**Application Code (`04/main.py`)**
```python
#!/usr/bin/env python3

from model import User
from pynamodb.exceptions import DoesNotExist, PutError, TableError

if __name__ == '__main__':
    try:
        # Create the table if it doesn't exist
        if not User.exists():
            print("Creating User table...")
            User.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
            print("Table created successfully!")

        # Create a new user
        user = User(
            email='alice@example.com',
            name='Alice',
            age=30
        )
        user.save()
        print(f"User {user.name} saved successfully!")

        # Query the user back
        try:
            retrieved_user = User.get('alice@example.com')
            print(f"Retrieved user: {retrieved_user.name}, age: {retrieved_user.age}")
        except DoesNotExist:
            print("User not found")

    except TableError as e:
        print(f"Table error: {e}")
    except PutError as e:
        print(f"Put error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

**Key Concepts:**
- NoSQL document-based data model
- Hash key for primary key identification
- AWS DynamoDB integration
- Exception handling for DynamoDB operations
- Automatic table creation and management
- Scalable cloud database solution

### 05. InfluxDB Time Series Operations
**Files:** `05/query.py`, `05/write.py`, `05/requirements.txt`, `05/.env`, `05/docker-compose.yml`

This section demonstrates how to use InfluxDB, a popular time series database, with Python. You will learn how to write and query time series data, set up InfluxDB using Docker, and manage credentials securely.

**Key Concepts:**
- Time series data modeling and storage
- Using the official InfluxDB Python client
- Writing and querying data points
- Environment variable management for credentials
- Running InfluxDB locally with Docker Compose

**How to Run:**
```bash
cd lesson-17/05

# Start InfluxDB with Docker
docker-compose up -d

# Install requirements
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Set environment variables (or edit .env)
export INFLUXDB_URL=http://localhost:8086
export INFLUXDB_TOKEN=your_token
export INFLUXDB_ORG=your_org
export INFLUXDB_BUCKET=your_bucket

# Write data
python3 write.py

# Query data
python3 query.py

# Stop InfluxDB container
docker-compose down
```

**Typical Usage:**
- Use `write.py` to insert time series data into InfluxDB.
- Use `query.py` to retrieve and analyze time series data.
- Store sensitive credentials in `.env` and load them in your scripts for security.

**Best Practices:**
- Always use environment variables or `.env` files for credentials.
- Use Docker Compose for easy local database setup and teardown.
- Batch writes for performance when inserting large volumes of data.

**References:**
- [InfluxDB Python Client Documentation](https://github.com/influxdata/influxdb-client-python)
- [InfluxDB Official Documentation](https://docs.influxdata.com/influxdb/)

## Database Technology Comparison

### Feature Comparison

| Feature | SQLite | SQLAlchemy + SQLite | SQLAlchemy + MySQL | PynamoDB + DynamoDB | InfluxDB |
|---------|--------|-------------------|-------------------|-------------------|----------|
| **Setup Complexity** | None | Low | Medium | Medium | Medium |
| **Scalability** | Low | Low | High | Very High | High |
| **ACID Compliance** | Yes | Yes | Yes | Limited | Yes |
| **Schema Flexibility** | Rigid | Rigid | Rigid | Flexible | Flexible |
| **Query Complexity** | High | High | High | Limited | Medium |
| **Cost** | Free | Free | Low | Pay-per-use | Free |
| **Cloud Native** | No | No | Depends | Yes | Yes |
| **Learning Curve** | Low | Medium | Medium | Medium | Medium |

### When to Use Each

#### Use SQLite when:
- Prototyping and development
- Small applications with minimal concurrency
- Local data storage needs
- No external database server required

#### Use SQLAlchemy + SQLite when:
- Need ORM benefits with simple deployment
- Type safety and modern Python features
- Complex relationships between entities
- Migration support required

#### Use SQLAlchemy + MySQL when:
- Production applications with high concurrency
- Complex queries and transactions
- Need ACID compliance
- Traditional relational data model

#### Use PynamoDB + DynamoDB when:
- Cloud-native applications
- Need massive scalability
- Flexible schema requirements
- AWS ecosystem integration

#### Use InfluxDB when:
- Working with time series data
- Need high write and query performance
- Require downsampling and retention policies
- Cloud-native monitoring and analytics

## Advanced Database Patterns

### Connection Pool Management
```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

# Configure connection pooling
engine = create_engine(
    'mysql+pymysql://user:password@localhost/db',
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=0,
    pool_recycle=3600,
    pool_pre_ping=True
)
```

### Database Migrations
```python
from alembic import command
from alembic.config import Config

# Initialize migrations
def init_migrations():
    alembic_cfg = Config("alembic.ini")
    command.init(alembic_cfg, "migrations")

# Create migration
def create_migration(message):
    alembic_cfg = Config("alembic.ini")
    command.revision(alembic_cfg, autogenerate=True, message=message)

# Apply migrations
def upgrade_database():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
```

### Advanced SQLAlchemy Queries
```python
from sqlalchemy import and_, or_, func
from sqlalchemy.orm import joinedload

def advanced_queries(session):
    # Complex filtering
    users = session.query(User).filter(
        and_(User.age >= 18, User.age <= 65)
    ).all()

    # Aggregation
    avg_age = session.query(func.avg(User.age)).scalar()

    # Eager loading relationships
    users_with_addresses = session.query(User).options(
        joinedload(User.addresses)
    ).all()

    # Subqueries
    subq = session.query(Address.user_id).filter(
        Address.email_address.like('%@gmail.com')
    ).subquery()

    gmail_users = session.query(User).filter(
        User.id.in_(subq)
    ).all()

    return users, avg_age, users_with_addresses, gmail_users
```

### DynamoDB Advanced Operations
```python
from pynamodb.attributes import ListAttribute, MapAttribute
from pynamodb.models import Model

class UserProfile(Model):
    class Meta:
        table_name = 'user_profile'
        region = 'us-west-1'

    user_id = UnicodeAttribute(hash_key=True)
    profile_data = MapAttribute()
    tags = ListAttribute()

    @classmethod
    def get_users_by_tag(cls, tag):
        # Scan operation (expensive, use carefully)
        for user in cls.scan():
            if tag in user.tags:
                yield user

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)
            self.save()
```

## How to Run Examples

### SQLite Example
```bash
# Navigate to corresponding directory
cd lesson-17/01
python3 main.py
```

### SQLAlchemy + SQLite Example
```bash
cd lesson-1702

# Install requirements
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run the script
python3 main.py
```

### SQLAlchemy + MySQL Example
```bash
cd lesson-17/03

# Start MySQL with Docker
docker-compose up -d

# Install requirements
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run the script
python3 main.py

# Stop MySQL container
docker-compose down
```

### DynamoDB Example
```bash
cd lesson-17/04

# Install requirements
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Configure AWS credentials (required)
aws configure
# or set environment variables:
# export AWS_ACCESS_KEY_ID=your_key
# export AWS_SECRET_ACCESS_KEY=your_secret

# Run the script
python3 main.py
```

### InfluxDB Example
```bash
cd lesson-17/05

# Start InfluxDB with Docker
docker-compose up -d

# Install requirements
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Set environment variables (or edit .env)
export INFLUXDB_URL=http://localhost:8086
export INFLUXDB_TOKEN=your_token
export INFLUXDB_ORG=your_org
export INFLUXDB_BUCKET=your_bucket

# Write data
python3 write.py

# Query data
python3 query.py

# Stop InfluxDB container
docker-compose down
```

## Database Best Practices

### 1. **Connection Management**
```python
# Good: Use context managers
from sqlalchemy.orm import Session

with Session(engine) as session:
    # Database operations
    user = User(name="Alice")
    session.add(user)
    session.commit()
# Session automatically closed

# Avoid: Manual connection management
session = Session(engine)
user = User(name="Alice")
session.add(user)
session.commit()
# session.close()  # Easy to forget!
```

### 2. **Error Handling**
```python
# Good: Comprehensive error handling
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

try:
    with Session(engine) as session:
        user = User(name="Alice", email="alice@example.com")
        session.add(user)
        session.commit()
except IntegrityError as e:
    print(f"Data integrity error: {e}")
    session.rollback()
except SQLAlchemyError as e:
    print(f"Database error: {e}")
    session.rollback()
```

### 3. **Query Optimization**
```python
# Good: Use eager loading for relationships
users = session.query(User).options(
    joinedload(User.addresses)
).all()

# Avoid: N+1 query problem
users = session.query(User).all()
for user in users:
    print(user.addresses)  # Separate query for each user
```

### 4. **Configuration Management**
```python
# Good: Environment-based configuration
import os

DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'sqlite:///default.db'
)

engine = create_engine(DATABASE_URL)

# Avoid: Hardcoded credentials
engine = create_engine('mysql://root:password@localhost/db')
```

### 5. **Schema Design**
```python
# Good: Proper constraints and indexes
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.now())

    __table_args__ = (
        Index('idx_user_email', 'email'),
        Index('idx_user_created_at', 'created_at'),
    )
```

## Performance Optimization

### Database Indexing
```python
# Add indexes for frequently queried columns
from sqlalchemy import Index

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    age: Mapped[int] = mapped_column()
    created_at: Mapped[datetime] = mapped_column()

    __table_args__ = (
        Index('idx_user_email', 'email'),
        Index('idx_user_age', 'age'),
        Index('idx_user_created_at', 'created_at'),
    )
```

### Query Batching
```python
# Batch inserts for better performance
def batch_insert_users(session, users_data):
    users = [User(**data) for data in users_data]
    session.add_all(users)
    session.commit()

# Bulk operations
def bulk_update_ages(session, age_increment):
    session.query(User).update(
        {User.age: User.age + age_increment}
    )
    session.commit()
```

### Connection Pooling
```python
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

# Configure appropriate pool for your use case
engine = create_engine(
    database_url,
    pool_size=20,          # Number of connections to maintain
    max_overflow=10,       # Additional connections allowed
    pool_recycle=3600,     # Recreate connections after 1 hour
    pool_pre_ping=True,    # Validate connections before use
)
```

## Common Pitfalls

- **Not closing connections**: Always use context managers or explicit close()
- **N+1 query problems**: Use eager loading for relationships
- **Missing error handling**: Database operations can fail in many ways
- **Hardcoded credentials**: Use environment variables for sensitive data
- **Ignoring transactions**: Use transactions for data consistency
- **Poor schema design**: Plan your database schema carefully
- **No connection pooling**: Configure appropriate connection pools

## Practice Suggestions

1. **User Management System**: Build a complete CRUD application
2. **Blog Platform**: Create a blogging system with posts, comments, and users
3. **E-commerce Database**: Design product catalog with categories and orders
4. **Social Media Backend**: Build user profiles, posts, and relationships
5. **Analytics Dashboard**: Create time-series data storage and querying
6. **Multi-tenant Application**: Design schema for multiple organizations

## Related Resources

- [SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [PynamoDB Documentation](https://pynamodb.readthedocs.io/)
- [Amazon DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/)
- [Database Design Principles](https://en.wikipedia.org/wiki/Database_design)
- [Alembic Migrations](https://alembic.sqlalchemy.org/)
- [InfluxDB Documentation](https://docs.influxdata.com/influxdb/)