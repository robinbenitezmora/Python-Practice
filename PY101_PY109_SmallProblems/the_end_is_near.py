'''Write a function that returns the next to last word in the string argument.

Words are any sequence of non-blank characters.

You may assume that the input string will always contain at least two words'''


def penultimate(string):
    string = string.split()
    return string[-2]

print(penultimate('last word') == 'last')
print(penultimate('Launch School is great!') == 'is')