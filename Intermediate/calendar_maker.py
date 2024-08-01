'''
Calendar Maker (Intermediate)
This is a simple calendar maker program. It takes a year and the day of the week that year starts on as input and prints out a calendar for that year. The calendar should start with the month of January and end with December. The output should be formatted as follows:

January
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21

February
Su Mo Tu We Th Fr Sa
          1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28

March
Su Mo Tu We Th Fr Sa
          1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31

...

December
Su Mo Tu We Th Fr Sa
             1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
The program should take two command line arguments: the year and the day of the week that year starts on. The day of the week should be a number from 0 to 6, where 0 is Sunday, 1 is Monday, and so on. The program should print out the calendar for that year, starting with the month of January and ending with December. The program should print out the calendar in the format shown above, with each month starting on a new line.

The program should handle leap years correctly. A leap year is any year that is divisible by 4, except for years that are divisible by 100 but not by 400. For example, 2000 and 2400 are leap years, but 1800, 1900, 2100, 2200, 2300, and 2500 are not.

The program should not use the calendar module or any other date/time libraries. The program should work for any year from 1900 to 9999.

The program should print out the calendar for the year 2020 that starts on a Wednesday like this:

$ python calendar_maker.py 2020 3
January
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

February
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29

March
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

...

December
Su Mo Tu We Th Fr Sa
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
'''

import datetime

DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

while True:
    print('Enter the year:')
    year = input('> ')
    if year.isdigit() and 1900 <= int(year) <= 9999:
        year = int(year)
        break
    print('Please enter a year between 1900 and 9999.')

while True:
    print('Enter the day of the week that year starts on (0-6):')
    dayOfWeek = input('> ')
    if dayOfWeek.isdigit() and 0 <= int(dayOfWeek) <= 6:
        dayOfWeek = int(dayOfWeek)
        break
    print('Please enter a number between 0 and 6.')

for month in range(1, 13):
    print()
    print(MONTHS[month - 1])
    print('Su Mo Tu We Th Fr Sa')

    # Get the number of days in the month
    if month in (1, 3, 5, 7, 8, 10, 12):
        daysInMonth = 31
    elif month in (4, 6, 9, 11):
        daysInMonth = 30
    else:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            daysInMonth = 29
        else:
            daysInMonth = 28

    # Print the days of the month
    for day in range(1, daysInMonth + 1):
        if day == 1:
            print('   ' * dayOfWeek, end='')
        print('{:2}'.format(day), end=' ')
        if (day + dayOfWeek) % 7 == 0:
            print()
    print()

# # What is the output of the following code?
# # A) The code will run a Caesar cipher decryption program that tries all possible keys to decrypt the message. It will print out all possible decryptions of the message for each key.
# # The original message could be any of the above, or none of them.
                                                                                            