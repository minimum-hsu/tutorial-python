#!/usr/bin/env python3

def hello(name: str):
    assert isinstance(name, str)
    print('hello', name)

if __name__ == '__main__':
    hello('Alice')

    # raise an AssertionError when the type is incorrect
    hello(['Bob'])
