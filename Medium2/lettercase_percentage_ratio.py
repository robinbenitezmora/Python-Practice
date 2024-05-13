'''Write a function that takes a string and returns an object containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
You may assume that the string will always contain at least one character.'''

def letter_percentages(string):
    total = len(string)
    lower = sum(1 for c in string if c.islower())
    upper = sum(1 for c in string if c.isupper())
    other = total - lower - upper
    return {
        'lowercase': lower / total * 100,
        'uppercase': upper / total * 100,
        'neither': other / total * 100,
    }

print(letter_percentages('abCdef 123'))
# { 'lowercase': "50.00", 'uppercase': "10.00", 'neither': "40.00" }

print(letter_percentages('AbCd +Ef'))
# { 'lowercase': "37.50", 'uppercase': "37.50", 'neither': "25.00" }

print(letter_percentages('123'))
# { 'lowercase': "0.00", 'uppercase': "0.00", 'neither': "100.00" }
