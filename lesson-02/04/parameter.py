#!/usr/bin/env python3

## Python ignores type hint at runtime.
## see PEP 484 (https://www.python.org/dev/peps/pep-0484/)
def hello(name):  # the parameter is 'name'
    print('hello', name)

if __name__ == '__main__':
    hello('Alice') # the argument is 'Alice'
