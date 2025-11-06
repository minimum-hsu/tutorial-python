#!/usr/bin/env python3

class MyClass:
    def __init__(self):
        self._internal_value = 42  # Internal attribute

    @property
    def value(self):
        '''Public property to access the internal value.'''
        return self._internal_value

if __name__ == '__main__':
    obj = MyClass()
    print("Accessing internal value via property:", obj.value)
