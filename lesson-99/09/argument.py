#!/usr/bin/env python3

from typing import Any

def custom_random(start: Any = ..., end: Any = ...):
    import random
    if start is ...:
        start = 0
    if end is ...:
        end = 10
    return random.randint(start, end)

if __name__ == '__main__':
    print(custom_random())         # prints a random number between 0 and 10
    print(custom_random(start=5))  # prints a random number between 5 and 10
    print(custom_random(end=5))    # prints a random number between 0 and 5
    print(custom_random(3, 7))     # prints a random number between 3 and 7