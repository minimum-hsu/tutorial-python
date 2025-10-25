#!/usr/bin/env python3

def action(value):
    # match-case statement introduced in Python 3.10
    # Refer to https://docs.python.org/3/tutorial/controlflow.html#match-statements
    match value:
        case 0:
            print('you get data from database')
        case 1:
            print('you delete data in database')
        case 2:
            print('you insert data to database')
        case _:
            print('unknown action')

if __name__ == '__main__':
    for i in range(4):  # simulate user choice
        action(i)
