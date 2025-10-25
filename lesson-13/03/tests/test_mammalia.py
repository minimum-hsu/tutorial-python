#!/usr/bin/env python3

from animal.mammalia import Dog

#############################
# Testcases
#############################
def test_dog():
    puppy = Dog(kind='Shiba', name='Maru')
    puppy.hello()
    puppy.run()
