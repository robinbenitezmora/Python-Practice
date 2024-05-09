# Given two lists of integers of the same length, return a new list where each element is the product of the corresponding elements from the two lists.

def multiply_elements(list1, list2):
    return [list1[i] * list2[i] for i in range(len(list1))]

print(multiply_elements([3, 5, 7], [9, 10, 11]))  # [27, 50, 77]
print(multiply_elements([10, 20, 30], [0, 1, 2])) # [0, 20, 60]
print(multiply_elements([1, 2, 3], [4, 5, 6]))    # [4, 10, 18]
print(multiply_elements([0, 0, 0], [1, 2, 3]))    # [0, 0, 0]
print(multiply_elements([1, 2, 3], [0, 0, 0]))    # [0, 0, 0]
print(multiply_elements([1], [1]))                 # [1]
print(multiply_elements([], []))                   # []
