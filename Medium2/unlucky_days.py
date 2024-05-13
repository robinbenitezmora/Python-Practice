'''Some people believe that Fridays that fall on the 13th day of the month are unlucky days. Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year. You may assume that the year is greater than 1752, which is when the United Kingdom adopted the modern Gregorian Calendar. You may also assume that the same calendar will remain in use for the foreseeable future.'''

def friday_the_13ths(year):
    import datetime
    count = 0
    for month in range(1, 13):
        if datetime.datetime(year, month, 13).weekday() == 4:
            count += 1
    return count

print(friday_the_13ths(1986))      # 1
print(friday_the_13ths(2015))      # 3
print(friday_the_13ths(2017))      # 2
print(friday_the_13ths(2018))      # 1
print(friday_the_13ths(2019))      # 2
print(friday_the_13ths(2020))      # 2
print(friday_the_13ths(2021))      # 1
print(friday_the_13ths(2022))      # 2
print(friday_the_13ths(2023))      # 1
print(friday_the_13ths(2024))      # 2
