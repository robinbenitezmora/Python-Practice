# Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two lists. You may assume that both arguments will always be lists.

def union(list1, list2):
    total_list = list1 + list2
    for i in total_list:
        if total_list.count(i) > 1:
            total_list.remove(i)
    return set(total_list)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True    
