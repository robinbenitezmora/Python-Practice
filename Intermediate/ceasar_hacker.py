'''
Ceasar Hacker, a program that can decrypt a Ceasar cipher without knowing the key.
'''

print('Ceasar Hacker')
print('Enter the encrypted message:')
message = input('> ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            if translatedIndex < 0:
                translatedIndex += len(SYMBOLS)
            translated += SYMBOLS[translatedIndex]
        else:
            translated += symbol
    print('Key #{}: {}'.format(key, translated))

print('All possible decryptions have been displayed.')
print('The original message could be any of the above, or none of them.')
# # What is the output of the following code?
# # A) The code will run a Caesar cipher decryption program that tries all possible keys to decrypt the message. It will print out all possible decryptions of the message for each key.
# # The original message could be any of the above, or none of them.

# # B) The code will run a Caesar cipher decryption program that tries all possible keys to decrypt the message. It will print out all possible decryptions of the message for each key. The original message could be any of the above, or none of them.

