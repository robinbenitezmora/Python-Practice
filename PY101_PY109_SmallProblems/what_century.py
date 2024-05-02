'''Write a function that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.'''

def century(year):
    century = year // 100
    century += 1 if year % 100 > 0 else 0
    return str(century) + 'th' if century % 100 in (11, 12, 13) else str(century) + {1: 'st', 2: 'nd', 3: 'rd'}.get(century % 10, 'th')

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True