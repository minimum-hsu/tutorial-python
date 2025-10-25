#!/usr/bin/env python3

def hello(greeting, name, title):
    print(greeting, title, name)

# Special parameters: '/' indicates positional-only parameters, '*' indicates keyword-only parameters.
# Refer to https://docs.python.org/3/tutorial/controlflow.html#special-parameters
def hi(greeting, /, name, *, title):
    print(greeting, title, name)

if __name__ == '__main__':
    # Positional arguments
    hello('Hello,', 'Alice', 'Ms.')

    # Keyword arguments
    hello(greeting='Hello,', name='Bob', title='Mr.')

    # Mixed positional and keyword arguments
    # Note: Positional arguments must come before keyword arguments
    hello('Hello', title='Dr.', name='Charlie')

    # Using special parameters
    hi('Hi,', 'Alice', title='Ms.')
    hi('Hi,', name='Bob', title='Mr.')
