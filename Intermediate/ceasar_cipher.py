'''
Caesar Cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in practice offers essentially no communication security.

The transformation can be represented by aligning two alphabets; the cipher alphabet is the plain alphabet rotated left or right by some number of positions. For instance, here is a Caesar cipher using a left rotation of three places, equivalent to a right shift of 23 (the shift parameter is used as the key):

Plain:    ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cipher:   XYZABCDEFGHIJKLMNOPQRSTUVW
When encrypting, a person looks up each letter of the message in the "plain" line and writes down the corresponding letter in the "cipher" line.

Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
Deciphering is done in reverse, with a right shift of 3.

The encryption can also be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A → 0, B → 1, ..., Z → 25.[1] Encryption of a letter x by a shift n can be described mathematically as,

E_n(x) = (x + n) mod 26
Decryption is performed similarly,

D_n(x) = (x - n) mod 26
(There are different definitions of the modulo operation. In the above, the result is in the range 0...25. I.e., if x + n or x - n are not in the range 0...25, we have to subtract or add 26.)

The replacement remains the same throughout the message, so the cipher is classed as a type of monoalphabetic substitution, as opposed to polyalphabetic substitution.

'''

import sys

try:
    import pyperclip
except ImportError:
    print('This program requires the pyperclip module, which you can install by running pip install pyperclip from the command line.')
    sys.exit()

def encryptMessage(message, key):
    # implementation of the encryptMessage function goes here
    pass

def decryptMessage(message, key):
    # implementation of the decryptMessage function goes here
    pass

def main():
    print('Caesar Cipher')
    print('The Caesar cipher encrypts or decrypts text by shifting the letters by a fixed number of places.')
    print()

    while True:
        print('Do you want to (E)ncrypt or (D)ecrypt?')
        response = input('> ').upper()
        if response in ('E', 'D'):
            break
        print('Please enter E or D.')

    print('Enter the message:')
    message = input('> ')

    print('Enter the key (1-25):')
    key = int(input('> '))

    if response == 'E':
        translated = encryptMessage(message, key)
    else:
        translated = decryptMessage(message, key)

    print('The translated message is:')
