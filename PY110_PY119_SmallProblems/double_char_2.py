'''Write a function that takes a string, doubles every consonant in the string, and returns the result as a new string. The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.'''

def double_consonants(string):
    new_string = ''
    for i in string:
        if i.isalpha() and i not in 'aeiouAEIOU':
            new_string += i * 2
        else:
            new_string += i
    return new_string

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
