#!/usr/bin/env python3

from animal import Animal

class Dog(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 4)

    def run(self):
        print('I can run by {} legs'.format(self.legs))

class Bird(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 2)

    def run(self):
        print('I can jump by {} legs'.format(self.legs))

if __name__ == '__main__':
    puppy = Dog(kind = 'Shiba', name = 'Maru')
    puppy.hello()
    puppy.run()

    eagle = Bird(kind = 'Sea Eagle', name = 'Andro')
    eagle.hello()
    eagle.run()
