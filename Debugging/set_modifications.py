# We want to remove certain items from a set while iterating over it, but the code below throws an error. Why is that and how can we fix it?

data_set = {1, 2, 3, 4, 5}

for item in data_set:
    lst = list(data_set)
    if item % 2 == 0:
        lst.remove(item)
        data_set = set(lst)

print(data_set)  # Expected: {1, 3, 5}