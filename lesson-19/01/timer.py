#!/usr/bin/env python3

# A simple decorator to measure execution time

import time

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds to execute.")
        return result

    return wrapper

@timer
def slow_function():
    time.sleep(2)

if __name__ == "__main__":
    slow_function()
