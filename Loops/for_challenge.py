
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

number = 0
num = 0
while number < len(my_list):
    item = my_list[number]
    while num < len(item):
        if item[num] % 2 == 0:
            print(item[num])
        num += 1
    number += 1
    num = 0

        