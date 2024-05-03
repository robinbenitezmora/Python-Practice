

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