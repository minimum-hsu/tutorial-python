#!/usr/bin/env python3

from animal import Animal
import sys


class Dog(Animal):
    def __init__(self, kind: str, name: str):
        ## see super method (https://docs.python.org/2/library/functions.html#super)
        super().__init__(kind, name, 4)

    def run(self):
        print('I can run by {} legs'.format(self.legs))

    def echo_kind(self):
        print('I am {}.'.format(self.__kind)) ## __kind is private variable of Animal class


if __name__ == '__main__':
    puppy = Dog(kind = 'Shiba', name = 'Maru')

    puppy.hello()
    puppy.run()
    try:
        puppy.echo_kind() ## failed to exec
    except AttributeError as e:
        print('[Error]', e, file = sys.stderr)

