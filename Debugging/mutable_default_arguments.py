# We want to create a function that appends a given value to a list. However, the function seems to be behaving unexpectedly

def append_to_list(value, lst = None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print(append_to_list(1))        # Expected: [1]
print(append_to_list(2))        # Expected: [2]
print(append_to_list(3))        # Expected: [3]
print(append_to_list(4))        # Expected: [4]
print(append_to_list(5, [1, 2]))  # Expected: [1, 2, 5]
print(append_to_list(6))        # Expected: [6]