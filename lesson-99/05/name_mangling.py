#!/usr/bin/env python3

# Refer to https://docs.python.org/3/reference/expressions.html#index-5

class Parent:
    def __init__(self):
        self.__private_attr = "I am private"

    def show(self):
        print("Private Attribute:", self.__private_attr)

class Child(Parent):
    def __init__(self):
        super().__init__()

    def print(self):
        try:
            print("Accessing Parent's private attribute:", self.__private_attr)
        except AttributeError as e:
            print("Error:", e)

if __name__ == '__main__':
    parent = Parent()
    parent.show()

    child = Child()
    child.show()
    child.print()
