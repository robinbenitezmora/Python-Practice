'''In the previous exercise, you developed a function that converts non-negative numbers to strings. In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.

Write a function that takes an integer and converts it to a string representation.

You may not use any of the standard conversion functions available in Python, such as str. You may, however, use integer_to_string from the previous exercise.'''

import number_to_string

def signed_integer_to_string(num):
    if num == 0:
        return '0'
    elif num > 0:
        return '+' + number_to_string.integer_to_string(num)
    else:
        return '-' + number_to_string.integer_to_string(-num)

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True