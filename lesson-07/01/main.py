#!/usr/bin/env python3

from animal import Animal


class Dog(Animal):
    def __init__(self, kind: str, name: str):
        ## see super method (https://docs.python.org/2/library/functions.html#super)
        super().__init__(kind, name, 4)

    def run(self):
        print('I can run by {} legs'.format(self.legs))


class Bird(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 2)


if __name__ == '__main__':
    # Animal.hello() ## failed to run
    Animal.run() ## nothing

    puppy = Dog(kind = 'Shiba', name = 'Maru')
    eagle = Bird(kind = 'Sea Eagle', name = 'Andro')

    puppy.hello()
    puppy.run()

    eagle.hello()
    eagle.run()
