from typing import override
from animal.base import Animal

class Dog(Animal):
    def __init__(self, kind: str, name: str):
        super().__init__(kind, name, 4)

    @override
    def run(self):
        print('I can run by {} legs'.format(self.legs))
