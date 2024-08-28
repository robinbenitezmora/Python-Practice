'''
Prime Number is a number that is greater than 1 and divided by 1 or itself only.
Write a program that asks the user to input a number and then displays whether the number is a prime number or not.
'''

import math, sys

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            return False
    return True

def main():
    print('Prime Number Checker')
    print('Enter a number to check if it is a prime number')
    number = input()
    if number.isdigit():
        number = int(number)
        if is_prime(number):
            print(f'{number} is a prime number')
        else:
            print(f'{number} is not a prime number')
    else:
        print('Invalid input. Please enter a valid number')

if __name__ == '__main__':
    main()