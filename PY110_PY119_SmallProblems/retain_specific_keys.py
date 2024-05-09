# Given a dictionary and a list of keys, produce a new dictionary that only retains the entries with the specified keys.

def keep_keys(dictionary, keys_list):
    return {key: value for key, value in dictionary.items() if key in keys_list}

print(keep_keys({'apple': 'fruit', 'broccoli': 'vegetable', 'salmon': 'fish'}, ['apple', 'salmon']))
# {'apple': 'fruit', 'salmon': 'fish'}
print(keep_keys({'red': 1, 'green': 2, 'blue': 3, 'yellow': 4}, ['red', 'blue']))
# {'red': 1, 'blue': 3}
