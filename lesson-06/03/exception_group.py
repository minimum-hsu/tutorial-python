#!/usr/bin/env python3

def throw_exception():
    exceptions = []
    names = ['Alice', 'Bob', 'Charlie']

    for i in range(6):
        try:
            print(names[i])
        except IndexError as e:
            exceptions.append(e)

    if exceptions:
        raise ExceptionGroup("Multiple exceptions occurred", exceptions)

if __name__ == '__main__':
    try:
        throw_exception()
    except ExceptionGroup as eg:
        for i, exc in enumerate(eg.exceptions, 1):
            print(f'[Error {i}]', exc)
