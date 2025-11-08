# Lesson 19 - Python Decorators <!-- omit in toc -->

This lesson covers Python decorators comprehensively, from basic concepts to advanced practical applications. Decorators are a powerful Python feature that allows you to modify or extend the behavior of functions, methods, or classes without permanently modifying their code.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. Timer Decorators - Performance Measurement](#01-timer-decorators---performance-measurement)
    - [Basic Timer Decorator (`01/timer.py`)](#basic-timer-decorator-01timerpy)
    - [Using timeit Module (`01/timeit_timer.py`)](#using-timeit-module-01timeit_timerpy)
    - [Context Manager Approach (`01/context.py`)](#context-manager-approach-01contextpy)
  - [02. Property Decorators - Getter and Setter Methods](#02-property-decorators---getter-and-setter-methods)
  - [03. Caching Decorators - Performance Optimization](#03-caching-decorators---performance-optimization)
  - [04. Flask Route Decorators - Web Development](#04-flask-route-decorators---web-development)
  - [05. AWS Lambda Powertools - Cloud Logging Decorators](#05-aws-lambda-powertools---cloud-logging-decorators)
    - [Lambda Function (`05/src/main.py`)](#lambda-function-05srcmainpy)
    - [Test Suite (`05/tests/test_lambda.py`)](#test-suite-05teststest_lambdapy)
- [How to Run Examples](#how-to-run-examples)
  - [Timer Decorators](#timer-decorators)
  - [Property Decorators](#property-decorators)
  - [Caching Decorators](#caching-decorators)
  - [Flask Route Decorators](#flask-route-decorators)
  - [AWS Lambda Powertools](#aws-lambda-powertools)
- [Advanced Decorator Patterns](#advanced-decorator-patterns)
  - [Decorator with Arguments](#decorator-with-arguments)
  - [Class-Based Decorators](#class-based-decorators)
  - [Preserving Function Metadata](#preserving-function-metadata)
  - [Multiple Decorators](#multiple-decorators)
- [Best Practices](#best-practices)
  - [1. **Use `functools.wraps`**](#1-use-functoolswraps)
  - [2. **Handle Arguments Gracefully**](#2-handle-arguments-gracefully)
  - [3. **Create Reusable Decorators**](#3-create-reusable-decorators)
  - [4. **Error Handling in Decorators**](#4-error-handling-in-decorators)
- [Common Use Cases](#common-use-cases)
  - [Authentication Decorator](#authentication-decorator)
  - [Retry Decorator](#retry-decorator)
  - [Rate Limiting Decorator](#rate-limiting-decorator)
- [Practice Suggestions](#practice-suggestions)
- [Common Pitfalls](#common-pitfalls)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Understand what decorators are and how they work
- Learn to create custom decorators for timing and performance measurement
- Master the `@property` decorator for getter/setter methods
- Explore built-in decorators like `@lru_cache` for optimization
- Apply decorators in real-world scenarios (Flask routes, AWS Lambda logging)
- Understand decorator patterns and best practices
- Create reusable and maintainable decorator solutions

## Course Content

### 01. Timer Decorators - Performance Measurement
**Files:** `01/timer.py`, `01/timeit_timer.py`, `01/context.py`

Learn different approaches to measure execution time using decorators and context managers:

#### Basic Timer Decorator (`01/timer.py`)
```python
#!/usr/bin/env python3

# A simple decorator to measure execution time

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds to execute.")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

if __name__ == "__main__":
    slow_function()
```

#### Using timeit Module (`01/timeit_timer.py`)
```python
#!/usr/bin/env python3

# Using timeit module to measure execution time

import timeit

def slow_function():
    import time
    time.sleep(2)

if __name__ == "__main__":
    timer = timeit.Timer(stmt="slow_function()", setup="from __main__ import slow_function")
    execution_time = timer.timeit(number=1)
    print(f"slow_function took {execution_time:.4f} seconds to execute.")
```

#### Context Manager Approach (`01/context.py`)
```python
#!/usr/bin/env python3

# Using context manager to measure execution time

import time
from contextlib import contextmanager

@contextmanager
def timer(name="block"):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"{name} took {end - start:.4f} seconds to execute.")

def slow_function():
    time.sleep(2)

if __name__ == "__main__":
    with timer(slow_function.__name__):
        slow_function()
```

**Key Concepts:**
- Decorator function wrapper pattern
- `*args` and `**kwargs` for flexible function signatures
- Performance measurement techniques
- Context managers vs decorators
- `timeit` module for precise timing
- Function metadata preservation

### 02. Property Decorators - Getter and Setter Methods
**File:** `02/property.py`

Master the `@property` decorator for creating getter and setter methods:

```python
#!/usr/bin/env python3

class Animal():
    def __init__(self, kind: str, name: str, legs: int):
        '''The first step when creating a new object'''
        self.__kind = kind
        self._name = name

    def hello(self):
        print('My name is {}. I am {}.'.format(self._name, self.__kind))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

if __name__ == '__main__':
    dog = Animal('dog', 'Buddy', 4)
    dog.hello()
    print('Current name:', dog.name)
    dog.name = 'Max'
    print('New name:', dog.name)
    dog.hello()
```

**Key Concepts:**
- `@property` decorator for getter methods
- `@<property_name>.setter` for setter methods
- Encapsulation and data validation
- Private vs protected attributes (`__` vs `_`)
- Pythonic getter/setter patterns
- Property vs direct attribute access

### 03. Caching Decorators - Performance Optimization
**File:** `03/cache.py`

Learn to use `@lru_cache` for function result caching and performance optimization:

```python
#!/usr/bin/env python3

from functools import lru_cache

@lru_cache(maxsize=32)
def fibonacci(n: int) -> int:
    print(f"Calculating fibonacci({n})")

    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print("Calculating Fibonacci numbers with caching:")
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

    print(fibonacci.cache_info())

    print("\nRecalculating Fibonacci numbers to demonstrate caching:")
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci(i)}")
```

**Key Concepts:**
- `@lru_cache` decorator for memoization
- LRU (Least Recently Used) cache strategy
- `maxsize` parameter configuration
- `cache_info()` method for cache statistics
- Performance improvement for recursive functions
- Memory vs speed trade-offs

### 04. Flask Route Decorators - Web Development
**Files:** `04/api.py`, `04/requirements.txt`, `04/README.md`

Apply decorators in Flask web framework for route handling:

```python
#!/usr/bin/env python3

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(message="Hello Flask!")

if __name__ == "__main__":
    app.run(debug=True)
```

**Key Concepts:**
- `@app.route()` decorator for URL routing
- HTTP methods specification
- Flask application structure
- RESTful API design patterns
- JSON response handling
- Web framework decorator patterns

### 05. AWS Lambda Powertools - Cloud Logging Decorators
**Files:** `05/src/main.py`, `05/tests/test_lambda.py`, `05/pyproject.toml`, `05/requirements.txt`, `05/README.md`

Learn advanced decorator usage in cloud environments with AWS Lambda Powertools:

#### Lambda Function (`05/src/main.py`)
```python
#############################
# Logging
#############################
from aws_lambda_powertools import Logger
logger = Logger()

#############################
# Main
#############################
@logger.inject_lambda_context(log_event=True)
def lambda_handler(event, context):
    logger.info("This is an info log")
    logger.debug("This is a debug log")
    logger.warning("This is a warning log")
    logger.error("This is an error log")
```

#### Test Suite (`05/tests/test_lambda.py`)
```python
from dataclasses import dataclass
import pytest
from main import lambda_handler

@pytest.fixture(scope="function")
def lambda_context():
    """Dummy Lambda Context object."""
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = "arn:aws:lambda:ap-northeast-1:000000000000:function:test"
        aws_request_id: str = "00000000-0000-0000-0000-000000000000"
    return LambdaContext()

def test_lambda_handler(lambda_context):
    lambda_handler({}, lambda_context)
```

**Key Concepts:**
- Advanced decorator parameters
- Dependency injection patterns
- Cloud-native logging strategies
- Structured logging with decorators
- Testing decorated functions
- AWS Lambda integration patterns

## How to Run Examples

### Timer Decorators
```bash
# Navigate to corresponding directory
cd lesson-19/01
python3 timer.py

# Run timeit version
python3 timeit_timer.py

# Run context manager version
python3 context.py
```

### Property Decorators
```bash
# Navigate to section 02
cd lesson-19/02
python3 property.py
```

### Caching Decorators
```bash
# Navigate to section 03
cd lesson-19/03
python3 cache.py
```

### Flask Route Decorators
```bash
# Navigate to section 04
cd lesson-19/04

# Install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run Flask application
export FLASK_APP=api.py
flask run

# Test the endpoint
curl http://localhost:5000/hello
```

### AWS Lambda Powertools
```bash
# Navigate to section 05
cd lesson-19/05

# Install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run tests
pytest -s
```

## Advanced Decorator Patterns

### Decorator with Arguments
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Prints "Hello, Alice!" three times
```

### Class-Based Decorators
```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # Call 1 of say_hello
say_hello()  # Call 2 of say_hello
```

### Preserving Function Metadata
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example_function():
    """This is an example function."""
    pass

print(example_function.__name__)  # example_function
print(example_function.__doc__)   # This is an example function.
```

### Multiple Decorators
```python
def bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper

@bold
@italic
def say_hello():
    return "Hello, World!"

print(say_hello())  # <b><i>Hello, World!</i></b>
```

## Best Practices

### 1. **Use `functools.wraps`**
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        # Decorator logic here
        return func(*args, **kwargs)
    return wrapper
```

### 2. **Handle Arguments Gracefully**
```python
def flexible_decorator(func=None, *, argument=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # Use argument if provided
            return f(*args, **kwargs)
        return wrapper

    if func is None:
        return decorator
    else:
        return decorator(func)

# Can be used with or without arguments
@flexible_decorator
def func1():
    pass

@flexible_decorator(argument="value")
def func2():
    pass
```

### 3. **Create Reusable Decorators**
```python
def validate_types(**expected_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Type validation logic
            bound_args = signature(func).bind(*args, **kwargs)
            for name, value in bound_args.arguments.items():
                if name in expected_types:
                    expected_type = expected_types[name]
                    if not isinstance(value, expected_type):
                        raise TypeError(f"Expected {name} to be {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(name=str, age=int)
def create_person(name, age):
    return f"Person: {name}, Age: {age}"
```

### 4. **Error Handling in Decorators**
```python
def safe_execute(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            return None
    return wrapper

@safe_execute
def risky_function():
    raise ValueError("Something went wrong")
```

## Common Use Cases

### Authentication Decorator
```python
def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_authenticated():
            raise PermissionError("Authentication required")
        return func(*args, **kwargs)
    return wrapper

@require_auth
def sensitive_operation():
    return "Sensitive data"
```

### Retry Decorator
```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def unreliable_api_call():
    # Simulate API call that might fail
    import random
    if random.random() < 0.7:
        raise ConnectionError("API temporarily unavailable")
    return "Success"
```

### Rate Limiting Decorator
```python
import time
from collections import defaultdict

def rate_limit(calls_per_second=1):
    call_times = defaultdict(list)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            func_name = func.__name__

            # Clean old calls
            call_times[func_name] = [t for t in call_times[func_name] if now - t < 1]

            if len(call_times[func_name]) >= calls_per_second:
                raise Exception("Rate limit exceeded")

            call_times[func_name].append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(calls_per_second=2)
def api_call():
    return "API response"
```

## Practice Suggestions

1. **Custom Timer Decorator**: Create a decorator that logs execution time to a file
2. **Validation Decorator**: Build a decorator that validates function arguments
3. **Caching Decorator**: Implement your own caching decorator with TTL (Time To Live)
4. **Logging Decorator**: Create a decorator that logs function calls with parameters
5. **Authentication Decorator**: Build a decorator for user authentication in web apps
6. **Retry Decorator**: Implement a decorator that retries failed operations
7. **Performance Monitor**: Create a decorator that tracks function performance metrics
8. **API Rate Limiter**: Build a decorator for API rate limiting

## Common Pitfalls

- **Forgetting `@wraps`**: Always use `@wraps` to preserve function metadata
- **Argument handling**: Ensure decorators properly handle `*args` and `**kwargs`
- **Stacking order**: Understand how multiple decorators are applied (bottom to top)
- **Performance overhead**: Be aware that decorators add function call overhead
- **Debugging complexity**: Decorated functions can be harder to debug
- **Memory leaks**: Avoid capturing unnecessary references in decorator closures

## Related Resources

- [Python Decorator Documentation](https://docs.python.org/3/glossary.html#term-decorator)
- [functools Module](https://docs.python.org/3/library/functools.html)
- [contextlib Module](https://docs.python.org/3/library/contextlib.html)
- [Real Python Decorators Guide](https://realpython.com/primer-on-python-decorators/)
- [Flask Decorators](https://flask.palletsprojects.com/en/2.3.x/patterns/decorators/)
- [AWS Lambda Powertools](https://docs.powertools.aws.dev/lambda/python/latest/)
- [PEP 318 - Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)