# Lesson 22 - Python Methods and Caching Patterns <!-- omit in toc -->

This lesson covers advanced caching patterns in Python, focusing on the use of `lru_cache`, `cached_property`, and `cachetools.cachedmethod`. You'll learn how to properly cache results for functions, instance methods, class methods, and static methods, and how to avoid common pitfalls like memory leaks when caching object instances.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. Function Caching](#01-function-caching)
  - [02. Instance Method Caching & Memory Leaks](#02-instance-method-caching--memory-leaks)
  - [03. Class Method & Static Method Caching](#03-class-method--static-method-caching)
- [How to Run Examples](#how-to-run-examples)
  - [01. Function Caching](#01-function-caching-1)
  - [02. Instance Method Caching](#02-instance-method-caching)
  - [03. Class & Static Methods](#03-class--static-methods)
- [Practice Suggestions](#practice-suggestions)
- [Common Pitfalls](#common-pitfalls)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Understand the differences between pure functions, instance methods, class methods, and static methods.
- Master Python's built-in caching decorators: `@lru_cache` and `@cached_property`.
- Recognize memory leak scenarios when directly applying `@lru_cache` on instance methods.
- Implement safe caching for instance methods using `cachetools.cachedmethod`.
- Apply type hints properly when dealing with decorators and caching libraries.
- Control cache lifecycles and forcefully clear cached results.

## Course Content

### 01. Function Caching
**Files:** `01/function.py`, `01/function_typehint.py`

Demonstrates how to use `functools.lru_cache` to cache the return value of a pure function, and how to preserve type hints using `wrapt`.

**Key Concepts:**
- Basic caching with `@lru_cache`.
- Performance tracking using a global `call_count` dictionary.
- Understanding how identical calls retrieve cached results without executing the function body.
- Using `wrapt.decorator` to build custom decorators that perfectly preserve docstrings, type hints, and function signatures.

---

### 02. Instance Method Caching & Memory Leaks
**Files:** `02/instance_method.py`, `02/instance_method_memoryleack.py`, `02/instance_property.py`

Explores the dangers of using `lru_cache` directly on instance methods and how to correctly address them using `cached_property` or external libraries like `cachetools`.

**Key Concepts:**
- **Memory Leaks:** `instance_method_memoryleack.py` shows how `lru_cache` stores a strong reference to `self` in the cache key, preventing Garbage Collection (GC) from deleting instances.
- **Safe Method Caching:** `instance_method.py` uses `cachetools.cachedmethod` to link the cache's lifecycle to the instance itself.
- **Property Caching:** `instance_property.py` uses `functools.cached_property` for values that only need one-time computation per instance, and shows how to invalidate the cache by calling `del self.attribute_name`.

---

### 03. Class Method & Static Method Caching
**Files:** `03/class_method.py`, `03/static_method.py`

Shows how caching decorators interact with class-level methods.

**Key Concepts:**
- Combining `@classmethod` with `@lru_cache` to cache operations operating on the class object (`cls`).
- Combining `@staticmethod` with `@lru_cache` for pure utility functions bounded to a class namespace.

## How to Run Examples

### 01. Function Caching
```sh
cd lesson-22/01
pip install -r requirements.txt
python3 function.py
python3 function_typehint.py
```

### 02. Instance Method Caching
```sh
cd lesson-22/02
# Install required dependencies
pip install -r requirements.txt

# Run safe caching example
python3 instance_method.py

# Run memory leak demonstration
python3 instance_method_memoryleack.py

# Run cached property example
python3 instance_property.py
```

### 03. Class & Static Methods
```sh
cd lesson-22/03
python3 class_method.py
python3 static_method.py
```

## Practice Suggestions

- Try changing the `maxsize` of the LRU cache (e.g., `LRUCache(maxsize=2)`) and execute the methods multiple times to see cache eviction in action.
- Modify `class_method.py` to create multiple inherited classes and observe if they share the same cache or maintain separate caches.
- Use the `timeit` module to benchmark the speed difference between a cached recursive function (like Fibonacci) and an uncached one.

## Common Pitfalls
- Stacking `@lru_cache` with `@classmethod` historically caused issues in older Python versions; always place `@classmethod` as the outermost decorator (top).
- Never use `@lru_cache` recursively on object methods if you create and destroy millions of short-lived objects. The global cache will prevent them from ever dying. Use `cachetools`!

## Related Resources
- [functools — Higher-order functions and operations on callable objects](https://docs.python.org/3/library/functools.html)
- [cachetools documentation](https://cachetools.readthedocs.io/en/latest/)
- [wrapt documentation](https://wrapt.readthedocs.io/en/latest/)
