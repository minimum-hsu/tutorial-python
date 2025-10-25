#!/usr/bin/env python3

def hello(name: str):
    print('hello', name)

if __name__ == '__main__':
    hello('Alice')

    # When you use Pylance or other type checkers, the following line will raise a type error.
    # But Python itself will not raise any error at runtime.
    hello(['Bob'])

    # suppress type checker warnings with 'type: ignore' comment
    hello(['Charlie']) # type: ignore
