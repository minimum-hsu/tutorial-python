# Lesson 02 - Python Functions and Modules

This lesson covers Python functions, modules, and the concept of the main entry point, including parameter handling, type hints, and lambda functions.

## Learning Objectives

- Understand the `__name__ == '__main__'` pattern
- Learn about Python modules and imports
- Master function definition and parameter handling
- Understand positional and keyword arguments
- Learn about type hints and type checking
- Master argument unpacking techniques
- Understand lambda functions

## Course Content

### 01. Main Entry Point
**Files:** `01/main.py`, `01/no_main.py`

Learn the difference between scripts with and without the main guard:

**`01/main.py`**
```python
#!/usr/bin/env python3

print('this is main.py')

# Top-level script pattern
if __name__ == '__main__':
    print('this is main')
```

**`01/no_main.py`**
```python
#!/usr/bin/env python3

print('this is no_main.py')

print('no main')
```

**Key Concepts:**
- `__name__ == '__main__'` pattern for script entry points
- Difference between running as script vs importing as module
- Reference: [Top-level script environment](https://docs.python.org/3/library/__main__.html)

### 02. Modules and Imports
**Files:** `02/main.py`, `02/second.py`

Learn how modules work and how `__name__` changes during imports:

**`02/main.py`**
```python
#!/usr/bin/env python3

import second

print('this is main.py. module name is', __name__)

if __name__ == '__main__':
    print('this is main')
```

**`02/second.py`**
```python
#!/usr/bin/env python3

print('this is second.py. module name is', __name__)

if __name__ == '__main__':
    print('this is second')
```

**Key Concepts:**
- Module import behavior
- `__name__` variable in different contexts
- How code executes during import vs direct execution

### 03. Basic Functions
**File:** `03/function.py`

Learn basic function definition and calling:

```python
#!/usr/bin/env python3

def hello():
    print('hello world')

if __name__ == '__main__':
    hello()
```

**Key Concepts:**
- Function definition with `def` keyword
- Function calling syntax
- Function scope and execution

### 04. Function Parameters
**Files:** `04/parameter.py`, `04/arbitrary.py`, `04/positional_and_keyword.py`

Learn various parameter handling techniques:

**Basic Parameters (`04/parameter.py`)**
```python
#!/usr/bin/env python3

def hello(name):  # 'name' is a parameter
    print('hello', name)

if __name__ == '__main__':
    hello('Alice')  # 'Alice' is an argument
```

**Arbitrary Arguments (`04/arbitrary.py`)**
```python
#!/usr/bin/env python3

# Arbitrary positional arguments
def print_multiply(*args):
    result = 1
    for num in args:
        result *= num
    print(result)

# Arbitrary keyword arguments
def print_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Combined arbitrary arguments
def combined_example(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
```

**Positional and Keyword Arguments (`04/positional_and_keyword.py`)**
```python
#!/usr/bin/env python3

def hello(greeting, name, title):
    print(greeting, title, name)

# Special parameters: '/' for positional-only, '*' for keyword-only
def hi(greeting, /, name, *, title):
    print(greeting, title, name)
```

**Key Concepts:**
- Parameters vs arguments distinction
- `*args` for arbitrary positional arguments
- `**kwargs` for arbitrary keyword arguments
- Positional-only parameters (`/`)
- Keyword-only parameters (`*`)
- Reference: [Python Glossary - Parameter](https://docs.python.org/3/glossary.html#term-parameter)

### 05. Type Hints and Type Checking
**File:** `05/typecheck.py`

Learn about type hints and runtime type checking:

```python
#!/usr/bin/env python3

def hello(name: str):
    assert isinstance(name, str)
    print('hello', name)

if __name__ == '__main__':
    hello('Alice')

    # Type checker will warn, but Python won't error at runtime
    hello(['Bob'])

    # Suppress type checker warnings
    hello(['Charlie'])  # type: ignore
```

**Key Concepts:**
- Type hints with `:` syntax
- Runtime vs static type checking
- `isinstance()` for runtime type validation
- `# type: ignore` comment for suppressing warnings
- Reference: [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)

### 06. Argument Unpacking
**File:** `06/unpack.py`

Learn how to unpack arguments when calling functions:

```python
#!/usr/bin/env python3

def hello(greeting, name, title):
    print(greeting, title, name)

if __name__ == '__main__':
    # Unpack tuple as positional arguments
    args = ('Hello,', 'Alice', 'Ms.')
    hello(*args)

    # Unpack dictionary as keyword arguments
    kwargs = {'greeting': 'Hi,', 'name': 'Bob', 'title': 'Mr.'}
    hello(**kwargs)
```

**Key Concepts:**
- `*` operator for unpacking positional arguments
- `**` operator for unpacking keyword arguments
- Reference: [Unpacking Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists)

### 07. Lambda Functions
**File:** `07/lambda.py`

Learn about anonymous functions with lambda:

```python
#!/usr/bin/env python3

function_double = lambda x: x * 2

function_multiply = lambda x, y: x * y

if __name__ == '__main__':
    print('function_double(5) =', function_double(5))      # Output: 10
    print('function_multiply(5, 3) =', function_multiply(5, 3))  # Output: 15
```

**Key Concepts:**
- Lambda syntax: `lambda parameters: expression`
- Anonymous functions for simple operations
- Assignment of lambda functions to variables
- Use cases for lambda functions

## How to Run

Each example can be executed directly:

```bash
# Navigate to lesson-02 directory
cd lesson-02

# Test main entry point
cd 01
python3 main.py
python3 no_main.py

# Test modules and imports
cd ../02
python3 main.py
python3 second.py

# Test functions
cd ../03
python3 function.py

# Test parameters
cd ../04
python3 parameter.py
python3 arbitrary.py
python3 positional_and_keyword.py

# Test type checking
cd ../05
python3 typecheck.py

# Test unpacking
cd ../06
python3 unpack.py

# Test lambda functions
cd ../07
python3 lambda.py
```

## Practice Suggestions

1. **Module Experiments**: Try importing the modules in different ways and observe the `__name__` variable
2. **Parameter Variations**: Create functions with different parameter combinations
3. **Type Hints**: Add type hints to your functions and use a type checker like mypy
4. **Unpacking Practice**: Practice unpacking different data structures as function arguments
5. **Lambda Usage**: Convert simple functions to lambda expressions and vice versa

## Related Resources

- [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Modules Documentation](https://docs.python.org/3/tutorial/modules.html)
- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [Python Glossary - Parameter vs Argument](https://docs.python.org/3/glossary.html#term-parameter)
- [Special Parameters Documentation](https://docs.python.org/3/tutorial/controlflow.html#special-parameters)