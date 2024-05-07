# Write a function that takes a positive integer as an argument and returns that number with its digits reversed.

def reverse_number(num):
    number = str(num)
    for i in range(len(number) - 1, -1, -1):
        if number[i] == '0':
            new_number = number[:i]
        else:
            new_number = number[:i + 1]
            break
    return int(new_number[::-1])

print(reverse_number(12345))    # 54321
print(reverse_number(12213))    # 31221
print(reverse_number(456))      # 654
print(reverse_number(12000))    # 21 # Note that leading zeros in the result get dropped!
print(reverse_number(1))        # 1   
