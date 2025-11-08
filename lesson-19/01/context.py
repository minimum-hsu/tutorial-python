#!/usr/bin/env python3

# Using context manager to measure execution time

import time
from contextlib import contextmanager

@contextmanager
def timer(name="block"):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"{name} took {end - start:.4f} seconds to execute.")

def slow_function():
    time.sleep(2)

if __name__ == "__main__":
    with timer(slow_function.__name__):
        slow_function()
