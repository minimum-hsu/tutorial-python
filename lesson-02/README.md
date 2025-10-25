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
- Learn to document functions with docstrings
- Master inner functions and closures
- Understand functional programming concepts

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
**Files:** `05/typehint.py`, `05/typecheck.py`, `05/assert.py`

Learn about type hints and runtime type checking:

**Basic Type Hints (`05/typehint.py`)**
```python
#!/usr/bin/env python3

def multiply(a: int, b: int) -> int:
    return a * b

if __name__ == '__main__':
    result = multiply(3, 4)
    print('3 multiplied by 4 is', result)
```

**Type Checking with Ignoring Warnings (`05/typecheck.py`)**
```python
#!/usr/bin/env python3

def hello(name: str):
    print('hello', name)

if __name__ == '__main__':
    hello('Alice')

    # Type checker will warn, but Python won't error at runtime
    hello(['Bob'])

    # Suppress type checker warnings
    hello(['Charlie'])  # type: ignore
```

**Runtime Assertion Checking (`05/assert.py`)**
```python
#!/usr/bin/env python3

def hello(name: str):
    assert isinstance(name, str)
    print('hello', name)

if __name__ == '__main__':
    hello('Alice')

    # This will raise an AssertionError when the type is incorrect
    hello(['Bob'])
```

**Key Concepts:**
- Type hints with `:` syntax for parameters
- Return type annotations with `->` syntax
- Runtime vs static type checking
- `isinstance()` for runtime type validation
- `assert` statement for runtime type enforcement
- `# type: ignore` comment for suppressing type checker warnings
- AssertionError when type validation fails
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

### 08. Documentation Strings (Docstrings)
**File:** `08/docstring.py`

Learn about documenting functions with docstrings:

```python
#!/usr/bin/env python3

def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers.

    Args:
        a (int): Multiplicand integer.
        b (int): Multiplier integer.

    Returns:
        int: The product of a and b.
    """
    return a * b

if __name__ == '__main__':
    result = multiply(3, 4)
    print(multiply.__doc__)  # Access the docstring
```

**Key Concepts:**
- Triple-quoted strings for multi-line documentation
- Google-style docstring format
- `Args:` section for parameter documentation
- `Returns:` section for return value documentation
- `__doc__` attribute to access docstrings
- Self-documenting code practices
- Integration with documentation generators (Sphinx, etc.)

### 09. Inner Functions (Nested Functions)
**File:** `09/inner.py`

Learn about defining functions inside other functions:

```python
#!/usr/bin/env python3

def format_text(text: str) -> str:
    """
    Format the input text by trimming whitespace and converting to lowercase.

    Args:
        text (str): The input text to format.

    Returns:
        str: The formatted text.
    """

    def trim(s: str) -> str:
        """
        The inner function to trim whitespace from both ends of the string.
        """
        return s.strip()

    def to_lower(s: str) -> str:
        """
        The inner function to convert the string to lowercase.
        """
        return s.lower()

    return to_lower(trim(text))

if __name__ == '__main__':
    sample = "   Hello World!   "
    formatted = format_text(sample)
    print(f"Original: '{sample}'")
    print(f"Formatted: '{formatted}'")
```

**Key Concepts:**
- Inner functions are defined inside other functions
- Inner functions have access to outer function's variables (closure)
- Inner functions are only accessible within the outer function
- Useful for code organization and encapsulation
- Can be used to create specialized helper functions
- Support for functional programming patterns

### 10. Functional Programming with pandas
**Files:** `10/funtional_programming.py`, `10/requirements.txt`

Learn functional programming concepts using pandas DataFrame operations:

**Requirements (`10/requirements.txt`)**
```pip-requirements
pandas
```

**Functional Programming Example (`10/funtional_programming.py`)**
```python
#!/usr/bin/env python3

from pandas import DataFrame

def create_example() -> DataFrame:
    """
    Create a simple pandas DataFrame as an example.

    Returns:
        DataFrame: A pandas DataFrame with sample data.
    """
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    return DataFrame(data)

def filter_age(df, min_age) -> DataFrame:
    '''
    Filter rows where Age is greater than min_age.

    Args:
        df (DataFrame): The input DataFrame.
        min_age (int): The minimum age to filter by.

    Returns:
        DataFrame: Filtered DataFrame.
    '''
    return df[df['Age'] > min_age]

def uppercase_city(df) -> DataFrame:
    '''
    Convert the 'City' column to uppercase.

    Args:
        df (DataFrame): The input DataFrame.

    Returns:
        DataFrame: DataFrame with 'City' column in uppercase.
    '''
    _df = df.copy()
    _df['City'] = _df['City'].apply(lambda city: city.upper())
    return _df

def add_age_flag(df) -> DataFrame:
    '''
    Add a new column 'Age > 30' indicating if Age is greater than 30.

    Args:
        df (DataFrame): The input DataFrame.

    Returns:
        DataFrame: DataFrame with new 'Age > 30' column.
    '''
    _df = df.copy()
    _df['Age > 30'] = _df['Age'].apply(lambda age: age > 30)
    return _df

if __name__ == '__main__':
    df = create_example()

    # Using pipe to chain functions
    result = df.pipe(filter_age, min_age=30) \
               .pipe(uppercase_city) \
               .pipe(add_age_flag)
    print(result)
```

**Key Concepts:**
- Functional programming principles with data processing
- Pure functions that don't modify input data
- Function chaining with `.pipe()` method
- `lambda` functions for simple transformations
- `DataFrame.apply()` for element-wise operations
- `DataFrame.copy()` for avoiding side effects
- Method chaining for readable data pipelines
- External dependencies management with `requirements.txt`

## How to Run

Each example can be executed directly:

```bash
# Navigate to corresponding directory
cd lesson-02/01
python3 main.py
python3 no_main.py
```

```bash
cd lesson-02/02
python3 main.py
python3 second.py
```

```bash
cd lesson-02/03
python3 function.py
```

```bash
cd lesson-02/04
python3 parameter.py
python3 arbitrary.py
python3 positional_and_keyword.py
```

```bash
cd lesson-02/05
python3 typehint.py
python3 typecheck.py
# assert.py will raise an AssertionError at runtime
python3 assert.py
```

```bash
cd lesson-02/06
python3 unpack.py
```

```bash
cd lesson-02/07
python3 lambda.py
```

```bash
cd lesson-02/08
python3 docstring.py
```

```bash
cd lesson-02/09
python3 inner.py
```

```bash
cd lesson-02/10
# Install dependencies first
pip install -r requirements.txt
python3 funtional_programming.py
```

## Practice Suggestions

1. **Module Experiments**: Try importing the modules in different ways and observe the `__name__` variable
2. **Parameter Variations**: Create functions with different parameter combinations
3. **Type Hints**: Add type hints to your functions and use a type checker like mypy
4. **Unpacking Practice**: Practice unpacking different data structures as function arguments
5. **Lambda Usage**: Convert simple functions to lambda expressions and vice versa
6. **Documentation Practice**: Write comprehensive docstrings for all your functions following Google or NumPy style
7. **Inner Functions**: Create functions with multiple inner functions for complex data processing
8. **Functional Programming**: Practice chaining operations and creating pure functions with data processing libraries

## Related Resources

- [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Modules Documentation](https://docs.python.org/3/tutorial/modules.html)
- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [Python Glossary - Parameter vs Argument](https://docs.python.org/3/glossary.html#term-parameter)
- [Special Parameters Documentation](https://docs.python.org/3/tutorial/controlflow.html#special-parameters)