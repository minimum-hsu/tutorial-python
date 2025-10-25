# Lesson 12 - Unit Testing in Python

This lesson covers comprehensive unit testing in Python using both unittest (built-in) and pytest (third-party) frameworks, from basic test cases to advanced testing patterns.

## Learning Objectives

- Master Python's built-in unittest framework
- Learn pytest framework and its advantages
- Understand test-driven development (TDD) principles
- Write effective test cases and assertions
- Use fixtures for test setup and teardown
- Handle exceptions in tests
- Organize test project structure
- Configure test environments and runners

## Course Content

### 01. Basic unittest Framework
**Files:** `01/timestamp.py`, `01/test.py`

Learn the fundamentals of unittest with a practical timestamp parsing example:

**Source Code (`01/timestamp.py`)**
```python
from datetime import datetime

def parse_timestamp(t):
    # Try multiple timestamp formats
    formats = [
        '%Y-%m-%dT%H:%M:%SZ',           # ISO 8601 with Z
        '%Y-%m-%dT%H:%M:%S.%fZ',        # ISO 8601 with microseconds and Z
        '%Y-%m-%dT%H:%M:%S%z',          # ISO 8601 with timezone
        '%Y-%m-%dT%H:%M:%S.%f%z',       # ISO 8601 with microseconds and timezone
        '%Y-%m-%dT%H:%M:%S',            # ISO 8601 basic
        '%Y-%m-%dT%H:%M:%S.%f',         # ISO 8601 with microseconds
        '%Y-%m-%d %H:%M:%SZ',           # Space separated with Z
        '%Y-%m-%d %H:%M:%S.%fZ',        # Space separated with microseconds and Z
        '%Y-%m-%d %H:%M:%S%z',          # Space separated with timezone
        '%Y-%m-%d %H:%M:%S.%f%z',       # Space separated with microseconds and timezone
        '%Y-%m-%d %H:%M:%S',            # Space separated basic
        '%Y-%m-%d %H:%M:%S.%f',         # Space separated with microseconds
        '%a %b %d %H:%M:%S %Z %Y'       # RFC 2822 format
    ]

    for fmt in formats:
        try:
            return datetime.strptime(t, fmt).utctimetuple()
        except ValueError:
            continue

    return None
```

**Test Cases (`01/test.py`)**
```python
#!/usr/bin/env python3

import unittest
from timestamp import parse_timestamp as parse

class TimestampTestCase(unittest.TestCase):

    def test_iso8601(self):
        self.assertIsNotNone(parse('2018-04-13T09:39:21'))
        self.assertIsNotNone(parse('2018-04-13T09:39:21.578'))
        self.assertIsNotNone(parse('2018-04-13T09:39:21+0800'))

    def test_slash(self):
        self.assertIsNotNone(parse('2018-04-13 09:39:21'))

    def test_special(self):
        self.assertIsNotNone(parse('Fri Apr 13 09:39:21 UTC 2018'))

if __name__ == '__main__':
    unittest.main()
```

**Key Concepts:**
- `unittest.TestCase` base class for test cases
- `assertIsNotNone()` for null checks
- Test method naming convention (`test_*`)
- `unittest.main()` for test runner
- Multiple format handling with try-except

### 02. Advanced unittest with Setup/Teardown
**Files:** `02/xml_parser_et.py`, `02/test.py`, `02/example.xml`

Learn advanced unittest features with file operations and logging:

**XML Parser (`02/xml_parser_et.py`)**
```python
#!/usr/bin/env python3

from pathlib import Path
import xml.etree.ElementTree as ET

def parse_xml(file_: str):
    tree = ET.parse(file_)
    root = tree.getroot()

    news = [(item.find('title').text, item.find('link').text)
            for item in root.iter('item')]
    return news
```

**Advanced Test Case (`02/test.py`)**
```python
#!/usr/bin/env python3

import logging
import os
from pathlib import Path
import unittest
from urllib import request
from xml_parser_et import parse_xml as parse

class NewsTestCase(unittest.TestCase):
    workdir = Path(__file__).parent
    report = workdir / 'report.log'
    xml = workdir / 'example.xml'

    def setUp(self):
        logging.basicConfig(
            format='%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%dT%H:%M:%S%z',
            level=logging.INFO,
            filename=self.report
        )

        self.url = 'https://status.aws.amazon.com/rss/billingconsole.rss'

        # Download news XML for testing
        with request.urlopen(self.url) as rss:
            data = rss.read().decode('utf-8')

        with open(self.xml, 'w') as f:
            f.write(data)

    def tearDown(self):
        logging.info('[success] %s', self.url)

    def doCleanups(self):
        # Optional: Remove test files
        # os.remove(self.xml)
        pass

    def test_parse(self):
        self.assertIsInstance(parse(self.xml), list)

if __name__ == '__main__':
    unittest.main()
```

**Key Concepts:**
- `setUp()` method for test preparation
- `tearDown()` method for cleanup
- `doCleanups()` for additional cleanup
- File operations in tests
- Network requests in test setup
- Logging integration in tests

### 03. Basic pytest Framework
**Files:** `03/src/main.py`, `03/tests/test_main.py`, `03/pyproject.toml`

Learn pytest basics with a simple multiplication function:

**Source Code (`03/src/main.py`)**
```python
#!/usr/bin/env python3

def multiply(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Both arguments must be integers')

    return a * b

if __name__ == '__main__':
    result = multiply(6, 7)
    print(f'The result of multiplication is: {result}')
```

**Test Cases (`03/tests/test_main.py`)**
```python
import pytest
from main import multiply

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0

def test_multiply_with_string():
    with pytest.raises(TypeError, match='Both arguments must be integers'):
        multiply(2, '3')
```

**Configuration (`03/pyproject.toml`)**
```toml
[tool.pytest.ini_options]
log_cli = false
log_cli_level = "INFO"
minversion = "8.4"
pythonpath = ["src"]
testpaths = ["tests"]
```

**Key Concepts:**
- Simple `assert` statements instead of `self.assert*`
- `pytest.raises()` for exception testing
- `match` parameter for exception message validation
- `pyproject.toml` configuration
- Separate `src/` and `tests/` directories

### 04. Advanced pytest with Fixtures
**Files:** `04/src/main.py`, `04/tests/test_main.py`, `04/pyproject.toml`

Learn pytest fixtures and advanced testing patterns:

**Source Code (`04/src/main.py`)**
```python
#!/usr/bin/env python3

class Operation:
    def calculate(self, a: int | float, b: int | float) -> int | float:
        raise NotImplementedError("Subclasses must implement this method")

class Multiplication(Operation):
    def calculate(self, a: int | float, b: int | float) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a * b

class Division(Operation):
    def calculate(self, a: int | float, b: int | float) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        if b == 0:
            raise ValueError("The divisor cannot be zero")
        return a / b
```

**Test Cases with Fixtures (`04/tests/test_main.py`)**
```python
import pytest
from main import Division, Multiplication

@pytest.fixture(scope='function')
def multiplication():
    return Multiplication()

@pytest.fixture(scope='function')
def division():
    return Division()

def test_multiplication(multiplication):
    assert multiplication.calculate(3, 4) == 12
    assert multiplication.calculate(-2, 5) == -10
    assert multiplication.calculate(0, 100) == 0
    assert multiplication.calculate(2.5, 4) == 10.0

def test_division(division):
    assert division.calculate(8, 2) == 4
    assert division.calculate(-9, 3) == -3
    assert division.calculate(7.5, 2.5) == 3.0
```

**Key Concepts:**
- `@pytest.fixture` decorator for test setup
- Fixture scopes: `function`, `class`, `module`, `session`
- Dependency injection through test parameters
- Object-oriented testing patterns
- Type hints with union types (`int | float`)

## Testing Framework Comparison

### unittest vs pytest

| Feature | unittest | pytest |
|---------|----------|--------|
| **Setup** | Built-in | Third-party |
| **Syntax** | `self.assertEqual(a, b)` | `assert a == b` |
| **Test Discovery** | `test*.py` or `*test.py` | Automatic |
| **Fixtures** | `setUp()/tearDown()` | `@pytest.fixture` |
| **Parameterization** | Manual loops | `@pytest.mark.parametrize` |
| **Plugins** | Limited | Extensive ecosystem |
| **Configuration** | Code-based | Configuration files |
| **Output** | Basic | Rich, colorful |

### Common Assertion Methods

#### unittest Assertions
```python
self.assertEqual(a, b)          # a == b
self.assertNotEqual(a, b)       # a != b
self.assertTrue(x)              # bool(x) is True
self.assertFalse(x)             # bool(x) is False
self.assertIs(a, b)             # a is b
self.assertIsNot(a, b)          # a is not b
self.assertIsNone(x)            # x is None
self.assertIsNotNone(x)         # x is not None
self.assertIn(a, b)             # a in b
self.assertNotIn(a, b)          # a not in b
self.assertIsInstance(a, b)     # isinstance(a, b)
self.assertRaises(exc, fun, *args, **kwargs)
```

#### pytest Assertions
```python
assert a == b
assert a != b
assert x
assert not x
assert a is b
assert a is not b
assert x is None
assert x is not None
assert a in b
assert a not in b
assert isinstance(a, b)
with pytest.raises(Exception):
    function_that_raises()
```

## Project Structure Best Practices

### Standard Layout
```
project/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

### Test File Naming
- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_*`
- Test classes: `Test*`
- Test methods: `test_*`

## Advanced Testing Patterns

### Parameterized Tests (pytest)
```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (-1, 5, -5),
    (0, 100, 0),
    (2.5, 4, 10.0),
])
def test_multiply_parametrized(a, b, expected):
    assert multiply(a, b) == expected
```

### Fixture Scopes and Dependencies
```python
@pytest.fixture(scope="session")
def database():
    db = create_test_database()
    yield db
    db.cleanup()

@pytest.fixture(scope="function")
def user(database):
    user = database.create_user("test_user")
    yield user
    database.delete_user(user.id)

def test_user_operations(user):
    assert user.name == "test_user"
```

### Mock Objects
```python
from unittest.mock import Mock, patch

def test_with_mock():
    mock_service = Mock()
    mock_service.get_data.return_value = {"key": "value"}

    result = process_data(mock_service)

    mock_service.get_data.assert_called_once()
    assert result == {"key": "value"}

@patch('requests.get')
def test_api_call(mock_get):
    mock_get.return_value.json.return_value = {"status": "ok"}

    result = call_api()

    assert result["status"] == "ok"
```

### Test Coverage
```python
# Install coverage
pip install coverage pytest-cov

# Run with coverage
pytest --cov=src --cov-report=html

# Generate coverage report
coverage run -m pytest
coverage report
coverage html
```

## How to Run Tests

### Running unittest
```bash
# Navigate to corresponding directory
cd lesson-12/01
python3 -m unittest test.py

# Run with verbose output
python3 -m unittest -v test.py

# Run specific test method
python3 -m unittest test.TimestampTestCase.test_iso8601
```

```bash
cd lesson-12/02
python3 -m unittest test.py
```

### Running pytest
```bash
# Navigate to corresponding directory
cd lesson-12/03

# Install pytest
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest

# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_main.py::test_multiply
```

```bash
# Navigate to corresponding directory
cd lesson-12/04

# Install pytest
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Best Practices

### 1. **Test Organization**
```python
# Good: Organize tests by functionality
class TestUserAuthentication:
    def test_valid_login(self):
        pass

    def test_invalid_password(self):
        pass

    def test_user_not_found(self):
        pass

# Good: Use descriptive test names
def test_should_return_error_when_password_is_empty():
    pass
```

### 2. **Test Independence**
```python
# Good: Each test is independent
def test_add_user():
    user = create_user("test")
    assert user.name == "test"
    cleanup_user(user)

# Avoid: Tests depending on each other
class BadTestCase(unittest.TestCase):
    def test_01_create_user(self):
        self.user = create_user("test")

    def test_02_update_user(self):  # Depends on test_01
        self.user.name = "updated"
```

### 3. **Use Appropriate Assertions**
```python
# Good: Specific assertions
assert len(users) == 3
assert user.name == "expected"
assert "error" in response

# Avoid: Generic assertions
assert len(users)  # What if it's 0?
assert user.name   # What if it's None?
```

### 4. **Test Edge Cases**
```python
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_empty_input():
    assert process_empty_list([]) == []

def test_large_numbers():
    result = multiply(999999999, 999999999)
    assert isinstance(result, int)
```

### 5. **Use Fixtures Effectively**
```python
# Good: Reusable fixtures
@pytest.fixture
def sample_data():
    return {
        "users": [{"id": 1, "name": "Alice"}],
        "products": [{"id": 1, "name": "Widget"}]
    }

def test_user_processing(sample_data):
    users = process_users(sample_data["users"])
    assert len(users) == 1
```

## Configuration Examples

### pytest.ini
```ini
[tool:pytest]
minversion = 8.4
addopts = -ra -q --strict-markers
testpaths = tests
python_files = test_*.py *_test.py
python_classes = Test*
python_functions = test_*
```

### pyproject.toml (pytest)
```toml
[tool.pytest.ini_options]
minversion = "8.4"
addopts = [
    "-ra",
    "--strict-markers",
    "--strict-config",
    "--cov=src",
    "--cov-report=term-missing",
]
testpaths = ["tests"]
pythonpath = ["src"]
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
]
```

## Common Testing Patterns

### Database Testing
```python
@pytest.fixture(scope="function")
def db_session():
    connection = create_connection()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()
```

### API Testing
```python
import requests
from unittest.mock import patch

@patch('requests.get')
def test_api_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"status": "success"}

    response = api_client.get_status()

    assert response["status"] == "success"
    mock_get.assert_called_once_with("https://api.example.com/status")
```

### File System Testing
```python
import tempfile
import os

def test_file_processing():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = os.path.join(temp_dir, "test.txt")
        with open(test_file, "w") as f:
            f.write("test content")

        result = process_file(test_file)

        assert result == "processed: test content"
```

## Practice Suggestions

1. **TDD Practice**: Write tests before implementing functions
2. **Legacy Code Testing**: Add tests to existing untested code
3. **Integration Testing**: Test multiple components together
4. **Performance Testing**: Measure and test execution time
5. **Error Handling**: Comprehensive exception testing
6. **Data Validation**: Test input validation and sanitization

## Common Pitfalls

- **Testing Implementation Instead of Behavior**: Focus on what, not how
- **Overly Complex Tests**: Keep tests simple and focused
- **Insufficient Edge Case Testing**: Test boundary conditions
- **Test Data Dependencies**: Avoid hard-coded test data
- **Ignoring Test Maintenance**: Keep tests updated with code changes
- **Poor Test Coverage**: Aim for meaningful coverage, not just high percentages

## Related Resources

- [unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [pytest Documentation](https://docs.pytest.org/)
- [Testing Best Practices](https://docs.python-guide.org/writing/tests/)
- [Test-Driven Development](https://en.wikipedia.org/wiki/Test-driven_development)
- [Mock Objects](https://docs.python.org/3/library/unittest.mock.html)
- [Coverage.py](https://coverage.readthedocs.io/)