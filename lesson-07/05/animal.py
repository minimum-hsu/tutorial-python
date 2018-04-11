#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, kind: str, name: str, legs: int):
        '''
        The first step when creating a new object
        '''

        self.__kind = kind
        self.name = name
        self.legs = legs

    def hello(self):
        print('My name is {}. I am {}.'.format(self.name, self.__kind))

    @abstractmethod
    def run(self):
        pass

