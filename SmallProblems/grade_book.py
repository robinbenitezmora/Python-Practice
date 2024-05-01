


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
