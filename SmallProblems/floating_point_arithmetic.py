
# Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

num1 = float(input("Enter a positive number:\n"))
num2 = float(input("Enter another positive number:\n"))

def operations(num1, num2):
    print(f'{num1} + {num2} = {num1 + num2}')
    print(f'{num1} - {num2} = {num1 - num2}')
    print(f'{num1} * {num2} = {num1 * num2}')
    print(f'{num1} / {num2} = {num1 / num2}')
    print(f'{num1} // {num2} = {num1 // num2}')
    print(f'{num1} % {num2} = {num1 % num2}')
    print(f'{num1} ** {num2} = {num1 ** num2}')

operations(num1, num2)