
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

big_list = zip(my_str, my_list, my_tuple, my_range)

print(list(big_list))