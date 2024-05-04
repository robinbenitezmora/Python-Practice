'''Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. Put the first half of the original list elements in the first element of the return value and put the second half in the second element. If the original list contains an odd number of elements, place the middle element in the first half list.'''

def halvsies(list1):
    if len(list1) % 2 == 0:
        return [list1[:len(list1)//2], list1[len(list1)//2:]]
    else:
        return [list1[:len(list1)//2 + 1], list1[len(list1)//2 + 1:]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
print(halvsies([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]])
print(halvsies([1, 2, 3, 4, 5, 6, 7]) == [[1, 2, 3, 4], [5, 6, 7]])
print(halvsies([1, 2, 3, 4, 5, 6, 7, 8]) == [[1, 2, 3, 4], [5, 6, 7, 8]])
    