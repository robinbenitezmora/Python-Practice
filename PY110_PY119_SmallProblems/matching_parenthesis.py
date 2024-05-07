# Write a function that takes a string as an argument and returns True if all parentheses in the string are properly balanced, False otherwise. To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

def is_balanced(string):
    if string.count('(') == string.count(')'):
        return True

print(is_balanced("What (is) this?") == True)
print(is_balanced("What is) this?") == False)
print(is_balanced("What (is this?") == False)
print(is_balanced("((What) (is this))?") == True)
print(is_balanced("((What)) (is this))?") == False)
print(is_balanced("Hey!") == True)
print(is_balanced(")Hey!(") == False)
print(is_balanced("What ((is))) up(") == False)    
