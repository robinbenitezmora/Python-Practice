
my_tuple = (1, 'a', '1', 3, [7], 3.1415, -4, None, {1, 2, 3}, False)

def find_integers(tuple):
    return [i for i in my_tuple if type(i) is int]

integers = find_integers(my_tuple)
print(integers)