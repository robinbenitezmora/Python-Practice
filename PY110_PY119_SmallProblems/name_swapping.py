# Write a function that takes a string argument consisting of a first name, a space, and a last name, and returns a new string consisting of the last name, a comma, a space, and the first name.

def swap_name(name):
    name = name.split()
    return f'{name[1]}, {name[0]}'

print(swap_name('Joe Roberts'))    # "Roberts, Joe"    