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

year = age
month = year * 12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

for i in range(begin_year, end_year):
    if judge_leap_year(i):
        day += 366
    else:
        day += 365

leap_year = judge_leap_year(localtime.tm_year)
for i in range(1, localtime.tm_mon):
    day += month_days(i, leap_year)

day += localtime.tm_mday

print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))
