# Lesson 06 - Python Exception Handling

This lesson covers Python exception handling, including throwing exceptions, catching them with try-except blocks, custom exceptions, and modern exception groups.

## Learning Objectives

- Understand how exceptions are thrown in Python
- Learn to create custom exceptions
- Master try-except-else-finally blocks
- Learn exception suppression techniques
- Understand exception groups (Python 3.11+)
- Develop robust error handling strategies

## Course Content

### 01. Throwing Exceptions
**Files:** `01/throw_exception.py`, `01/throw_custom_exception.py`, `01/throw_derived_exception.py`

Learn different ways to throw exceptions in Python:

**Natural Exception (`01/throw_exception.py`)**
```python
#!/usr/bin/env python3

def throw_exception():
    names = ['Alice', 'Bob', 'Charlie']

    for i in range(4):  # Will access index 3, which doesn't exist
        print(names[i])

if __name__ == '__main__':
    throw_exception()
    # This will raise:
    # IndexError: list index out of range
```

**Custom Exception Message (`01/throw_custom_exception.py`)**
```python
#!/usr/bin/env python3

def throw_exception():
    raise Exception('Custom exception')

if __name__ == '__main__':
    throw_exception()
    # This will raise:
    # Exception: Custom exception
```

**Custom Exception Class (`01/throw_derived_exception.py`)**
```python
#!/usr/bin/env python3

class CustomException(Exception):
    pass

def throw_exception():
    raise CustomException('Custom exception')

if __name__ == '__main__':
    throw_exception()
    # This will raise:
    # CustomException: Custom exception
```

**Key Concepts:**
- Natural exceptions occur from invalid operations
- `raise` statement for manual exception throwing
- Custom exception classes inherit from `Exception`
- Exception messages provide context for debugging

### 02. Exception Handling
**Files:** `02/without_exception.py`, `02/try_except.py`, `02/suppress.py`

Learn comprehensive exception handling techniques:

**No Exception Case (`02/without_exception.py`)**
```python
#!/usr/bin/env python3

import sys

def throw_exception():
    names = ['Alice', 'Bob', 'Charlie']

    for i in range(3):  # Safe range - no exception
        print(names[i])

if __name__ == '__main__':
    try:
        throw_exception()
    except IndexError as err:
        # Not executed in this case
        print('[Error]', err, file=sys.stderr)
    else:
        print('no exception launched')  # This will execute
    finally:
        print('finally block is always executed')
```

**Exception Handling (`02/try_except.py`)**
```python
#!/usr/bin/env python3

import sys

def throw_exception():
    names = ['Alice', 'Bob', 'Charlie']

    for i in range(4):  # Will cause IndexError
        print(names[i])

if __name__ == '__main__':
    try:
        throw_exception()
    except IndexError as err:
        print('[Error]', err, file=sys.stderr)  # This will execute
    else:
        # Not executed in this case
        print('no exception launched')
    finally:
        print('finally block is always executed')
```

**Exception Suppression (`02/suppress.py`)**
```python
#!/usr/bin/env python3

from contextlib import suppress

def throw_exception():
    names = ['Alice', 'Bob', 'Charlie']

    for i in range(4):  # Will cause IndexError
        print(names[i])

if __name__ == '__main__':
    # Suppress IndexError exceptions
    with suppress(IndexError):
        throw_exception()  # Exception is silently ignored
```

**Key Concepts:**
- `try-except` blocks for exception catching
- `except ClassName as variable` syntax for accessing exception object
- `else` block executes only when no exception occurs
- `finally` block always executes (cleanup code)
- `contextlib.suppress()` for silently ignoring specific exceptions
- `sys.stderr` for error output

### 03. Exception Groups (Python 3.11+)
**File:** `03/exception_group.py`

Learn about handling multiple exceptions simultaneously:

```python
#!/usr/bin/env python3

def throw_exception():
    exceptions = []
    names = ['Alice', 'Bob', 'Charlie']

    for i in range(6):  # Will try to access indices 3, 4, 5
        try:
            print(names[i])
        except IndexError as e:
            exceptions.append(e)  # Collect exceptions

    if exceptions:
        raise ExceptionGroup("Multiple exceptions occurred", exceptions)

if __name__ == '__main__':
    try:
        throw_exception()
    except ExceptionGroup as eg:
        for i, exc in enumerate(eg.exceptions, 1):
            print(f'[Error {i}]', exc)
```

**Key Concepts:**
- `ExceptionGroup` for grouping multiple exceptions
- Collecting exceptions instead of immediate failure
- Iterating through grouped exceptions
- Batch error processing
- Available in Python 3.11+

## Exception Handling Patterns

### Basic Exception Handling
```python
try:
    # Code that might raise an exception
    risky_operation()
except SpecificException as e:
    # Handle specific exception
    handle_specific_error(e)
except Exception as e:
    # Handle any other exception
    handle_general_error(e)
else:
    # Code that runs if no exception occurred
    success_operations()
finally:
    # Cleanup code that always runs
    cleanup_resources()
```

### Multiple Exception Types
```python
try:
    risky_operation()
except (ValueError, TypeError) as e:
    # Handle multiple exception types the same way
    handle_value_or_type_error(e)
except IndexError as e:
    # Handle IndexError differently
    handle_index_error(e)
```

### Exception Chaining
```python
try:
    operation()
except OriginalException as e:
    # Re-raise with additional context
    raise NewException("Additional context") from e
```

## How to Run

Each example can be executed directly:

```bash
# Navigate to corresponding directory
cd lesson-06/01
python3 throw_exception.py
python3 throw_custom_exception.py
python3 throw_derived_exception.py
```

```bash
cd lesson-06/02
python3 without_exception.py
python3 try_except.py
python3 suppress.py
```

```bash
cd lesson-06/03
python3 exception_group.py
```

**Note:** The exception group example requires Python 3.11 or later.

## Best Practices

### 1. **Specific Exception Handling**
```python
# Good: Catch specific exceptions
try:
    value = int(user_input)
except ValueError:
    print("Invalid number format")

# Avoid: Catching all exceptions
try:
    value = int(user_input)
except:  # Too broad
    print("Something went wrong")
```

### 2. **Proper Exception Messages**
```python
# Good: Descriptive messages
raise ValueError(f"Invalid age: {age}. Age must be between 0 and 150")

# Avoid: Generic messages
raise ValueError("Invalid input")
```

### 3. **Resource Cleanup**
```python
# Good: Use finally for cleanup
file = None
try:
    file = open('data.txt')
    process_file(file)
except IOError:
    print("File error occurred")
finally:
    if file:
        file.close()

# Better: Use context managers
try:
    with open('data.txt') as file:
        process_file(file)
except IOError:
    print("File error occurred")
```

### 4. **Custom Exception Hierarchy**
```python
class ApplicationError(Exception):
    """Base exception for application"""
    pass

class ValidationError(ApplicationError):
    """Raised when validation fails"""
    pass

class NetworkError(ApplicationError):
    """Raised when network operations fail"""
    pass
```

## Practice Suggestions

1. **Exception Scenarios**:
   - Create functions that handle file operations with proper exception handling
   - Build input validation with custom exceptions
   - Practice with network operations and timeout handling

2. **Custom Exception Design**:
   - Design exception hierarchies for specific domains
   - Add custom attributes to exception classes
   - Practice exception chaining and context preservation

3. **Error Recovery**:
   - Implement retry mechanisms with exception handling
   - Create fallback strategies when operations fail
   - Practice graceful degradation patterns

4. **Exception Groups**:
   - Experiment with collecting and processing multiple errors
   - Handle partial failures in batch operations
   - Practice with concurrent error scenarios

## Common Exception Types

- **`ValueError`**: Invalid value for operation
- **`TypeError`**: Wrong data type
- **`IndexError`**: List/sequence index out of range
- **`KeyError`**: Dictionary key not found
- **`FileNotFoundError`**: File or directory not found
- **`IOError`**: Input/output operation failed
- **`AttributeError`**: Object has no attribute
- **`ImportError`**: Module import failed

## Related Resources

- [Python Exception Handling Documentation](https://docs.python.org/3/tutorial/errors.html)
- [Built-in Exceptions Documentation](https://docs.python.org/3/library/exceptions.html)
- [Exception Groups (Python 3.11+)](https://docs.python.org/3/library/exceptions.html#exception-groups)
- [Context Managers Documentation](https://docs.python.org/3/library/contextlib.html)
- [PEP 654 - Exception Groups](https://www.python.org/dev/peps/pep-0654/)