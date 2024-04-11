
def reminders(numbers):
    return [number % 5 for number in numbers]

numbers_1 = reminders([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(all(reminders(numbers_1)))
numbers_2 = reminders([1, 2, 3, 4, 6, 7, 8, 9])
print(all(reminders(numbers_2)))
numbers_3 = reminders([0, 5, 10])
print(all(reminders(numbers_3)))
numbers_4 = reminders([])
print(all(reminders(numbers_4)))