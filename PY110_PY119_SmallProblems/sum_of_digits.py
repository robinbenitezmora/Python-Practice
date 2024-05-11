# Write a function that takes one argument, a positive integer, and returns the sum of its digits.

def sum_digits(num):
    return sum([int(digit) for digit in str(num)])

print(sum_digits(23))           # 5
print(sum_digits(496))          # 19
print(sum_digits(123456789))    # 45
print(sum_digits(0))            # 0
print(sum_digits(123))          # 6
print(sum_digits(1))            # 1
print(sum_digits(100))          # 1
print(sum_digits(999999999999)) # 99
print(sum_digits(1234567890))   # 45