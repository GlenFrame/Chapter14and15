class Time:
    """Represents a time of day."""
lunch = Time()
lunch.hour = 11
lunch.minute = 59
lunch.second = 1
print(lunch.hour)
def print_time(time):
    s = f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}'
    print(s)
print_time(lunch)

def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time

class Strawberries:
    def __init__(self, variety, taste, date):
        self.variety = variety
        self.taste = taste
        self.date = date
stbry1 = Strawberries('alba', 'sweet & tangy', '6/27/25')
stbry2 = Strawberries('alexandria', 'sweet, but slightly bitter', '7/2/25')

print(f'The {stbry1.variety} strawberry was {stbry1.taste}, and the {stbry2.variety} strawberry was {stbry2.taste}')

time = make_time(11, 59, 1)
print_time(time)