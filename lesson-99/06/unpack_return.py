#!/usr/bin/env python3

def get_array() -> list[str]:
    '''Return a sample array of strings.'''
    return ['apple', 'banana', 'orange', 'banana', 'grape']

if __name__ == '__main__':
    first, *middle, last = get_array()
    print("First element:", first)
    print("Middle elements:", middle)
    print("Last element:", last)

    first, second, *rest = get_array()
    print("First element:", first)
    print("Second element:", second)
    print("Rest of the elements:", rest)

    *_, last = get_array()
    print("Last element only:", last)