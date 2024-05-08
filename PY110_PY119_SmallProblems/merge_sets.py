# Given two lists, convert them to sets and return a new set which is the union of both sets.

def merge_sets(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.union(set2)

print(merge_sets([3,5,7,9], [5,7,11,13]))
# {3, 5, 7, 9, 11, 13}    
