#!/usr/bin/env python3

from datetime import datetime
from datetime import timedelta

if __name__ == '__main__':
    # current time in local
    t = datetime.now()
    print('Current time')
    print(t.timetuple())

    print('\n2 days ago')
    t_2_day_ago = t + timedelta(days = -2)
    print(t_2_day_ago.timetuple())

    print('\n40 hours later')
    t_40_hour_later = t + timedelta(hours = 40)
    print(t_40_hour_later.timetuple())
