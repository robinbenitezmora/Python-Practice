# You have a function that should check whether a key exists in a dictionary and returns its value. However, it's raising an error. Why is that? How would you fix this code?

def get_key_value(my_dict, key):
    try:
        return my_dict[key]
    except KeyError:
        return f'key not found'

print(get_key_value({'a': 1}, 'b'))
