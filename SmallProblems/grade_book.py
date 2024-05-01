''' Write a function that determines the mean (average) of the three scores passed to it, and returns the letter associated with that grade.

90 <= score <= 100: 'A'
80 <= score < 90: 'B'
70 <= score < 80: 'C'
60 <= score < 70: 'D'
0 <= score < 60: 'F'
Tested values are all between 0 and 100. There is no need to check for negative values or values greater than 100.'''


grade = int(input("Enter a grade: "))

def get_grade(grade):
    if 90 <= grade <= 100:
        return f'You have got an A'
    elif 80 <= grade <= 89:
        return f'You have got a B'
    elif 70 <= grade <= 79:
        return f'You have got a C'
    elif 60 <= grade <= 69:
        return f'You have got a D'
    elif 0 <= grade <= 59:
        return f'You have got an F'
    else:
        return f'Invalid grade'

print(get_grade(grade))
