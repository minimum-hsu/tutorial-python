#!/usr/bin/env python3

from typing import ClassVar
from typing import Self


class Animal():

    # Class variables
    _instance_cache: ClassVar[dict[tuple, Self]] = {}

    # Instance variables
    _initialized: bool

    def __new__(cls, kind: str, name: str) -> Self:
        cache_key = (cls, kind, name)

        if cache_key not in cls._instance_cache:
            obj = super().__new__(cls)
            obj._initialized = False
            cls._instance_cache[cache_key] = obj
            print(f"Creating a new {cls.__name__} instance.")
        else:
            print(f"{cls.__name__} instance already exists. Returning the cached instance.")

        return cls._instance_cache[cache_key]

    def __init__(self, kind: str, name: str, legs: int):
        if getattr(self, "_initialized", False):
            return

        self.__kind = kind
        self.name = name
        self.legs = legs

        print("Initializing the Animal part.")
        if type(self) is Animal:
            self._initialized = True

    def hello(self):
        print("My name is {}. I am {}.".format(self.name, self.__kind))

    def run(self):
        print("no defined action")

    @classmethod
    def _instance_cache_clear(cls):
        cls._instance_cache.clear()


class Dog(Animal):

    def __init__(self, kind: str, name: str):
        if getattr(self, "_initialized", False):
            return

        super().__init__(kind, name, 4)

        print("Initializing the Dog part.")
        self._initialized = True


if __name__ == "__main__":
    print("Creating the first Dog instance.")
    Dog(kind="Shiba", name="Maru")

    print("Creating the second Dog instance.")
    Dog(kind="Shiba", name="Maru")

    print("Creating the third Dog instance.")
    Dog(kind="Mix", name="Pochi")
