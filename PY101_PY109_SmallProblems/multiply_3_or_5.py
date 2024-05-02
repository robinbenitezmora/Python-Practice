
def multiply_3_or_5(num):
    sum = 0
    for i in range(1, num + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# These examples should all print True
print(multiply_3_or_5(3) == 3)
print(multiply_3_or_5(5) == 8)
print(multiply_3_or_5(10) == 33)
print(multiply_3_or_5(1000) == 234168)   

