#!/usr/bin/env python3

from datetime import datetime


if __name__ == '__main__':
    # current time in local
    t = datetime.now()
    print('Current time')
    print(t.timetuple())

    print('\nFormat time string')
    print(t.strftime('%a %b %d, %Y'))
