#!/usr/bin/env python3

def double(number: int):
    return number * 2

if __name__ == '__main__':
    array = range(0, 5)
    doubled = [double(number) for number in array] # List comprehension
    print(doubled) # Output: [0, 2, 4, 6, 8]

    even = [number for number in array if number % 2 == 0] # List comprehension with condition
    print(even) # Output: [0, 2, 4]