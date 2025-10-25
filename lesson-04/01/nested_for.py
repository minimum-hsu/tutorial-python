#!/usr/bin/env python3

def multiplication_table():
    for multiplicand in range(1, 10):
        for multiplier in range(1, 10):
            print(multiplicand, 'x', multiplier, '=', multiplicand * multiplier)

if __name__ == '__main__':
    multiplication_table()
