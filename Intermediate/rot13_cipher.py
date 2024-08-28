'''
ROT13 Cipher is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the alphabet. ROT13 is a special case of the Caesar cipher which was developed in ancient Rome.

To write a ROT13 cipher in Python, here are the steps we'll need to take:

1. Ask the user to input a message to encrypt or decrypt.
2. Make sure the user entered a valid message.
3. Convert the message to ROT13.
4. Display the encrypted or decrypted message.
'''

try:
    import pyperclip
except ImportError:
    print('pyperclip module is not installed. Install it using pip install pyperclip')

def rot13(message):
    encrypted = ''
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
        else:
            encrypted += char
    return encrypted

def main():
    print('ROT13 Cipher')
    print('Enter a message to encrypt or decrypt using ROT13')
    message = input()
    if message.isprintable():
        encrypted = rot13(message)
        print(f'The ROT13 encryption of the message is: {encrypted}')
        pyperclip.copy(encrypted)
        print('The encrypted message has been copied to the clipboard')
    else:
        print('Invalid message. Please enter a valid message')

if __name__ == '__main__':
    main()
    