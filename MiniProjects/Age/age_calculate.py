import time
from calendar import isleap

def judge_leap_year(year):
    if isleap(year):
        return True
    return False

def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if leap_year:
            return 29
        return 28
        
name = input('Write your name:\n')
age = int(input('Write your age:\n'))
localtime = time.localtime(time.time())

year = localtime.tm_year - age
month = localtime.tm_mon
day = localtime.tm_mday

leap_year = judge_leap_year(year)
days = 0
for i in range(1, month):
    days += month_days(i, leap_year)
days += day
print(f'{name}, you were born on the {days} day of the year {year}.')
