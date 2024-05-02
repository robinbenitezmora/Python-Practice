

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