#!/usr/bin/env python3

import sys
from typing import override
from animal import Animal

class Dog(Animal):
    def __init__(self, kind: str, name: str):
        # see super method (https://docs.python.org/2/library/functions.html#super)
        super().__init__(kind, name, 4)

    @override  # optional, but good practice to indicate overriding method
    def run(self):
        print('I can run by {} legs'.format(self.legs))

    def echo_kind(self):
        print('I am {}.'.format(self.__kind))  # __kind is private attribute of Animal

if __name__ == '__main__':
    puppy = Dog(kind='Shiba', name='Maru')

    puppy.hello()
    puppy.run()

    try:
        # failed to access private attribute
        puppy.echo_kind()
    except AttributeError as e:
        print('[Error]', e, file=sys.stderr)
