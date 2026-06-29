#!/usr/bin/env python3

function_double = lambda x: x * 2  # noqa: E731

function_multiply = lambda x, y: x * y  # noqa: E731

if __name__ == "__main__":
    print("function_double(5) =", function_double(5)) # Output: 10
    print("function_multiply(5, 3) =", function_multiply(5, 3)) # Output: 15
