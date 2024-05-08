# Transform two lists into frozensets and find their common elements.

def find_intersection(list1, list2):
    set1 = frozenset(list1)
    set2 = frozenset(list2)
    return set1.intersection(set2)

print(find_intersection([2,4,6,8], [1,3,5,7,8])) # frozenset({8})