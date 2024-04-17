my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []

for i in my_list:
    if i % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')

print(new_list)