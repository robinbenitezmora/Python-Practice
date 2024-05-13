'''Write a function that takes a list argument and returns a new list that contains the values from the input list in sorted order. The function should sort the list using the merge sort algorithm as described above. You may assume that every element of the list will be of the same data type—either all numbers or all strings.

Feel free to use the merge function you wrote in the previous exercise.'''
def merge(lst1, lst2):
    result = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            result.append(lst1.pop(0))
        else:
            result.append(lst2.pop(0))
    result.extend(lst1)
    result.extend(lst2)
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

print(merge_sort([9, 5, 7, 1]))           # [1, 5, 7, 9]
print(merge_sort([5, 3]))                 # [3, 5]
print(merge_sort([6, 2, 7, 1, 4]))        # [1, 2, 4, 6, 7]

print(merge_sort(['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']))
# ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]

print(merge_sort([7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54, 43, 5, 25, 35, 18, 46]))
# [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25, 35, 37, 43, 46, 51, 54]