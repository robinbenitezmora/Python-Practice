
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

def amount_letters(words):
    return { name: len(name) for name in words if len(name) % 2 != 0 }

name_lengths = amount_letters(my_set)
print(name_lengths)