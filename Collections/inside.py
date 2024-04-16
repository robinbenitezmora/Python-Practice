
def print_items(lists):
    if 3 in lists:
        print(f'3 is in {lists}')
    else:
        print(f'3 is not in {lists}')

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print_items(numbers1)
print_items(numbers2)
print_items(numbers3)
print_items(numbers4)
print_items(numbers5)
        