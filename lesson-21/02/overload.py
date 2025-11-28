#!/usr/bin/env python3

from dataclasses import dataclass
from typing import overload

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
# Function Overloading
#############################
@overload
def hello(animal: Dog) -> str:
    ...

@overload
def hello(animal: Bird) -> str:
    ...

def hello(animal: Dog | Bird) -> str:
    if isinstance(animal, Dog):
        return 'My name is {}. I am {}, which is a breed of dog'.format(animal.name, animal.kind)
    elif isinstance(animal, Bird):
        return 'My name is {}. I am {}, which is a species of bird'.format(animal.name, animal.kind)
    else:
        raise TypeError('Unsupported type')


#############################
# Main
#############################
if __name__ == '__main__':
    dog = Dog(kind='Shiba', name='Maru')
    bird = Bird(kind='Parrot', name='Polly')

    print(hello(dog))
    print(hello(bird))
