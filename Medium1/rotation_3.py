'''Take the number 735291 and rotate it by one digit to the left, getting 352917. Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. Keep the first two digits fixed in place and rotate again to get 321759. Keep the first three digits fixed in place and rotate again to get 321597. Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer. You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.'''

def rotate_rightmost_digits(number, count):
    number_str = str(number)
    if count == 1:
        return number
    return int(number_str[:-count] + number_str[-count+1:] + number_str[-count])

def max_rotation(number):
    number_str = str(number)
    for i in range(len(number_str)):
        number = rotate_rightmost_digits(number, len(number_str) - i)
    return number

print(max_rotation(735291))         # 321579
print(max_rotation(3))              # 3
print(max_rotation(35))             # 53
print(max_rotation(105))            # 15 (the leading zero gets dropped)
print(max_rotation(8703529146))     # 7321609845