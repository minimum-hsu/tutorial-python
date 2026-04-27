#!/usr/bin/env python3

from functools import partial
import gc
import random
from time import time
from cachetools import LRUCache
from cachetools import cachedmethod
from cachetools.keys import methodkey

call_count = {"count": 0}

class NumberGenerator:
    """Use cachetools.cachedmethod to avoid memory leaks with instance methods."""

    def __init__(self):
        self._cache = LRUCache(maxsize=128)

    @cachedmethod(lambda self: self._cache,
                  key=partial(methodkey, method="generate_number"))
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

    print("The instance should be deleted now, and you should see the message from __del__.")
