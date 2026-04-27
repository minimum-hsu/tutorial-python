#!/usr/bin/env python3

from functools import lru_cache
import random
from time import time

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
