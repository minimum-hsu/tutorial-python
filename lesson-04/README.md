# Lesson 04 - Python Loops and Iteration  <!-- omit in toc -->

This lesson covers Python's loop structures, including for loops, while loops, loop control statements, and list comprehensions for efficient iteration and data processing.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. For Loops](#01-for-loops)
  - [02. While Loops](#02-while-loops)
  - [03. Loop Control Statements](#03-loop-control-statements)
  - [04. List Comprehensions](#04-list-comprehensions)
- [Loop Comparison](#loop-comparison)
- [How to Run](#how-to-run)
- [Practice Suggestions](#practice-suggestions)
- [Performance Tips](#performance-tips)
- [Advanced Topics to Explore](#advanced-topics-to-explore)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Master for loops and iteration over sequences
- Understand nested loops and their applications
- Learn while loops and their use cases
- Master loop control with break and continue
- Understand list comprehensions for concise data processing
- Compare different iteration approaches

## Course Content

### 01. For Loops
**Files:** `01/for.py`, `01/nested_for.py`

Learn the fundamentals of for loops and nested iterations:

**Basic For Loop (`01/for.py`)**
```python
#!/usr/bin/env python3

names = ['Alice', 'Bob', 'John']

for name in names:
    print(name)
```

**Nested For Loop (`01/nested_for.py`)**
```python
#!/usr/bin/env python3

def multiplication_table():
    for multiplicand in range(1, 10):
        for multiplier in range(1, 10):
            print(multiplicand, 'x', multiplier, '=', multiplicand * multiplier)

if __name__ == '__main__':
    multiplication_table()
```

**Key Concepts:**
- `for` loop syntax for iterating over sequences
- Iteration over lists, strings, and other iterables
- `range()` function for generating number sequences
- Nested loops for multi-dimensional operations
- Variable naming in loop contexts (multiplicand, multiplier)

### 02. While Loops
**File:** `02/while.py`

Learn condition-based iteration with while loops:

```python
#!/usr/bin/env python3

count = 0

while count < 5:
    print(count)
    count += 1
```

**Key Concepts:**
- `while` loop syntax for condition-based iteration
- Loop counter and increment operations
- `+=` operator for incrementing values
- Preventing infinite loops with proper conditions
- When to use while vs for loops

### 03. Loop Control Statements
**Files:** `03/break.py`, `03/continue.py`

Learn how to control loop execution with break and continue:

**Break Statement (`03/break.py`)**
```python
#!/usr/bin/env python3

from random import randint

match = [1, 3]

while True:  # Infinite loop until break
    number = randint(0, 10)

    if number in match:
        print(number, 'is matched')
        break  # Exit the loop
    else:
        print(number, 'is not matched')
```

**Continue Statement (`03/continue.py`)**
```python
#!/usr/bin/env python3

for number in range(0, 10):
    if number % 2:  # If number is odd
        continue  # Skip to next iteration

    print(number)  # Only prints even numbers
```

**Key Concepts:**
- `break` statement to exit loops early
- `continue` statement to skip current iteration
- `while True` pattern for infinite loops
- Random number generation with `randint()`
- Modulo operator `%` for checking even/odd numbers
- `in` operator for membership testing

### 04. List Comprehensions
**File:** `04/list_comprehension.py`

Learn concise ways to create lists with list comprehensions:

```python
#!/usr/bin/env python3

def double(number: int) -> int:
    return number * 2

if __name__ == '__main__':
    array = range(0, 5)

    # List comprehension
    doubled = [double(number) for number in array]
    print(doubled)  # Output: [0, 2, 4, 6, 8]

    # List comprehension with condition
    even = [number for number in array if number % 2 == 0]
    print(even)  # Output: [0, 2, 4]
```

**Key Concepts:**
- List comprehension syntax: `[expression for item in iterable]`
- Conditional list comprehensions: `[expression for item in iterable if condition]`
- Function calls within list comprehensions
- More concise than traditional for loops
- Functional programming approach

## Loop Comparison

| Loop Type | Best For | Use Cases | Pros | Cons |
|-----------|----------|-----------|------|------|
| **for** | Known iterations | Lists, ranges, sequences | Clean, readable | Less flexible for complex conditions |
| **while** | Condition-based | Unknown iterations, events | Flexible conditions | Risk of infinite loops |
| **List Comprehension** | Data transformation | Creating new lists | Concise, efficient | Can be less readable for complex logic |

## How to Run

Each example can be executed directly:

```bash
# Navigate to corresponding directory
cd lesson-04/01
python3 for.py
python3 nested_for.py
```

```bash
cd lesson-04/02
python3 while.py
```

```bash
cd lesson-04/03
python3 break.py
python3 continue.py
```

```bash
cd lesson-04/04
python3 list_comprehension.py
```

## Practice Suggestions

1. **For Loop Variations**:
   - Iterate over different data types (strings, tuples, dictionaries)
   - Use `enumerate()` to get both index and value
   - Try `zip()` to iterate over multiple sequences

2. **While Loop Practice**:
   - Create a guessing game using while loops
   - Implement input validation with while loops
   - Practice with different termination conditions

3. **Loop Control Mastery**:
   - Use break and continue in nested loops
   - Implement search algorithms with early termination
   - Create menu systems with loop control

4. **List Comprehension Challenges**:
   - Convert nested for loops to list comprehensions
   - Create dictionary and set comprehensions
   - Combine multiple conditions in comprehensions

## Performance Tips

- **List Comprehensions** are generally faster than equivalent for loops
- **Generator Expressions** `(expression for item in iterable)` are memory-efficient for large datasets
- **Built-in Functions** like `map()`, `filter()` can be alternatives to list comprehensions
- **Early Termination** with break can improve performance in search operations

## Advanced Topics to Explore

- **Generator Expressions**: Memory-efficient iteration
- **Iterator Protocol**: Creating custom iterables
- **Nested Comprehensions**: Multi-dimensional data processing
- **enumerate() and zip()**: Advanced iteration techniques
- **else Clauses**: Using else with for and while loops

## Related Resources

- [Python For Loops Documentation](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python While Loops Documentation](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
- [List Comprehensions Documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Built-in Functions Documentation](https://docs.python.org/3/library/functions.html)
- [PEP 202 - List Comprehensions](https://www.python.org/dev/peps/pep-0202/)