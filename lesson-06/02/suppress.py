#!/usr/bin/env python3

from contextlib import suppress

def throw_exception():
    names = ['Alice', 'Bob', 'Charlie']

    for i in range(4):
        print(names[i])

if __name__ == '__main__':
    # Suppress IndexError exceptions
    with suppress(IndexError):
        throw_exception()
