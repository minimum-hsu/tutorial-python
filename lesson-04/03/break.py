#!/usr/bin/env python3

from random import randint

match = [1, 3]

while True:  # be careful, this loop is always run until break
    number = randint(0, 10)

    if number in match:
        print(number, 'is matched')
        break
    else:
        print(number, 'is not matched')
