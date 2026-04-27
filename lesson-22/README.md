# Lesson 22 - Python Caching Patterns <!-- omit in toc -->

This lesson covers advanced caching patterns in Python, focusing on the use of `lru_cache`, `cached_property`, and `cachetools.cachedmethod` with functions, instance methods, class methods, and static methods. It also demonstrates common pitfalls such as memory leaks when caching instance methods incorrectly.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. Function Caching (`lru_cache`)](#01-function-caching-lru_cache)
  - [02. Instance Method Caching and Memory Leaks](#02-instance-method-caching-and-memory-leaks)
  - [03. Class Method and Static Method Caching](#03-class-method-and-static-method-caching)
- [How to Run](#how-to-run)
  - [Function caching](#function-caching)
  - [Instance method caching](#instance-method-caching)
  - [Cached property](#cached-property)
  - [Class method caching](#class-method-caching)
- [Summary](#summary)
<!-- /TOC -->

## Learning Objectives

- Understand the differences between function, instance method, class method, and static method in Python
- Learn to use `lru_cache`, `cached_property`, and `cachetools.cachedmethod` for efficient caching
- Recognize and avoid memory leaks caused by improper caching of instance methods
- Apply best practices for cache management in Python

## Course Content

### 01. Function Caching (`lru_cache`)
**File:** `01/function.py`

Demonstrates how to use `functools.lru_cache` to cache the result of a pure function. The example generates a random number and counts how many times the function is actually called, showing the effect of caching.

### 02. Instance Method Caching and Memory Leaks
**Files:**
- `02/instance_method.py`: Uses `cachetools.cachedmethod` to cache instance methods safely, avoiding memory leaks. Requires the `cachetools` package.
- `02/instance_method_memoryleack.py`: Shows that using `lru_cache` directly on instance methods causes memory leaks, because the cache holds a strong reference to the instance (`self`).
- `02/instance_property.py`: Uses `functools.cached_property` to cache a property value, suitable for values that only need to be computed once. Also demonstrates how to clear the cache and observe object deletion and garbage collection.
- `02/requirements.txt`: Install `cachetools` with:
  ```sh
  pip install cachetools
  ```

### 03. Class Method and Static Method Caching
**Files:**
- `03/class_method.py`: Uses `@classmethod` with `lru_cache` to cache class method results.
- `03/static_method.py`: Uses `@staticmethod` with `lru_cache` to cache static method results.

## How to Run

To run the examples in this lesson, use the following commands in your terminal:

### Function caching

```sh
cd lesson-22/01
python3 function.py
```

### Instance method caching

```sh
cd lesson-22/02
python3 instance_method.py

# Memory leak demonstration
python3 instance_method_memoryleack.py
```

### Cached property

```sh
cd lesson-22/02
python3 instance_property.py
```

### Class method caching

```sh
cd lesson-22/03
python3 class_method.py
```

## Summary

- Use `lru_cache` for pure functions, class methods, and static methods.
- For instance methods, prefer `cachetools.cachedmethod` or `cached_property` to avoid memory leaks.
- Always consider how caching affects object lifecycles and memory usage.
