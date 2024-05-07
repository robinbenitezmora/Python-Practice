# Write a function that takes a string, doubles every character in the string, and returns the result as a new string.

def repeater(string):
    new_string = ''
    for i in string:
        new_string += i * 2
    return new_string

print(repeater('Hello'))        # "HHeelllloo"
print(repeater('Good job!'))    # "GGoooodd  jjoobb!!"
print(repeater(''))             # ""    
