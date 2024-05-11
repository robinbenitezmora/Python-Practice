# We defined a function intending to multiply the sum of numbers by a factor. However, the function raises an error. Why? How would you fix this code?

def sum(numbers, factor):
    total = 0
    for number in numbers:
        total += number
    return factor * total

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)
