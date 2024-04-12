
number = int(input("Enter any number: "))

def number_range(number):
    if number < 0:
        return f'The number {number} is less than 0.'
    elif 0 <= number <= 50:
        return f'The number {number} is between 0 and 50.'
    elif 51 <= number <= 100:
        return f'The number {number} is between 51 and 100.'
    else:
        return f'The number {number} is greater than 100.'

print(number_range(number))
