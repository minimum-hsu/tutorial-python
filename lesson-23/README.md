# Lesson 23 - Singleton Pattern  <!-- omit in toc -->

This lesson explores the Singleton design pattern in Python, demonstrating how to restrict the instantiation of a class to one "single" instance using the `__new__` method and class-level caching.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. Singleton Implementation with \`__new__\`](#01-singleton-implementation-with-__new__)
  - [02. Singleton Pattern with Inheritance](#02-singleton-pattern-with-inheritance)
- [Design Pattern Overview](#design-pattern-overview)
  - [What is a Singleton?](#what-is-a-singleton)
  - [Key Mechanisms Used](#key-mechanisms-used)
- [How to Run Examples](#how-to-run-examples)
  - [01. Basic Singleton Example](#01-basic-singleton-example)
  - [02. Inherited Singleton Example](#02-inherited-singleton-example)
- [Best Practices](#best-practices)
- [Common Pitfalls](#common-pitfalls)
- [Practice Suggestions](#practice-suggestions)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Understand the concept and purpose of the Singleton design pattern.
- Learn how to override the `__new__` method to control instance creation.
- Use a class-level dictionary cache to store and retrieve existing instances.
- Manage initialization logic properly to avoid re-initializing cached instances.
- Apply the Singleton pattern in a hierarchy with class inheritance.

## Course Content

### 01. Singleton Implementation with \`__new__\`
**File:** `01/singleton.py`

This example demonstrates the core approach to implementing a Singleton in Python, where instances are uniquely identified and cached based on their arguments.

```python
from typing import ClassVar
from typing import Self

class Dog():
    # Class-level dictionary to cache instances based on arguments
    _instance_cache: ClassVar[dict[tuple, Self]] = {}
    _initialized: bool

    def __new__(cls, kind: str, name: str) -> Self:
        # Create a unique key using the class and arguments
        cache_key = (cls, kind, name)

        if cache_key not in cls._instance_cache:
            obj = super().__new__(cls)
            obj._initialized = False
            cls._instance_cache[cache_key] = obj
            print(f"Creating a new {cls.__name__} instance.")
        else:
            print(f"{cls.__name__} instance already exists. Returning the cached instance.")

        return cls._instance_cache[cache_key]

    def __init__(self, kind: str, name: str):
        # Prevent re-initialization if the instance is fetched from cache
        if getattr(self, "_initialized", False):
            return

        self.__kind = kind
        self.name = name
        self.legs = 4

        print("Initializing the Dog part.")
        self._initialized = True
```

**Key Concepts:**
- `__new__` vs `__init__`: `__new__` creates the object, `__init__` initializes it.
- **Instance Caching**: By checking the tuple `(cls, kind, name)` in a class var cache, identical requests return the exact same memory object.
- **Initialization Guard**: `_initialized` flag ensures `__init__` logic runs only once per unique instance.

### 02. Singleton Pattern with Inheritance
**File:** `02/singleton.py`

This example demonstrates applying the Singleton pattern across a class hierarchy (a base `Animal` class and a derived `Dog` class).

```python
class Animal():
    _instance_cache: ClassVar[dict[tuple, Self]] = {}
    _initialized: bool

    def __new__(cls, kind: str, name: str) -> Self:
        cache_key = (cls, kind, name)
        if cache_key not in cls._instance_cache:
            obj = super().__new__(cls)
            obj._initialized = False
            cls._instance_cache[cache_key] = obj
            print(f"Creating a new {cls.__name__} instance.")
        else:
            print(f"{cls.__name__} instance already exists. Returning the cached instance.")
        return cls._instance_cache[cache_key]

    def __init__(self, kind: str, name: str, legs: int):
        if getattr(self, "_initialized", False):
            return
        self.__kind = kind
        self.name = name
        self.legs = legs
        print("Initializing the Animal part.")
        if type(self) is Animal:
            self._initialized = True

class Dog(Animal):
    def __init__(self, kind: str, name: str):
        if getattr(self, "_initialized", False):
            return
        super().__init__(kind, name, 4)
        print("Initializing the Dog part.")
        self._initialized = True
```

**Key Concepts:**
- Inheritance: Subclasses automatically inherit the `__new__` caching logic.
- The `type(self) is BaseClass` check prevents the base class from marking a subclass instance as fully initialized prematurely.

## Design Pattern Overview

### What is a Singleton?
A Singleton ensures that a class has only one instance (or in this contextual case, one instance per unique set of arguments/cache key), and provides a global point of access to it.

### Key Mechanisms Used
1. **`__new__(cls, *args, **kwargs)`**: The magical method responsible for instance creation before `__init__` is invoked. Returning an existing cached object intercepts normal object creation.
2. **Class Variables**: Shared state across all instances. Useful for maintaining the cache dictionary.

## How to Run Examples

### 01. Basic Singleton Example
```bash
cd lesson-23/01
python3 singleton.py
```

### 02. Inherited Singleton Example
```bash
cd lesson-23/02
python3 singleton.py
```

## Best Practices

- **Initialization Checks**: Always wrap `__init__` body with an `if getattr(self, "_initialized", False): return` check when returning cached instances from `__new__`. Unlike `__new__`, `__init__` is generally called every time you invoke the class constructor.
- **Cache Key Consistency**: Ensure the caching key uniquely represents the inputs you want to be treated as equivalent instances.
- **Memory Management**: If caching instances permanently, consider using weak references if instances should be garbage-collected once no longer used elsewhere.

## Common Pitfalls

- **Re-initialization Overwriting**: Forgetting an `_initialized` check in `__init__` will cause existing instances to overwrite their internal state when retrieved from the cache.
- **Inheritance Traps**: In a hierarchy, `__init__` gets called dynamically for multiple layers. The initialization guard logic can become tricky to place perfectly (as shown in the `type(self) is Animal` check in `02/singleton.py`).
- **Thread Safety**: The dictionary-based cache approach in multi-threaded environments might cause race conditions without proper lock mechanisms.

## Practice Suggestions

1. **Multithreaded Singleton**: Modify the basic singleton to implement thread safety using the `threading.Lock` module.
2. **Metaclass Implementation**: Try implementing the Singleton pattern using a custom Metaclass instead of modifying the `__new__` method, and compare advantages.
3. **Database Connection Class**: Represent a shared Database configuration context using the Singleton pattern so all application modules share the same connections pool object.

## Related Resources

- [Python Data Model - __new__](https://docs.python.org/3/reference/datamodel.html#object.__new__)
- [Singleton Pattern Overview](https://refactoring.guru/design-patterns/singleton)
- [When to Use Singletons](https://en.wikipedia.org/wiki/Singleton_pattern)

