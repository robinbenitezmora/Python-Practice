
# You may modify this line

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = dict(dict1)
dict2['a'] = list(dict1['a'])
dict2['a'][0] = list(dict1['a'][0])
dict2['a'][1] = list(dict1['a'][1])
dict2['b'] = list(dict1['b'])
dict2['b'][0] = list(dict1['b'][0])
dict2['b'][1] = list(dict1['b'][1])

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])