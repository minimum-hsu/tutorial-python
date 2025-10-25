#!/usr/bin/env python3

def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers.

    Args:
        a (int): Multiplicand integer.
        b (int): Multiplier integer.

    Returns:
        int: The product of a and b.
    """

    return a * b

if __name__ == '__main__':
    result = multiply(3, 4)
    print(multiply.__doc__)
