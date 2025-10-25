#!/usr/bin/env python3

def throw_exception():
    raise Exception('Custom exception')

if __name__ == '__main__':
    throw_exception()
    # This will raise:
    # Exception: Custom exception
