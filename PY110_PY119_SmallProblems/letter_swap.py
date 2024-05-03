'''Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.'''

def swap(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) > 1:
            words[i] = words[i][-1] + words[i][1:-1] + words[i][0]
    return ' '.join(words)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True    
