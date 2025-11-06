#!/usr/bin/env python3

def hello(greeting, name, title):
    print(greeting, title, name)

if __name__ == '__main__':
    # Unpacking argument lists
    # Refer to https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

    args = ('Hello,', 'Alice', 'Ms.')
    hello(*args)

    kwargs = {'greeting': 'Hi,', 'name': 'Bob', 'title': 'Mr.'}
    hello(**kwargs)
