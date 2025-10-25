#!/usr/bin/env python3

from animal import Animal
import sys
from typing import override

class Dog(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 4)

    @override
    def run(self):
        print('I can run by {} legs'.format(self.legs))

    @override
    @classmethod
    def info(cls):
        print('This is Dog class.')


if __name__ == '__main__':
    try:
        # failed to run
        # hello() is instance method, need instance to call
        Animal.hello()
    except TypeError as e:
        print('[Error]', e, file = sys.stderr)

    # correct way to call class method
    Animal.info()
    Dog.info()

    puppy = Dog(kind = 'Shiba', name = 'Maru')
    puppy.hello()
    puppy.run()
