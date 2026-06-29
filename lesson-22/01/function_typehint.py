import functools
import random
from time import time
from typing import Any
from typing import Callable
import wrapt

def lru_cache[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """A typed version of the lru_cache decorator that preserves the original function's type hints.

    Args:
        func (Callable[P, R]): The target function to be decorated.

    Returns:
        Callable[P, R]: A wrapped function with the same signature and caching enabled.
    """

    # Use functools.lru_cache to create a cached version of the function
    cached_func = functools.lru_cache(func)

    @wrapt.decorator
    def wrapper(wrapped: Callable[P, R], instance: Any, args: Any, kwargs: Any) -> R:
        return cached_func(*args, **kwargs)

    # Use the wrapper to create a new function that preserves the original function's signature
    wrapped_func = wrapper(func)

    # Add the cache_clear method to the wrapped function so it can be cleared if needed
    wrapped_func.cache_clear = cached_func.cache_clear  # type: ignore[attr-defined]

    return wrapped_func

call_count = {"count": 0}

@lru_cache
def generate_number() -> int:
    """Generates a random number between 1 and 10000."""
    call_count["count"] += 1
    random.seed(time())
    return random.randint(1, 10000)  # noqa:S311

if __name__ == "__main__":
    number1 = generate_number()
    print(f"Generated number: {number1}")
    number2 = generate_number()
    print(f"Generated number: {number2}")
    print(f"Function was called {call_count['count']} times.")
