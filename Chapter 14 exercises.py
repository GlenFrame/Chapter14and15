import copy


class Time:
    """Represents a time of day."""

class Date:
    """Represents a year, month, and day"""

def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time

def print_time(time):
    s = f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}'
    print(s)


def increment_time(time, hours, minutes, seconds):
    time.hour += hours
    time.minute += minutes
    time.second += seconds

    carry, time.second = divmod(time.second, 60)
    carry, time.minute = divmod(time.minute + carry, 60)
    carry, time.hour = divmod(time.hour + carry, 60)

def add_time(time, hours, minutes, seconds):
    total = copy(time)
    increment_time(total, hours, minutes, seconds)
    return total



time1 = make_time(5, 1, 2)
time2 = make_time(5, 0, 59)

def subtract_time(t1, t2): # theyre not even comparable, mine needs to be shortened and made way more efficient and concise.
    """ Returns the time interval between two times in seconds (only works in 24-hour format)"""
    hour = abs(t1.hour - t2.hour)
    minute = abs(t1.minute - t2.minute)
    second = abs(t1.second - t2. second)
    if t1.hour >= 24 or t1.minute >= 60 or t1.second >= 60 or t2.hour >= 24 or t2.minute >= 60 or t2.second >= 60:
        return "Time Format Invalid"
    if hour >= 1:
        minute += hour * 60
    if minute >= 1:
        second += minute * 60
    return second


def is_after(t1, t2): # mine is much longer and much less efficient
    """Checks whether `t1` is after `t2`.

    >>> is_after(make_time(3, 2, 1), make_time(3, 2, 0))
    True
    >>> is_after(make_time(3, 2, 1), make_time(3, 2, 1))
    False
    >>> is_after(make_time(11, 12, 0), make_time(9, 40, 0))
    True
    """
    base_time = make_time(0,0,0)
    time1_seconds = subtract_time(base_time, t1)
    time2_seconds = subtract_time(base_time, t2)
    return time1_seconds > time2_seconds

def make_date(year, month, day):
    date = Date()
    date.year = year
    date.month = month
    date.day = day
    return date

def print_date(date):
    d = f"{date.year:02d}-{date.month:02d}-{date.day:02d}"
    print(d)

def date_after(date1, date2):
    if date1.year > date2.year:
        return True
    elif date1.year == date2.year:
        if date1.month > date2.month:
            return True
        elif date1.month == date2.month:
            return date1.day > date2.day
        else: return False
    else: return False


day1 = make_date(1933, 6, 22)
day2 = make_date(1933, 9, 17)

print(date_after(day1, day2))

print_date(day1)

print(is_after(time1, time2))

print(subtract_time(time1, time2))

# My versions are so much longer and more noodly
