# Lesson 99 - Python Advanced Techniques and Idioms <!-- omit in toc -->

This lesson covers advanced Python techniques, idioms, and lesser-known features that make your code more elegant, readable, and Pythonic. These are essential patterns and practices that experienced Python developers use regularly.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. Pass Statement - Placeholder for Code](#01-pass-statement---placeholder-for-code)
  - [02. Walrus Operator - Assignment Expressions](#02-walrus-operator---assignment-expressions)
  - [03. Comprehensions - Elegant Data Processing](#03-comprehensions---elegant-data-processing)
  - [04. Del Statement - Advanced Object Deletion](#04-del-statement---advanced-object-deletion)
  - [05. Python Naming Conventions and Special Features](#05-python-naming-conventions-and-special-features)
    - [Internal Attributes and Properties](#internal-attributes-and-properties)
    - [Name Conflict Resolution](#name-conflict-resolution)
    - [Name Mangling for Privacy](#name-mangling-for-privacy)
    - [Numeric Literals with Underscores](#numeric-literals-with-underscores)
    - [Special Methods and Attributes](#special-methods-and-attributes)
    - [Underscore Usage Patterns](#underscore-usage-patterns)
  - [06. Unpacking Patterns - Advanced Argument Handling](#06-unpacking-patterns---advanced-argument-handling)
    - [Function Argument Unpacking](#function-argument-unpacking)
    - [Return Value Unpacking](#return-value-unpacking)
  - [07. Advanced Control Flow - For-Else and Try-Else-Finally](#07-advanced-control-flow---for-else-and-try-else-finally)
    - [For-Else Pattern](#for-else-pattern)
    - [Try-Except-Else-Finally Pattern](#try-except-else-finally-pattern)
  - [08. Data Structure Merging - Lists and Dictionaries](#08-data-structure-merging---lists-and-dictionaries)
    - [Dictionary Merging Techniques](#dictionary-merging-techniques)
    - [List Merging Techniques](#list-merging-techniques)
  - [09. Ellipsis - The ... Operator](#09-ellipsis---the--operator)
    - [Basic Ellipsis Object (`09/ellipsis.py`)](#basic-ellipsis-object-09ellipsispy)
    - [Ellipsis as Placeholder (`09/placeholder.py`)](#ellipsis-as-placeholder-09placeholderpy)
    - [Ellipsis in Function Arguments (`09/argument.py`)](#ellipsis-in-function-arguments-09argumentpy)
    - [Ellipsis in Type Hints (`09/arbitrary.py`)](#ellipsis-in-type-hints-09arbitrarypy)
- [How to Run Examples](#how-to-run-examples)
  - [Basic Pattern Examples](#basic-pattern-examples)
  - [Naming Conventions and Special Features](#naming-conventions-and-special-features)
  - [Unpacking Patterns](#unpacking-patterns)
  - [Advanced Control Flow](#advanced-control-flow)
  - [Data Structure Merging](#data-structure-merging)
  - [Ellipsis Operator](#ellipsis-operator)
- [Practice Suggestions](#practice-suggestions)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Master Python's advanced syntax and idioms
- Understand walrus operator and assignment expressions
- Learn comprehensive techniques and list comprehensions
- Master unpacking and packing patterns
- Understand Python's naming conventions and special methods
- Learn advanced control flow patterns (for-else, try-except-else-finally)
- Master dictionary and list merging techniques
- Explore the ellipsis (`...`) operator and its applications
- Understand Python's special variables and REPL features
- Write more Pythonic and elegant code
- Apply advanced patterns in real-world scenarios

## Course Content

### 01. Pass Statement - Placeholder for Code
**File:** `01/pass.py`

Learn the `pass` statement for creating syntactically correct placeholders:

```python
#!/usr/bin/env python3

# Refer to https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement

def foo():
    pass

class MyException(Exception):
    pass

if __name__ == '__main__':
    foo()
    raise MyException("This is a custom exception.")
```

**Key Concepts:**
- `pass` as a null operation placeholder
- Used in function stubs during development
- Essential for empty class definitions
- Maintains syntactic correctness while coding
- Common in exception class definitions

### 02. Walrus Operator - Assignment Expressions
**File:** `02/assignment.py`

Master the walrus operator (`:=`) for assignment expressions:

```python
#!/usr/bin/env python3

# Refer to https://docs.python.org/3/reference/expressions.html#assignment-expressions

def get_first_element(array: list) -> str:
    '''Return the first element of the list.'''
    if not array:
        return 'The list is empty.'
    return array[0]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    if first := get_first_element(sample_list):
        print(f'The first element is: {first}')
```

**Key Concepts:**
- `:=` walrus operator for assignment within expressions
- Reduces code duplication and improves readability
- Useful in conditions, list comprehensions, and while loops
- Assigns value and returns it in single expression
- Available in Python 3.8+

### 03. Comprehensions - Elegant Data Processing
**File:** `03/comprehension.py`

Learn all types of Python comprehensions for concise data processing:

```python
#!/usr/bin/env python3

list_comprehension = [x * 2 for x in range(10)]
dict_comprehension = {x: x * 2 for x in range(10)}
set_comprehension = {x * 2 for x in range(10)}
generator_comprehension = (x * 2 for x in range(10))

print("List Comprehension:", list_comprehension)
print("Dict Comprehension:", dict_comprehension)
print("Set Comprehension:", set_comprehension)
print("Generator Comprehension:", generator_comprehension, list(generator_comprehension))
```

**Key Concepts:**
- List comprehension `[expr for item in iterable]`
- Dictionary comprehension `{key: value for item in iterable}`
- Set comprehension `{expr for item in iterable}`
- Generator expression `(expr for item in iterable)`
- Memory-efficient alternatives to loops
- Support for conditions and nested iterations

### 04. Del Statement - Advanced Object Deletion
**File:** `04/del.py`

Understand the `del` statement for precise object and attribute deletion:

```python
#!/usr/bin/env python3

def remove_element(array: list[str], element: str) -> list[str]:
    '''Remove all occurrences of element from array.'''
    # Using list comprehension to create a new list without the specified element
    return [item for item in array if item != element]

def del_element(array: list[str], element: str) -> list[str]:
    '''Remove all occurrences of element from array using del statement.'''
    # Find all indices of the element to be removed
    indices_to_remove = [i for i, item in enumerate(array) if item == element]

    # Remove elements in reverse order to avoid index shifting
    for index in reversed(indices_to_remove):
        print("Removing element at index:", index)
        del array[index]
    return array

if __name__ == '__main__':
    sample_array = ['apple', 'banana', 'orange', 'banana', 'grape']
    element_to_remove = 'banana'

    print("Original array:", sample_array)

    new_array = remove_element(sample_array.copy(), element_to_remove)
    print("Array after remove_element:", new_array)

    modified_array = del_element(sample_array.copy(), element_to_remove)
    print("Array after del_element:", modified_array)
```

**Key Concepts:**
- `del` statement for removing variables, attributes, and list items
- Index-based deletion from lists and dictionaries
- Memory cleanup and reference removal
- Difference between `del` and reassignment
- Handling index shifting during multiple deletions

### 05. Python Naming Conventions and Special Features
**Files:** `05/internal.py`, `05/name_conflict.py`, `05/name_mangling.py`, `05/numeric_literals.py`, `05/special.py`, `05/underscore.py`, `05/REPL.md`

#### Internal Attributes and Properties
```python
#!/usr/bin/env python3

class MyClass:
    def __init__(self):
        self._internal_value = 42  # Internal attribute

    @property
    def value(self):
        '''Public property to access the internal value.'''
        return self._internal_value

if __name__ == '__main__':
    obj = MyClass()
    print("Accessing internal value via property:", obj.value)
```

#### Name Conflict Resolution
```python
#!/usr/bin/env python3

# Using reserved keywords as variable names by appending an underscore
id_ = 123
class_ = "MyClass"

print("id(id_):", id(id_))
print("id_:", id_)
print("class: reserved keyword")
print("class_:", class_)
```

#### Name Mangling for Privacy
```python
#!/usr/bin/env python3

class Parent:
    def __init__(self):
        self.__private_attr = "I am private"

    def show(self):
        print("Private Attribute:", self.__private_attr)

class Child(Parent):
    def __init__(self):
        super().__init__()

    def print(self):
        try:
            print("Accessing Parent's private attribute:", self.__private_attr)
        except AttributeError as e:
            print("Error:", e)
```

#### Numeric Literals with Underscores
```python
#!/usr/bin/env python3

large_number = 1_000_000_000
hex_number = 0xFF_FF_FF
binary_number = 0b1010_1010

print("Large Number:", large_number)
print("Hex Number:", hex_number)
print("Binary Number:", binary_number)
```

#### Special Methods and Attributes
```python
#!/usr/bin/env python3

def foo():
    '''function docstring'''
    pass

class Bar:
    '''sequence-like class'''

    def __init__(self):
        self.value = [0, 1, 2]

    def __getitem__(self, index):
        return self.value[index]

    def __len__(self):
        return len(self.value)

if __name__ == '__main__':
    print("Function foo docstring:", foo.__doc__)
    print("Function foo name:", foo.__name__)

    bar = Bar()
    print("Bar length:", len(bar))
    print("Bar items:", [bar[i] for i in bar])
```

#### Underscore Usage Patterns
```python
#!/usr/bin/env python3

# Using underscore as a throwaway variable in a loop
for _ in range(3):
    print("_", end="")

# Using underscore to ignore specific values during unpacking
one, _, three = [1, 2, 3]
print("\nFirst:", one)
print("Third:", three)
```

**Key Concepts:**
- Single underscore `_` for internal use indication
- Double underscore `__` for name mangling
- Trailing underscore `_` to avoid keyword conflicts
- Numeric literal separators for readability
- Special methods `__init__`, `__len__`, `__getitem__`
- Special attributes `__doc__`, `__name__`
- REPL special variable `_` for last result

### 06. Unpacking Patterns - Advanced Argument Handling
**Files:** `06/unpack_args.py`, `06/unpack_return.py`

#### Function Argument Unpacking
```python
#!/usr/bin/env python3

def hello(greeting, name, title):
    print(greeting, title, name)

if __name__ == '__main__':
    # Unpacking argument lists
    args = ('Hello,', 'Alice', 'Ms.')
    hello(*args)

    kwargs = {'greeting': 'Hi,', 'name': 'Bob', 'title': 'Mr.'}
    hello(**kwargs)
```

#### Return Value Unpacking
```python
#!/usr/bin/env python3

def get_array() -> list[str]:
    '''Return a sample array of strings.'''
    return ['apple', 'banana', 'orange', 'banana', 'grape']

if __name__ == '__main__':
    first, *middle, last = get_array()
    print("First element:", first)
    print("Middle elements:", middle)
    print("Last element:", last)

    first, second, *rest = get_array()
    print("First element:", first)
    print("Second element:", second)
    print("Rest of the elements:", rest)

    *_, last = get_array()
    print("Last element only:", last)
```

**Key Concepts:**
- `*args` for unpacking positional arguments
- `**kwargs` for unpacking keyword arguments
- `*variable` for collecting multiple values
- Advanced unpacking patterns with `*` and `_`
- Flexible function parameter handling
- Elegant multiple assignment techniques

### 07. Advanced Control Flow - For-Else and Try-Else-Finally
**Files:** `07/for_else.py`, `07/try_except_else_finally.py`

#### For-Else Pattern
```python
#!/usr/bin/env python3

if __name__ == '__main__':
    # Find out the prime numbers in a given range
    for num in range(2, 100):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(f"{num} is prime")
            # The else block executes only if the loop wasn't broken out of
```

#### Try-Except-Else-Finally Pattern
```python
#!/usr/bin/env python3

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('Error: Division by zero!')
    else:
        print('Division successful, result is:', result)
    finally:
        print('Execution of divide() is complete.')

def open_file(filename: str):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print('Error: File not found!')
    else:
        content = f.read()
        print('File content:', content)
    finally:
        print('Closing file...')
        try:
            f.close()
        except NameError:
            # File was never opened
            pass
```

**Key Concepts:**
- `for-else` executes else block only if loop completes without `break`
- `try-except-else-finally` for comprehensive error handling
- `else` block runs only when no exceptions occur
- `finally` block always executes for cleanup
- Elegant search and validation patterns
- Proper resource management techniques

### 08. Data Structure Merging - Lists and Dictionaries
**Files:** `08/merge_dict.py`, `08/merge_list.py`

#### Dictionary Merging Techniques
```python
#!/usr/bin/env python3

map_a = {'a': 1, 'b': 2}
map_b = {'b': 3, 'c': 4}

# Merging two dictionaries using the unpacking operator **
merged_map = {**map_a, **map_b}
print("Merged Dictionary:", merged_map)

# Merging two dictionaries using the update() method
merged_map = map_a.copy()  # Create a copy to avoid modifying the original
merged_map.update(map_b)
print("Merged Dictionary using update():", merged_map)

# Merging two dictionaries using the | operator (Python 3.9+)
merged_map = map_a | map_b
print("Merged Dictionary using | operator:", merged_map)
```

#### List Merging Techniques
```python
#!/usr/bin/env python3

array_a = [1, 2, 3]
array_b = [4, 5, 6]

# Merging two lists using the + operator
merged_array = array_a + array_b
print("Merged List using + operator:", merged_array)

# Merging two lists using unpacking operator *
merged_array = [*array_a, *array_b]
print("Merged List using unpacking * operator:", merged_array)

# Merging two lists using extend() method
merged_array = array_a.copy()  # Create a copy to avoid modifying the original
merged_array.extend(array_b)
print("Merged List using extend() method:", merged_array)

# Merging two lists using itertools.chain
import itertools
merged_array = list(itertools.chain(array_a, array_b))
print("Merged List using itertools.chain:", merged_array)
```

**Key Concepts:**
- Multiple approaches to merge dictionaries and lists
- Understanding performance implications of different methods
- Using unpacking operators `*` and `**` for merging
- Modern Python 3.9+ union operator `|` for dictionaries
- Choosing the right merging technique for your use case
- Preserving original data vs. in-place modifications

### 09. Ellipsis - The ... Operator
**Files:** `09/ellipsis.py`, `09/placeholder.py`, `09/argument.py`, `09/arbitrary.py`

Learn about Python's ellipsis (`...`) operator and its comprehensive use cases:

#### Basic Ellipsis Object (`09/ellipsis.py`)
```python
#!/usr/bin/env python3

print(...)
print(type(...))
```

#### Ellipsis as Placeholder (`09/placeholder.py`)
```python
#!/usr/bin/env python3

# Refer to https://docs.python.org/3/library/stdtypes.html#the-ellipsis-object

# Ellipsis as a placeholder (similar to pass)
def function_to_implement():
    ... # Placeholder for future implementation

class MyClass:
    def method_to_implement(self):
        ... # Placeholder for future implementation

if __name__ == '__main__':
    function_to_implement()
    obj = MyClass()
    obj.method_to_implement()
```

#### Ellipsis in Function Arguments (`09/argument.py`)
```python
#!/usr/bin/env python3

from typing import Any

def custom_random(start: Any = ..., end: Any = ...):
    import random
    if start is ...:
        start = 0
    if end is ...:
        end = 10
    return random.randint(start, end)

if __name__ == '__main__':
    print(custom_random())         # prints a random number between 0 and 10
    print(custom_random(start=5))  # prints a random number between 5 and 10
    print(custom_random(end=5))    # prints a random number between 0 and 5
    print(custom_random(3, 7))     # prints a random number between 3 and 7
```

#### Ellipsis in Type Hints (`09/arbitrary.py`)
```python
#!/usr/bin/env python3

def foo(array: tuple[int, ...]):
    # Function that takes a tuple of integers of any length
    print(array)

if __name__ == '__main__':
    foo((1, 2, 3))
    foo((4, 5))
    foo(())
```

**Key Concepts:**
- `...` (Ellipsis) as a built-in singleton object
- Using ellipsis as a placeholder like `pass`
- Ellipsis as default function argument values
- Type hint applications with `tuple[int, ...]` for arbitrary length
- Ellipsis in multi-dimensional array slicing (NumPy)
- `Callable[..., Any]` for functions with any arguments
- Custom implementations of ellipsis handling
- Advanced patterns for flexible APIs

## How to Run Examples

### Basic Pattern Examples
```bash
# Navigate to corresponding directory
cd lesson-99/01
python3 pass.py

# Run walrus operator example
cd lesson-99/02
python3 assignment.py

# Run comprehensions example
cd lesson-99/03
python3 comprehension.py

# Run del statement example
cd lesson-99/04
python3 del.py
```

### Naming Conventions and Special Features
```bash
# Navigate to section 05
cd lesson-99/05

# Run each example
python3 internal.py
python3 name_conflict.py
python3 name_mangling.py
python3 numeric_literals.py
python3 special.py
python3 underscore.py

# Try REPL special variable
python3
>>> 1 + 2
3
>>> _ * 3
9
>>> exit()
```

### Unpacking Patterns
```bash
# Navigate to section 06
cd lesson-99/06

# Run unpacking examples
python3 unpack_args.py
python3 unpack_return.py
```

### Advanced Control Flow
```bash
# Navigate to section 07
cd lesson-99/07

# Run for-else example (prime number finder)
python3 for_else.py

# Run try-except-else-finally example
python3 try_except_else_finally.py
```

### Data Structure Merging
```bash
# Navigate to section 08
cd lesson-99/08

# Run merging examples
python3 merge_dict.py
python3 merge_list.py
```

### Ellipsis Operator
```bash
# Navigate to section 09
cd lesson-99/09

# Run basic ellipsis examples
python3 ellipsis.py

# Run placeholder examples
python3 placeholder.py

# Run function argument examples
python3 argument.py

# Run type hint examples
python3 arbitrary.py

# Try interactive ellipsis examples
python3
>>> ...
Ellipsis
>>> type(...)
<class 'ellipsis'>
>>> ... is ...
True
>>> exit()
```

## Practice Suggestions

1. **Experiment with pass vs ellipsis**: Try using both `pass` and `...` as placeholders and understand when each is appropriate
2. **Master walrus operator patterns**: Practice using `:=` in different contexts like loops, conditionals, and comprehensions
3. **Build comprehensive data structures**: Create complex nested data using dictionary and list comprehensions
4. **Explore unpacking patterns**: Practice advanced unpacking with `*args`, `**kwargs`, and mixed assignments
5. **Implement naming conventions**: Create classes demonstrating proper use of `_`, `__`, and trailing underscores
6. **Design flexible APIs**: Use ellipsis in function signatures for optional parameters with meaningful defaults
7. **Apply control flow patterns**: Use for-else and try-except-else-finally in real problem-solving scenarios
8. **Compare merging techniques**: Benchmark different approaches for merging lists and dictionaries
9. **Custom ellipsis handling**: Implement classes that meaningfully handle ellipsis in `__getitem__` methods

## Related Resources

- [Python Enhancement Proposals (PEPs)](https://www.python.org/dev/peps/) - Official Python improvement proposals
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html) - Special methods and attributes
- [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/) - Official style guide
- [The Zen of Python (PEP 20)](https://www.python.org/dev/peps/pep-0020/) - Python philosophy
- [Effective Python](https://effectivepython.com/) - Best practices book
- [Python Tricks](https://realpython.com/python-tricks/) - Advanced Python techniques
- [Python Patterns](https://python-patterns.guide/) - Design patterns in Python
- [Real Python](https://realpython.com/) - Advanced Python tutorials and articles