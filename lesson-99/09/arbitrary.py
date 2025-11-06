#!/usr/bin/env python3

def foo(array: tuple[int, ...]):
    # Function that takes a tuple of integers of any length
    print(array)

if __name__ == '__main__':
    foo((1, 2, 3))
    foo((4, 5))
    foo(())