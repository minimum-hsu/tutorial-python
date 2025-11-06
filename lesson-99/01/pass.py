#!/usr/bin/env python3

# Refer to https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement

def foo():
    pass

class MyException(Exception):
    pass

if __name__ == '__main__':
    foo()
    raise MyException("This is a custom exception.")