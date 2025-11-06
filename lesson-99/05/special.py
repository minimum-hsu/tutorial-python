#!/usr/bin/env python3

# Refer to https://docs.python.org/3/reference/datamodel.html#specialnames

def foo():
    '''function docstring'''
    pass

class Bar:
    '''sequence-like class'''

    def __init__(self):
        self.value = [0, 1, 2]

    def __getitem__(self, index):
        return self.value[index]

    def __len__(self):
        return len(self.value)

if __name__ == '__main__':
    print("Function foo docstring:", foo.__doc__)
    print("Function foo name:", foo.__name__)

    bar = Bar()
    print("Bar length:", len(bar))
    print("Bar items:", [bar[i] for i in bar])
