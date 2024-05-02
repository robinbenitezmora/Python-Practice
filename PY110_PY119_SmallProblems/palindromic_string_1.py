# Write a function that returns True if the string passed as an argument is a palindrome, False otherwise. A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

def palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-(i + 1)]:
            return False
    return True

# All of these examples should print True

print(palindrome('madam') == True)
print(palindrome('356653') == True)
print(palindrome('356635') == False)

# case matters
print(palindrome('Madam') == False)

# all characters matter
print(palindrome("madam i'm adam") == False)