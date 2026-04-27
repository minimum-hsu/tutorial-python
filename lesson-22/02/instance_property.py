#!/usr/bin/env python3

from contextlib import suppress
from functools import cached_property
import gc
import random
from time import time

call_count = {"count": 0}

class NumberGenerator:
    """Use functools.cached_property"""

    @cached_property
    def number(self) -> int:
        """Generates a random number between 1 and 10000."""
        call_count["count"] += 1
        random.seed(time())
        return random.randint(1, 10000)  # noqa:S311

    def cache_clear(self):
        """Clear the cache"""
        with suppress(AttributeError):
            del self.number

    def __del__(self):
        print("NumberGenerator instance is being deleted.", flush=True)

if __name__ == "__main__":
    generator = NumberGenerator()
    number1 = generator.number
    print(f"Generated number: {number1}")
    number2 = generator.number
    print(f"Generated number: {number2}")
    print(f"Method was called {call_count['count']} times.")

    del generator  # Delete the instance to see if the cache is cleared
    print("Deleted the generator instance and forcing garbage collection...")
    gc.collect()  # Force garbage collection to see if the instance is deleted

    print("The instance should be deleted now, and you should see the message from __del__.")
