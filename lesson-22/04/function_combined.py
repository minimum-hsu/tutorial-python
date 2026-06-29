#!/usr/bin/env python3

"""
This module provides a typed version of the lru_cache decorator that preserves the original function's type hints.
It also demonstrates the use of the cachetools library to handle unhashable types in Python.
"""

import random
from time import time
from typing import Any
from typing import Callable
from cachetools import LRUCache
from cachetools import cached
from cachetools import keys
import wrapt

def lru_cache(
    key: Callable[..., Any] = keys.hashkey,
    maxsize: int = 128
):
    """A decorator that applies an LRU cache to a function while preserving its type hints.

    Args:
        key (Callable[..., Any], optional): A function that generates a cache key based on the function's arguments. Defaults to `cachetools.keys.hashkey`, which generates a hashable key based on the function's arguments.
        maxsize (int, optional): The maximum size of the cache. When the cache exceeds this size, the least recently used items will be discarded. Defaults to 128.

    Returns:
        Callable[..., Any]: A decorator that can be applied to a function to enable LRU caching with the specified key generation and maximum size. The decorated function will have the same signature and type hints as the original function.
    """

    def decorator[**P, R](func: Callable[P, R]) -> Callable[P, R]:
        """A typed version of the lru_cache decorator that preserves the original function's type hints.

        Args:
            func (Callable[P, R]): The target function to be decorated.

        Returns:
            Callable[P, R]: A wrapped function with the same signature and caching enabled.
        """

        # Use functools.lru_cache to create a cached version of the function
        cached_func = cached(cache=LRUCache(maxsize=maxsize), key=key)(func)

        @wrapt.decorator
        def wrapper(wrapped: Callable[P, R], instance: Any, args: Any, kwargs: Any) -> R:
            return cached_func(*args, **kwargs)

        # Use the wrapper to create a new function that preserves the original function's signature
        wrapped_func = wrapper(func)

        # Add the cache_clear method to the wrapped function so it can be cleared if needed
        wrapped_func.cache_clear = cached_func.cache_clear  # type: ignore[attr-defined]

        return wrapped_func

    return decorator

call_count = {"count": 0}

@lru_cache(key=lambda *args, **kwargs: str(args) + str(kwargs))
def choice(arr: list[int]) -> int:
    """Randomly choose an element from the given list."""
    call_count["count"] += 1
    random.seed(time())
    return random.choice(arr)

if __name__ == "__main__":
    arr = list(range(1, 10001))
    number1 = choice(arr)
    print(f"Generated number: {number1}")
    number2 = choice(arr)
    print(f"Generated number: {number2}")
    print(f"Function was called {call_count['count']} times.")
