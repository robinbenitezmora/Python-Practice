
def reminders(numbers):
    return [number % 3 for number in numbers]

numbers_1 = reminders([0, 1, 2, 3, 4, 5, 6,])
print(any(reminders(numbers_1)))
numbers_2 = reminders([1, 2, 4,5])
print(any(reminders(numbers_2)))
numbers_3 = reminders([0, 3, 6])
print(any(reminders(numbers_3)))
numbers_4 = reminders([])
print(any(reminders(numbers_4)))
