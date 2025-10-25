#!/usr/bin/env python3

class Operation:

    def calculate(self, a: int | float, b: int| float) -> int | float:
        raise NotImplementedError("Subclasses must implement this method")

class Multiplication(Operation):

    def calculate(self, a: int | float, b: int | float) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")

        return a * b

class Division(Operation):

    def calculate(self, a: int | float, b: int | float) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")

        if b == 0:
            raise ValueError("The divisor cannot be zero")

        return a / b

if __name__ == '__main__':
    operation = Multiplication()
    result = operation.calculate(6, 7)
    print(f'The result of multiplication is: {result}')
