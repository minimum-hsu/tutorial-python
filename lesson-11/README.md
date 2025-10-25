# Lesson 11 - Date and Time Handling

This lesson covers comprehensive date and time operations in Python, from basic datetime usage to advanced parsing with external libraries.

## Learning Objectives

- Master Python's datetime module
- Understand timezone handling and UTC conversion
- Learn date/time formatting and parsing
- Perform date arithmetic with timedelta
- Use advanced parsing with python-dateutil
- Understand ISO 8601 and Unix timestamps
- Master timezone-aware programming

## Course Content

### 01. Basic DateTime Operations
**File:** `01/main.py`

Learn fundamental datetime operations and different time representations:

```python
#!/usr/bin/env python3

from datetime import datetime
from datetime import timezone

if __name__ == '__main__':
    # current time in local
    t = datetime.now()
    print('Local time')
    print(t.timetuple())
    print(t)

    # current time in UTC
    utc = datetime.now(timezone.utc)
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
```

**Key Concepts:**
- `datetime.now()` for local current time
- `datetime.now(timezone.utc)` for UTC time
- `timetuple()` returns time.struct_time object
- `isoformat()` for ISO 8601 standard formatting
- `timestamp()` for Unix epoch time conversion
- Timezone-aware vs naive datetime objects

### 02. Time String Parsing and Timezone Conversion
**File:** `02/main.py`

Learn to parse time strings and handle timezone conversions:

```python
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
```

**Key Concepts:**
- `datetime.strptime()` for parsing formatted time strings
- Format codes: `%Y`, `%m`, `%d`, `%H`, `%M`, `%S`, `%z`
- `astimezone()` for timezone conversion
- `utctimetuple()` for UTC time tuple
- Timezone offset parsing (`+0200`)

### 03. Date Arithmetic with Timedelta
**File:** `03/main.py`

Learn date arithmetic using timedelta for calculations:

```python
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
```

**Key Concepts:**
- `timedelta` for representing time differences
- Date arithmetic with `+` and `-` operators
- Common timedelta parameters: `days`, `hours`, `minutes`, `seconds`
- Negative values for past dates
- Automatic date rollover (40 hours = 1 day + 16 hours)

### 04. Custom Date Formatting
**File:** `04/main.py`

Learn custom date formatting using strftime:

```python
#!/usr/bin/env python3

from datetime import datetime

if __name__ == '__main__':
    # current time in local
    t = datetime.now()
    print('Current time')
    print(t.timetuple())

    print('\nFormat time string')
    print(t.strftime('%a %b %d, %Y'))
```

**Key Concepts:**
- `strftime()` for custom date formatting
- Format codes: `%a` (weekday short), `%b` (month short), `%d` (day), `%Y` (year)
- Human-readable date formats
- Localized formatting support

### 05. Advanced Parsing with python-dateutil
**Files:** `05/main.py`, `05/requirements.txt`

Learn flexible date parsing with the python-dateutil library:

**Requirements (`05/requirements.txt`)**
```pip-requirements
python-dateutil
```

**Application Code (`05/main.py`)**
```python
#!/usr/bin/env python3

from dateutil.parser import parse

if __name__ == '__main__':
    # parse time string
    print(parse('2017-01-23T12:30:40+02:00'))
    print(parse('2017-01-23 12:30 CST'))
```

**Key Concepts:**
- `dateutil.parser.parse()` for intelligent date parsing
- Automatic format detection
- Support for various date formats
- Timezone abbreviations (CST, EST, etc.)
- ISO 8601 format support
- Flexible parsing without explicit format strings

## DateTime Components Deep Dive

### Date and Time Creation
```python
from datetime import datetime, date, time

# Specific date and time
dt = datetime(2023, 12, 25, 14, 30, 0)  # Christmas 2023, 2:30 PM

# Date only
d = date(2023, 12, 25)

# Time only
t = time(14, 30, 0)

# Combine date and time
dt = datetime.combine(d, t)
```

### Timezone Handling
```python
from datetime import datetime, timezone, timedelta

# Create timezone-aware datetime
utc = timezone.utc
eastern = timezone(timedelta(hours=-5))  # EST

dt_utc = datetime.now(utc)
dt_eastern = datetime.now(eastern)

# Convert between timezones
dt_converted = dt_utc.astimezone(eastern)
```

### Common Format Codes
| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | 4-digit year | 2023 |
| `%y` | 2-digit year | 23 |
| `%m` | Month (01-12) | 12 |
| `%B` | Full month name | December |
| `%b` | Short month name | Dec |
| `%d` | Day of month (01-31) | 25 |
| `%A` | Full weekday name | Monday |
| `%a` | Short weekday name | Mon |
| `%H` | Hour (00-23) | 14 |
| `%I` | Hour (01-12) | 02 |
| `%M` | Minute (00-59) | 30 |
| `%S` | Second (00-59) | 45 |
| `%p` | AM/PM | PM |
| `%z` | Timezone offset | +0200 |
| `%Z` | Timezone name | EST |

## Practical Examples

### Date Range Generation
```python
from datetime import datetime, timedelta

def date_range(start_date, end_date):
    current = start_date
    while current <= end_date:
        yield current
        current += timedelta(days=1)

# Usage
start = datetime(2023, 1, 1)
end = datetime(2023, 1, 7)
for date in date_range(start, end):
    print(date.strftime('%Y-%m-%d'))
```

### Age Calculation
```python
from datetime import datetime, date

def calculate_age(birth_date):
    today = date.today()
    return today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )

# Usage
birth = date(1990, 5, 15)
age = calculate_age(birth)
print(f"Age: {age} years")
```

### Working Days Calculator
```python
from datetime import datetime, timedelta

def working_days(start_date, end_date):
    current = start_date
    count = 0
    while current <= end_date:
        if current.weekday() < 5:  # Monday = 0, Sunday = 6
            count += 1
        current += timedelta(days=1)
    return count

# Usage
start = datetime(2023, 1, 1)
end = datetime(2023, 1, 31)
print(f"Working days in January 2023: {working_days(start, end)}")
```

### Time Zone Converter
```python
from datetime import datetime, timezone, timedelta

def convert_timezone(dt, from_tz, to_tz):
    """Convert datetime from one timezone to another"""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=from_tz)
    return dt.astimezone(to_tz)

# Usage
utc = timezone.utc
eastern = timezone(timedelta(hours=-5))
pacific = timezone(timedelta(hours=-8))

dt_utc = datetime(2023, 12, 25, 12, 0, 0, tzinfo=utc)
dt_eastern = convert_timezone(dt_utc, utc, eastern)
dt_pacific = convert_timezone(dt_utc, utc, pacific)

print(f"UTC: {dt_utc}")
print(f"Eastern: {dt_eastern}")
print(f"Pacific: {dt_pacific}")
```

## How to Run

Each example can be executed directly:

```bash
# Navigate to corresponding directory
cd lesson-11/01
python3 main.py
```

```bash
cd lesson-11/02
python3 main.py
```

```bash
cd lesson-11/03
python3 main.py
```

```bash
cd lesson-11/04
python3 main.py
```

```bash
cd ../05
pip install -r requirements.txt
python3 main.py
```

## Best Practices

### 1. **Always Use Timezone-Aware Datetimes**
```python
# Good: Timezone-aware
from datetime import datetime, timezone
dt = datetime.now(timezone.utc)

# Avoid: Naive datetime for production
dt = datetime.now()  # No timezone info
```

### 2. **Use UTC for Storage and Calculations**
```python
# Good: Store in UTC, display in local
import datetime
utc_time = datetime.datetime.now(datetime.timezone.utc)
local_time = utc_time.astimezone()

# Good: Always work in UTC for calculations
def time_difference(start_utc, end_utc):
    return end_utc - start_utc
```

### 3. **Validate Date Inputs**
```python
# Good: Handle invalid dates
def safe_date_parse(date_string, format_string):
    try:
        return datetime.strptime(date_string, format_string)
    except ValueError as e:
        print(f"Invalid date format: {e}")
        return None

# Good: Validate date ranges
def validate_date_range(start, end):
    if start > end:
        raise ValueError("Start date must be before end date")
```

### 4. **Use dateutil for Flexible Parsing**
```python
# Good: Handle various formats automatically
from dateutil.parser import parse
dates = [
    '2023-12-25',
    '25/12/2023',
    'December 25, 2023',
    '2023-12-25T14:30:00+02:00'
]
for date_str in dates:
    dt = parse(date_str)
    print(f"{date_str} -> {dt}")
```

### 5. **Handle Daylight Saving Time**
```python
# Good: Use pytz for complex timezone handling
import pytz
from datetime import datetime

eastern = pytz.timezone('US/Eastern')
dt = eastern.localize(datetime(2023, 3, 12, 2, 30))  # DST transition
dt_utc = dt.astimezone(pytz.UTC)
```

## Common Datetime Operations

### String to DateTime Conversion
```python
# Basic parsing
dt = datetime.strptime('2023-12-25 14:30:00', '%Y-%m-%d %H:%M:%S')

# ISO format parsing
dt = datetime.fromisoformat('2023-12-25T14:30:00+02:00')

# Flexible parsing with dateutil
from dateutil.parser import parse
dt = parse('Dec 25, 2023 2:30 PM')
```

### DateTime to String Conversion
```python
dt = datetime.now()

# Standard formats
iso_format = dt.isoformat()
readable = dt.strftime('%B %d, %Y at %I:%M %p')
compact = dt.strftime('%Y%m%d_%H%M%S')

# Custom formats
custom = dt.strftime('%a, %b %d %Y')
```

### Time Calculations
```python
from datetime import datetime, timedelta

# Add/subtract time
future = datetime.now() + timedelta(days=30, hours=2)
past = datetime.now() - timedelta(weeks=2)

# Calculate differences
diff = future - past
days = diff.days
seconds = diff.seconds
total_seconds = diff.total_seconds()
```

## Advanced Topics

### Custom DateTime Classes
```python
from datetime import datetime

class BusinessDateTime(datetime):
    def is_business_day(self):
        return self.weekday() < 5

    def next_business_day(self):
        next_day = self + timedelta(days=1)
        while not next_day.is_business_day():
            next_day += timedelta(days=1)
        return next_day
```

### Performance Considerations
```python
# For many datetime operations, consider using pandas
import pandas as pd

# Fast datetime operations on series
dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
business_days = dates[dates.dayofweek < 5]

# Timezone conversions
utc_dates = dates.tz_localize('UTC')
local_dates = utc_dates.tz_convert('US/Eastern')
```

## Practice Suggestions

1. **Build a Meeting Scheduler**: Handle different timezones and business hours
2. **Create a Date Calculator**: Calculate ages, anniversaries, time until events
3. **Log File Analyzer**: Parse timestamps from log files and analyze patterns
4. **Event Reminder System**: Calculate time until events and send notifications
5. **Working Hours Calculator**: Compute billable hours excluding weekends/holidays
6. **Time Series Data Handler**: Process time-stamped data with proper timezone handling

## Common Pitfalls

- **Mixing naive and timezone-aware datetimes**: Always be consistent
- **Ignoring daylight saving time**: Use proper timezone libraries
- **Hardcoding timezone offsets**: Use named timezones instead
- **Not validating date inputs**: Always handle parsing errors
- **Using local time for stored data**: Store in UTC, display in local time
- **Assuming 24-hour days**: Account for DST transitions
- **Not handling leap years**: Use proper date arithmetic

## Related Resources

- [Python datetime Documentation](https://docs.python.org/3/library/datetime.html)
- [dateutil Documentation](https://dateutil.readthedocs.io/)
- [pytz Documentation](https://pytz.sourceforge.net/)
- [ISO 8601 Standard](https://en.wikipedia.org/wiki/ISO_8601)
- [Time Zone Database](https://www.iana.org/time-zones)
- [Pandas DateTime](https://pandas.pydata.org/docs/user_guide/timeseries.html)