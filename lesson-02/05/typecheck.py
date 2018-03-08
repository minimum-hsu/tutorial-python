#!/usr/bin/env python3

def hello(name: str):
    assert isinstance(name, str)
    print('hello', name)

if __name__ == '__main__':
    hello('Alice')
    hello(['Bob'])
