#!/usr/bin/env python3

from datetime import datetime


if __name__ == '__main__':
    # parse time string
    time_string = '2017/01/23 12:30:40+0200'
    print('Time string is {}'.format(time_string))
    original_time = datetime.strptime(time_string, '%Y/%m/%d %H:%M:%S%z')

    # convert to local timezone
    t = original_time.astimezone()
    print('Local timezone')
    print(t.timetuple())
    print('UTC time')
    print(t.utctimetuple())
