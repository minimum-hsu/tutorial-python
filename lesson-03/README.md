# Lesson 03 - Python Control Flow: Conditional Statements

This lesson covers Python's conditional statements, including if-else statements, switch-case alternatives, and the modern match-case statement.

## Learning Objectives

- Master if-else conditional statements
- Understand chained comparisons
- Learn dictionary-based switch-case alternatives
- Understand the modern match-case statement (Python 3.10+)
- Compare different approaches for conditional logic

## Course Content

### 01. If-Else Statements
**File:** `01/if_else.py`

Learn the fundamentals of conditional statements in Python:

```python
#!/usr/bin/env python3

name = 'Alice'
count = len(name)

# Simple if-else statement
if count is 5:  # same as "count == 5"
    print('[1] size of', name, 'is 5')
else:
    print('[1] size of', name, 'is not 5')

# if-elif-else statement
if count < 3:
    print('[3] size of', name, 'is less than 3')
elif count > 6:
    print('[3] size of', name, 'is greater than 6')
else:
    print('[3] size of', name, 'is between 3 and 6')

# Chained comparison
if 3 < count < 6:
    print('[2] size of', name, 'is between 3 and 6')
else:
    print('[2] size of', name, 'is not between 3 and 6')
```

**Key Concepts:**
- Basic `if-else` syntax
- `elif` for multiple conditions
- `is` operator vs `==` operator
- Chained comparisons (e.g., `3 < count < 6`)
- Python's readable comparison syntax
- Reference: [Comparisons Documentation](https://docs.python.org/3/reference/expressions.html#comparisons)

### 02. Switch-Case Alternative (Dictionary Dispatch)
**File:** `02/switch_case.py`

Learn how to implement switch-case behavior using dictionaries:

```python
#!/usr/bin/env python3

from random import randint

def get():
    print('you get data from database')

def delete():
    print('you delete data in database')

def insert():
    print('you insert data to database')

# Dictionary-based switch-case alternative
action = {
    0: get,
    1: delete,
    2: insert
}

if __name__ == '__main__':
    index = randint(0, 2)  # simulate user choice
    action[index]()
```

**Key Concepts:**
- Dictionary dispatch pattern
- Function objects as dictionary values
- Cleaner alternative to multiple if-elif statements
- Dynamic function calling
- Random number generation with `randint()`

### 03. Match-Case Statement (Python 3.10+)
**File:** `03/match.py`

Learn the modern match-case statement introduced in Python 3.10:

```python
#!/usr/bin/env python3

def action(value):
    # match-case statement
    match value:
        case 0:
            print('you get data from database')
        case 1:
            print('you delete data in database')
        case 2:
            print('you insert data to database')
        case _:  # wildcard pattern (default case)
            print('unknown action')

if __name__ == '__main__':
    for i in range(4):  # simulate user choice
        action(i)
```

**Key Concepts:**
- `match-case` syntax (Python 3.10+ feature)
- Pattern matching capabilities
- Wildcard pattern `_` for default case
- More powerful than traditional switch-case
- Structural pattern matching support
- Reference: [Match Statements Documentation](https://docs.python.org/3/tutorial/controlflow.html#match-statements)

## Comparison of Approaches

| Approach | Best For | Python Version | Pros | Cons |
|----------|----------|----------------|------|------|
| **if-elif-else** | Complex conditions, ranges | All versions | Flexible, readable | Verbose for simple switches |
| **Dictionary Dispatch** | Simple value mapping | All versions | Clean, fast lookup | Limited to exact matches |
| **match-case** | Pattern matching, complex cases | 3.10+ | Powerful, expressive | Requires newer Python |

## How to Run

Each example can be executed directly:

```bash
#Navigate to corresponding directory
cd lesson-03/01
python3 if_else.py
```

```bash
cd lesson-03/02
python3 switch_case.py
```

```bash
cd lesson-03/03
python3 match.py
```

**Note:** The `match.py` example requires Python 3.10 or later. If you're using an older version, you'll get a syntax error.

## Practice Suggestions

1. **Condition Variations**:
   - Modify the conditions in `if_else.py` to test different scenarios
   - Experiment with different comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)

2. **Dictionary Dispatch**:
   - Add more functions to the action dictionary
   - Try using lambda functions as dictionary values
   - Handle cases where the key doesn't exist

3. **Match-Case Exploration**:
   - Add more cases to the match statement
   - Experiment with guard clauses using `if` in case statements
   - Try pattern matching with lists, tuples, or objects

4. **Performance Comparison**:
   - Compare the performance of different approaches with large datasets
   - Measure execution time for each method

## Advanced Topics to Explore

- **Guard Clauses**: Using `if` conditions within match cases
- **Pattern Matching**: Matching complex data structures
- **Capture Patterns**: Extracting values during matching
- **Class Patterns**: Matching based on object types and attributes

## Related Resources

- [Python Control Flow Documentation](https://docs.python.org/3/tutorial/controlflow.html)
- [Comparison Operations](https://docs.python.org/3/reference/expressions.html#comparisons)
- [Match Statements (Python 3.10+)](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
- [PEP 634 - Structural Pattern Matching](https://www.python.org/dev/peps/pep-0634/)
- [Dictionary Methods Documentation](https://docs.python.org/3/library/stdtypes.html#dict)