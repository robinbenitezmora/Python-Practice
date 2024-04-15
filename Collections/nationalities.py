
nationality = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganada',
    'Yoshitaka': 'Japan'
}

def get_national(name):
    for key, value in nationality.items():
        if key == name:
            return f'{name} is from {value}'
    return f'{name} is not in the list'

print(get_national('Alice'))
print(get_national('Francois'))
print(get_national('Peter'))
print(get_national('Monika'))
print(get_national('Sanyu'))
print(get_national('Keisha'))
print(get_national('Yoshitaka'))
print(get_national('Inti'))
print(get_national('Annette'))