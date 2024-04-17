
names = ['Chris', 'Susan', 'Bill', 'Raymond', 'Graham']
upper_names = []

for name in names:
    if name == 'Bill':
        continue
    upper_names.append(name.upper())

print(upper_names)
    