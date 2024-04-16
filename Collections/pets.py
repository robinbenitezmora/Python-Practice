
pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet',
}

def get_pet_sound(pet):
    for key, value in pets.items():
        if key == pet:
            return value
    return f'<silence>'

print(get_pet_sound('Dog'))  # Bark
print(get_pet_sound('Lizard'))  # <silence>
