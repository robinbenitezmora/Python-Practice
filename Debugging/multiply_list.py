# You want to multiply all elements of a list by 2. However, the function is not returning the expected result.

def multiply_list(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i * 2)
    return new_lst

print(multiply_list([1, 2, 3, 4, 5]))  # [2, 4, 6, 8, 10]
print(multiply_list([10, 20, 30, 40, 50]))  # [20, 40, 60, 80, 100]
print(multiply_list([0, 0, 0, 0, 0]))  # [0, 0, 0, 0, 0]
print(multiply_list([1, 3, 5, 7, 9]))  # [2, 6, 10, 14, 18]
print(multiply_list([2, 4, 6, 8, 10]))  # [4, 8, 12, 16, 20]
print(multiply_list([1, 4, 9, 16, 25]))  # [2, 8, 18, 32, 50]
print(multiply_list([1, 1, 1, 1, 1]))  # [2, 2, 2, 2, 2]
print(multiply_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]