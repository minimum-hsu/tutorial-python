#!/usr/bin/env python3

from functools import lru_cache
import gc
import random
from time import time

call_count = {"count": 0}

class NumberGenerator:
    """OBSERVATION: Using functools.lru_cache on instance methods causes memory leaks.

    Reason: The functools.lru_cache is stored on the function object associated with the class.
    It maintains a mapping of (self, *args) -> result. Since 'self' is part of the cache key,
    the cache holds a STRONG REFERENCE to the instance, preventing Garbage Collection (GC).

    You should use functools.cached_property or cachetools.cachedmethod instead.
    """

    @lru_cache
    def generate_number(self) -> int:
        """Generates a random number between 1 and 10000."""
        call_count["count"] += 1
        random.seed(time())
        return random.randint(1, 10000)  # noqa:S311

    def cache_clear(self):
        """Clear the cache"""
        self.generate_number.cache_clear()

    def __del__(self):
        print("NumberGenerator instance is being deleted.", flush=True)

if __name__ == "__main__":
    generator = NumberGenerator()
    number1 = generator.generate_number()
    print(f"Generated number: {number1}")
    number2 = generator.generate_number()
    print(f"Generated number: {number2}")
    print(f"Method was called {call_count['count']} times.")

    del generator  # Delete the instance to see if the cache is cleared
    print("Deleted the generator instance and forcing garbage collection...")
    gc.collect()  # Force garbage collection to see if the instance is deleted

    print("The instance is still alive because it's being 'held' by the lru_cache internal dictionary.")
    # Note: The "NumberGenerator instance is being deleted" message will appear
    # AFTER this line because the process is shutting down and clearing class-level objects.
