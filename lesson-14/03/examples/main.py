#!/usr/bin/env python3

from animal.mammalia import Dog

if __name__ == '__main__':
    puppy = Dog(kind='Shiba', name='Maru')
    puppy.hello()
    puppy.run()
