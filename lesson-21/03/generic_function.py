#!/usr/bin/env python3

from dataclasses import dataclass
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
# Generic Function
#############################
T = TypeVar('T', bound=Animal)

# A generic function is one in which the types of the arguments and the return value have a defined relationship.
def sort_by_legs(*animals: T) -> list[T]:
    return sorted(animals, key=lambda animal: animal.legs)


#############################
# Main
#############################
if __name__ == '__main__':
    dog = Dog(kind='Shiba', name='Maru')
    bird = Bird(kind='Parrot', name='Polly')

    print(sort_by_legs(dog, bird))
