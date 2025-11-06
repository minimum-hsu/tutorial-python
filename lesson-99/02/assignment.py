#!/usr/bin/env python3

# Refer to https://docs.python.org/3/reference/expressions.html#assignment-expressions

def get_first_element(array: list) -> str:
    '''Return the first element of the list.'''
    if not array:
        return 'The list is empty.'
    return array[0]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    if first := get_first_element(sample_list):
        print(f'The first element is: {first}')
