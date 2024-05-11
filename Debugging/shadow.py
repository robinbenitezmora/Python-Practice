# We have a list of lists and want to make a copy of it. After making the copy, we modify the original list, but the copied list also seems to be affected:

def sum(numbers, factor):
    total = 0
    for number in numbers:
        total += number
    return factor * total

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)
