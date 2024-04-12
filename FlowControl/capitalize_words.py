word = input('Please write a word:\n ')

def capitalize(word):
    new_word = ''
    if len(word) > 10:
        new_word = word.upper()
        return new_word
    else:
        return word

print(capitalize(word))


