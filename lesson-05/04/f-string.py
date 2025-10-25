#!/usr/bin/env python3

# see Formatted string literals (https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
# see PEP 498 (https://www.python.org/dev/peps/pep-0498/)

var = 'hello'
print(f'Fill space to format output: {var:>10}')

var = 12
print(f'Fill zeros to format output: {var+1:04}')

user = 'I'
money = 12
print(f'{user} have {money} dollars')

names = ['Alice', 'Bob', 'Charlie']
print(f'{names[0]} has {money} dollars')
