#!/usr/bin/env python3

from animal import Animal
import sys


class Dog(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 4)

    def run(self):
        print('I can run by {} legs'.format(self.legs))


if __name__ == '__main__':
    try:
        Animal.hello() ## failed to run
    except TypeError as e:
        print('[Error]', e, file = sys.stderr)   
    Animal.run()

    puppy = Dog(kind = 'Shiba', name = 'Maru')
    puppy.hello()
    puppy.run()
