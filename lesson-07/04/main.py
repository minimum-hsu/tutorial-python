#!/usr/bin/env python3

import sys
from animal import Animal

class Dog(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 4)

    def run(self):
        print('I can run by {} legs'.format(self.legs))

class Bird(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 2)

if __name__ == '__main__':
    puppy = Dog(kind='Shiba', name='Maru')
    puppy.hello()
    puppy.run()

    try:
        # failed to exec
        # Animal.run() is abstract method, need Bird to implement it
        eagle = Bird(kind='Sea Eagle', name='Andro')
        eagle.hello()
        eagle.run()
    except TypeError as e:
        print('[Error]', e, file=sys.stderr)
