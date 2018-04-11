#!/usr/bin/env python3

## What is __init__ method? see objects (https://docs.python.org/3/reference/datamodel.html#basic-customization)

class Animal():

    def __init__(self, kind: str, name: str, legs: int):
        '''
        The first step when creating a new object
        '''

        ## Why is underscore used? see PEP 8 (https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles)

        self.__kind = kind
        self.name = name
        self.legs = legs

    def hello(self):
        print('My name is {}.\nI am {}.'.format(self.name, self.__kind))

    ## see decoractor (https://www.python.org/dev/peps/pep-0318/)
    ## see classmethod (https://docs.python.org/3/library/functions.html#classmethod)
    
    @classmethod
    def run(cls):
        print('no defined action')

