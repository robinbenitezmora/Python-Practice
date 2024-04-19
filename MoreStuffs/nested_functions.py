
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def square(x):
    return x * x

def sum_of_squares(a, b):
    def square(x):
        return x * x
    return square(a) + square(b)

print("The sum of the squares of the two numbers is: ", sum_of_squares(num1, num2))