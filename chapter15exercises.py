class Date:
    """Represents a date"""

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        s = f'{self.year:02d}-{self.month:02d}-{self.day:02d}'
        return s
    def to_tuple(date):
        date = (f'{date.year}', f'{date.month}', f'{date.day}')
        return date
    def is_after(date1, date2): # I dont know why the professor had all of the other methods, but mine looks pretty similar.
        return Date.to_tuple(date1) > Date.to_tuple(date2)

date1 = Date(1933, 6, 22)
date2 = Date(1933, 9, 17)
print(date1, date2)
print(Date.is_after(date1, date2))
