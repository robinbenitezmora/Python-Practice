# Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

def count_occurrences(lst):
    dict_ocurrences = {}
    for item in lst:
        dict_ocurrences[item] = lst.count(item)
    for key, value in dict_ocurrences.items():
        print(f"{key} => {value}")

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
