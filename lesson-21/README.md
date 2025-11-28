# Lesson 21 - Python Generics and Type Hinting <!-- omit in toc -->

This lesson introduces Python generics and type hinting, including generic functions, generic classes, and type overloads. You'll learn how to write safer, more maintainable, and flexible code using advanced typing techniques.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. Type Hint Basics](#01-type-hint-basics)
  - [02. Type Overloading (Overload)](#02-type-overloading-overload)
  - [03. Generic Functions and Classes](#03-generic-functions-and-classes)
- [How to Run](#how-to-run)
- [Practice Suggestions](#practice-suggestions)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Understand Python type hinting syntax and usage
- Use generic types from the `typing` module
- Design generic functions and classes
- Apply type overloading (`@overload`) for flexible APIs
- Improve code safety and maintainability with static type checking

## Course Content

### 01. Type Hint Basics
**File:** `01/hint.py`

Learn how to use type hints in Python:

```python
#!/usr/bin/env python3
from typing import List, Dict

def greet(name: str) -> str:
    return f"Hello, {name}"

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def get_user_info() -> Dict[str, str]:
    return {"name": "Alice", "email": "alice@example.com"}
```

**Key Concepts:**
- Basic type hint syntax (`str`, `int`, `List`, `Dict`)
- Annotating function parameters and return types
- Static type checking tools (e.g., mypy)

---

### 02. Type Overloading (Overload)
**File:** `02/overload.py`

Learn how to use `@overload` for function type overloading:

```python
#!/usr/bin/env python3
from typing import overload, Union

@overload
def process(data: int) -> int: ...
@overload
def process(data: str) -> str: ...

def process(data: Union[int, str]) -> Union[int, str]:
    if isinstance(data, int):
        return data * 2
    elif isinstance(data, str):
        return data.upper()
    raise TypeError("Unsupported type")
```

**Key Concepts:**
- `@overload` for static type checking
- Implementing polymorphic functions
- Combining `Union` types and runtime type checks

---

### 03. Generic Functions and Classes
**Files:** `03/generic_function.py`, `03/generic_class.py`

Learn how to design generic functions and classes:

**Generic Function (`03/generic_function.py`)**
```python
#!/usr/bin/env python3
from typing import TypeVar, List

T = TypeVar('T')

def first_item(items: List[T]) -> T:
    return items[0]

print(first_item([1, 2, 3]))      # int
print(first_item(["a", "b"]))     # str
```

**Generic Class (`03/generic_class.py`)**
```python
#!/usr/bin/env python3
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def is_empty(self) -> bool:
        return not self._items

stack_int = Stack[int]()
stack_int.push(1)
stack_int.push(2)
print(stack_int.pop())  # 2

stack_str = Stack[str]()
stack_str.push("hello")
stack_str.push("world")
print(stack_str.pop())  # world
```

**Key Concepts:**
- `TypeVar` for defining generic type parameters
- Designing generic functions and classes
- `Generic[T]` base class
- Type-safe containers and data structures

---

## How to Run

Each example can be executed directly:

```bash
cd lesson-21/01
python3 hint.py
```

```bash
cd lesson-21/02
python3 overload.py
```

```bash
cd lesson-21/03
python3 generic_function.py
python3 generic_class.py
```

## Practice Suggestions

1. Design your own generic container class (e.g., Queue, Tree)
2. Practice using @overload for polymorphic APIs
3. Combine type hints and generics for complex data structures
4. Use mypy to check type safety
5. Try adding generics and type hints to your own projects

## Related Resources

- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [PEP 544 - Protocols](https://www.python.org/dev/peps/pep-0544/)
- [Python typing documentation](https://docs.python.org/3/library/typing.html)
- [mypy type checker](http://mypy-lang.org/)
- [Real Python: Generics](https://realpython.com/python-generics/)

---

For more advanced generic techniques or type design examples, feel free to ask!
