#!/usr/bin/env python3

from dateutil.parser import parse

if __name__ == '__main__':
    # parse time string
    print(parse('2017-01-23T12:30:40+02:00'))
    print(parse('2017-01-23 12:30 CST'))
