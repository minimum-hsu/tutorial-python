#!/usr/bin/env python3

name = 'Alice'
count = len(name)


if count is 5:  ## same as "count == 5"
    print('[1] size of', name, 'is 5')
else:
    print('[1] size of', name, 'is not 5')


if count < 3:
    print('[3] size of', name, 'is less than 3')
elif count > 6:
    print('[3] size of', name, 'is greater than 6')
else:
    print('[3] size of', name, 'is between 3 and 6')


if 3 < count < 6:
    print('[2] size of', name, 'is between 3 and 6')
else:
    print('[2] size of', name, 'is not between 3 and 6')
