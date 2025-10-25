#!/usr/bin/env python3

def multiply(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Both arguments must be integers')

    return a * b

if __name__ == '__main__':
    result = multiply(6, 7)
    print(f'The result of multiplication is: {result}')
