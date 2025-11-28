#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Generic
from typing import TypeVar


#############################
# Classes
#############################
@dataclass
class Animal:
    kind: str
    name: str
    legs: int


@dataclass
class Dog(Animal):
    legs: int = 4


@dataclass
class Bird(Animal):
    legs: int = 2


#############################
# Generic Class
#############################
T = TypeVar('T', bound=Animal)


class AnimalHandler(Generic[T]):

    def hello(self, animal: T):
        if isinstance(animal, Dog):
            return 'My name is {}. I am {}, which is a breed of dog'.format(animal.name, animal.kind)
        elif isinstance(animal, Bird):
            return 'My name is {}. I am {}, which is a species of bird'.format(animal.name, animal.kind)
        else:
            raise TypeError('Unsupported type')

    def sort_by_legs(self, *animals: T) -> list[T]:
        return sorted(animals, key=lambda animal: animal.legs)


#############################
# Main
#############################
if __name__ == '__main__':
    dog = Dog(kind='Shiba', name='Maru')
    bird = Bird(kind='Parrot', name='Polly')
    handler = AnimalHandler[Animal]()

    print(handler.hello(dog))
    print(handler.hello(bird))
    print(handler.sort_by_legs(dog, bird))