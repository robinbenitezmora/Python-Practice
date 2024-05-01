
# Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.

num = int(input("Enter a number:\n"))
string = input("Enter a string:\n")

def repeat_string(string, num):
    return f'{string}\n' * num

print(repeat_string(string, num))
