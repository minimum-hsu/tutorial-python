#!/usr/bin/env python3

# see Format Specification Mini-Language (https://docs.python.org/3.6/library/string.html#format-specification-mini-language)

print('Fill space to format output: {:>10s}'.format('hello'))

print('Fill zeros to format output: {:04d}'.format(12))

print('{} have {} dollars'.format('I', 12))

print('{user} has {money} dollars'.format(user='Alice', money=12))

print('Reorder output: {0}. {2}, {1}'.format('Alice', 'Bob', 'Charlie'))
