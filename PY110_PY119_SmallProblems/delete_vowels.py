# Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.

def remove_vowels(strings_list):
    new_list = []
    vowels = 'aeiouAEIOU'
    for string in strings_list:
        new_string = ''
        for char in string:
            if char not in vowels:
                new_string += char
        new_list.append(new_string)
    return new_list

print(remove_vowels(['apple', 'banana', 'cherry', 'date']))
# ['ppl', 'bnn', 'chrry', 'dt']
print(remove_vowels(['abcdefghijklmnopqrstuvwxyz']))        # ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(['green', 'YELLOW', 'black', 'white'])) # ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(['ABC', 'AEIOU', 'XYZ']))               # ['BC', '', 'XYZ']   