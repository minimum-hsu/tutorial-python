#!/usr/bin/env python3

# see printf-style String Formatting (https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)

print('Fill space to format output: %10s' % 'hello')

print('Fill zeros to format output: %04d' % 12)

print('Rounded output: %3.4f' % 3.14159)

print('%s have %d dollars' % ('I', 12))

print('%(user)s has %(money)d dollars' % {'user': 'Alice', 'money': 12})
