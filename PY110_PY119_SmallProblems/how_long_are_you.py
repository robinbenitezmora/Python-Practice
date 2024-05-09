'''Write a function that takes a string as an argument and returns a list that contains every word from the string, with each word followed by a space and the word's length. If the argument is an empty string or if no argument is passed, the function should return an empty list.

You may assume that every pair of words in the string will be separated by a single space.'''

def word_lengths(string):
    if string == '' or string == None:
        return []
    words = string.split()
    return [f'{word} {len(word)}' for word in words]

#
print(word_lengths('cow sheep chicken'))
# ['cow 3', 'sheep 5', 'chicken 7']

print(word_lengths('baseball hot dogs and apple pie'))
# ['baseball 8', 'hot 3', 'dogs 4', 'and 3', 'apple 5', 'pie 3']

print(word_lengths("It ain't easy, is it?"))
# ['It 2', "ain't 5", 'easy, 5', 'is 2', 'it? 3']

print(word_lengths('Supercalifragilisticexpialidocious'))
# ['Supercalifragilisticexpialidocious 34']

print(word_lengths(''))      # []
#print(word_lengths())        # []
    