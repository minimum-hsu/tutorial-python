#!/usr/bin/env python3

from functools import lru_cache

@lru_cache(maxsize=32)
def fibonacci(n: int) -> int:
    print(f"Calculating fibonacci({n})")

    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print("Calculating Fibonacci numbers with caching:")
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

    print(fibonacci.cache_info())

    print("\nRecalculating Fibonacci numbers to demonstrate caching:")
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci(i)}")
