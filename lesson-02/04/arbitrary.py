#!/usr/bin/env python3

# Function that accepts arbitrary number of positional arguments
def print_multiply(*args):
    result = 1
    for num in args:
        result *= num
    print(result)

# Function that accepts arbitrary number of keyword arguments
def print_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Function that accepts arbitrary number of positional arguments and keyword arguments
def combined_example(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

if __name__ == '__main__':
    # Refer to https://docs.python.org/3/glossary.html#term-parameter

    # Using arbitrary positional arguments
    print_multiply(1, 2, 3)  # Output: 6

    # Using arbitrary keyword arguments
    print_args(name='Alice', age=30, city='New York')
    # Output:
    # name: Alice
    # age: 30
    # city: New York

    # Using both arbitrary positional and keyword arguments
    combined_example(1, 2, 3, name='Bob', age=25)
    # Output:
    # Positional arguments: (1, 2, 3)
    # Keyword arguments: {'name': 'Bob', 'age': 25}
