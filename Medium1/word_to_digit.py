'''Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.'''

def word_to_digit(message):
    word_to_digit_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for word in word_to_digit_dict:
        message = message.replace(word, word_to_digit_dict[word])
    return message

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4") # Should print True
message = 'Please call me at five five five one two three four five six seven eight nine zero'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4 5 6 7 8 9 0") # Should print True
message = 'Please call me at five five five one two three four five six seven eight nine zero zero nine eight seven six five four three two one'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4 5 6 7 8 9 0 0 9 8 7 6 5 4 3 2 1") # Should print True