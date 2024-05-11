

def sum(numbers, factor):
    total = 0
    for number in numbers:
        total += number
    return factor * total

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)
