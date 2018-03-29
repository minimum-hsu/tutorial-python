#!/usr/bin/env python3

import sys

def throw_exception():
    names = ['Alice', 'Bob', 'Charlie']

    for i in range(4):
        print(names[i])

if __name__ == '__main__':
    try:
        throw_exception()
    except IndexError as err:
        print('[Error]', err, file = sys.stderr)
    else:
        print('no exception launched')
    finally:
        print('finally block is always executed')
