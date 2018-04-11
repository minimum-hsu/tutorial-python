#!/usr/bin/env python3

class Dog():
    def __init__(self, kind: str, name: str):
        '''
        The first step when creating a new object
        '''

        ## Why is underscore used? see PEP 8 (https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles)

        self.__kind = kind
        self.name = name
        self.legs = 4

    def hello(self):
        print('My name is {}. I am {}.'.format(self.name, self.__kind))

    def run(self):
        print('I can run by {} legs'.format(self.legs))


if __name__ == '__main__':
    puppy = Dog(kind = 'Shiba', name = 'Maru')

    puppy.hello()
    puppy.run()

