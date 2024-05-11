# Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the initial occurrence. Return the refined sequence.

def unique_sequence(lst):
    return list(dict.fromkeys(lst))

print(unique_sequence([1, 1, 2, 3, 3, 3, 4, 5, 5, 6]))
# [1, 2, 3, 4, 5, 6]