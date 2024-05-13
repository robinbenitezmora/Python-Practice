'''Write a function that takes two sorted lists as arguments and returns a new list that contains all the elements from both input lists in sorted order.

You may not provide any solution that requires you to sort the result list. You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.'''

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

print(merge([1, 5, 9], [2, 6, 8]))      # [1, 2, 5, 6, 8, 9]
print(merge([1, 1, 3], [2, 2]))         # [1, 1, 2, 2, 3]
print(merge([], [1, 4, 5]))             # [1, 4, 5]
print(merge([1, 4, 5], []))             # [1, 4, 5]    