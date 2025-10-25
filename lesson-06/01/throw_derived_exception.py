#!/usr/bin/env python3

class CustomException(Exception):
    pass

def throw_exception():
    raise CustomException('Custom exception')

if __name__ == '__main__':
    throw_exception()
    # This will raise:
    # CustomException: Custom exception
