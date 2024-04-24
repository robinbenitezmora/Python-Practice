
phrase = 'launch school tech & talk'
phrase_capitalize = phrase.split(' ')
phrase_capitalize = [word.capitalize() for word in phrase_capitalize]
phrase_capitalize = ' '.join(phrase_capitalize)
print(phrase_capitalize)