'''Given a string that consists of some words and an assortment of non-alphabetic characters, write a function that returns that string with all of the non-alphabetic characters replaced by spaces. If one or more non-alphabetic characters occur in a row, you should only have one space in the result (i.e., the result string should never have consecutive spaces).'''

def cleanup(string):
    result = ''
    for char in string:
        if char.isalpha():
            result += char
        else:
            if result and result[-1] != ' ':
                result += ' '
    return result.strip()

print(cleanup("---what's my +*& line?") == 'what s my line') # True
print(cleanup("what's my line?") == 'what s my line') # True
