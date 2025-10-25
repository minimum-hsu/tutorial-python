# Lesson 01 - Python Basic Output and print Function

This lesson introduces the most fundamental output operations in Python, including various uses of the `print()` function and output control techniques.

## Learning Objectives

- Understand Python basic output syntax
- Master the use of `print()` function parameters
- Learn the application of escape characters
- Understand standard error output
- Master list unpacking output

## Course Content

### 01. Hello World - Basic Output
**File:** `01/hello_world.py`

Learn basic `print()` syntax and parameter control:

```python
#!/usr/bin/env python3

# Basic output
print('hello world')

# Output multiple arguments
print('hello', 'world')

# Use sep parameter to change separator
print('hello', 'world', sep='_')
```

**Key Concepts:**
- Basic usage of `print()` function
- `sep` parameter controls separator between multiple arguments
- By default, multiple arguments are separated by spaces

### 02. Escape Characters
**File:** `02/escape_character.py`

Learn commonly used escape characters and output control:

```python
#!/usr/bin/env python3

# Newline character \n
print('hello\nworld')

# Tab character \t
print('hello\tpython')

# Vertical tab \v with end parameter
print('hello world', end='\v')
```

**Key Concepts:**
- `\n` - newline character
- `\t` - horizontal tab character
- `\v` - vertical tab character
- `end` parameter controls the ending character of output
- Reference ASCII character table: https://www.asciitable.com

### 03. Standard Error Output
**File:** `03/stderr.py`

Learn how to output to standard error stream:

```python
#!/usr/bin/env python3

import sys

# Output to standard error stream
print('error', file=sys.stderr)
```

**Key Concepts:**
- `sys.stderr` - standard error output stream
- `file` parameter specifies the output target
- Difference between standard output vs standard error

### 04. List Unpacking
**File:** `04/unpacking_list.py`

Learn to use `*` operator to unpack lists:

```python
#!/usr/bin/env python3

var_list = [1, 2, 3]

# Direct output of list (including brackets)
print(var_list)

# Use * to unpack list elements
print(*var_list)
```

**Key Concepts:**
- `*` operator is used to unpack iterable objects
- Unpacked output doesn't include container symbols
- Reference PEP 448: https://www.python.org/dev/peps/pep-0448/

## How to Run

Each example can be executed directly:

```bash
# Navigate to corresponding directory
cd lesson-01/01
python3 hello_world.py
```

```bash
cd lesson-01/02
python3 escape_character.py
```

```bash
cd lesson-01/03
python3 stderr.py
```

```bash
cd lesson-01/04
python3 unpacking_list.py
```

## Practice Suggestions

1. Try modifying the `sep` parameter with different separators
2. Experiment with combinations of various escape characters
3. Observe the differences between standard output and standard error (test with redirection)
4. Practice unpacking different types of iterable objects (lists, tuples, strings, etc.)

## Related Resources

- [Python Print Function Documentation](https://docs.python.org/3/library/functions.html#print)
- [ASCII Character Table](https://www.asciitable.com)
- [PEP 448 - Additional Unpacking Generalizations](https://www.python.org/dev/peps/pep-0448/)