# Write a function that computes the difference between the square of the sum of the first count positive integers and the sum of the squares of the first count positive integers.

def sum_square_difference(number):
    return sum(range(1, number + 1)) ** 2 - sum(x ** 2 for x in range(1, number + 1))

print(sum_square_difference(3))      # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
print(sum_square_difference(10))     # 2640
print(sum_square_difference(1))      # 0
print(sum_square_difference(100))    # 25164150
print(sum_square_difference(1000))   # 250166416500
print(sum_square_difference(10000))  # 2500166641665000