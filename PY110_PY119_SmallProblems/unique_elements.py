# From two lists, determine the elements that are unique to the first list.

def unique_from_first(list1, list2):
    return set(list1) - set(list2)

print(unique_from_first([3,6,9,12], [6,12,15,18])) # {9, 3}