#!/usr/bin/env python3

from datetime import datetime
import time
import sys

assert sys.version_info >= (3, 6)


if __name__ == '__main__':
    # current time in local
    t = datetime.now()
    print('Local time')
    print(t.timetuple())
    print(t)

    # current time in UTC
    utc = datetime.utcnow()
    print('\nUTC time')
    print(utc.timetuple())  # same as t.utctimetuple()
    print(utc)

    # ISO 8601
    print('\nISO 8601')
    print(t.isoformat(timespec='seconds'))
    print(t.isoformat(timespec='milliseconds'))

    # unix time (epoch time)
    print('\nUnix time')
    print(t.timestamp())
