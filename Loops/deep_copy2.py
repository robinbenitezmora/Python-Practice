
dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict1.copy()
dict2['a'] = dict1['a'].copy()
dict2['a'][0] = dict1['a'][0].copy()
dict2['a'][1] = dict1['a'][1].copy()
dict2['b'] = list(dict1['b']).copy()
dict2['b'][0] = dict1['b'][0].copy()
dict2['b'][1] = dict1['b'][1].copy()

print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])