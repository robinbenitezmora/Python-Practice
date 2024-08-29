import random

try:
    from string import ascii_lowercase as letters
except ImportError:
    from string import lowercase as letters

def generate_key():
    key = list(letters)
    random.shuffle(key)
    return ''.join(key)

def encrypt(key, plaintext):
    return ''.join(key[letters.index(c)] for c in plaintext)

def decrypt(key, ciphertext):
    return ''.join(letters[key.index(c)] for c in ciphertext)

if __name__ == '__main__':
    key = generate_key()
    print(key)
    plaintext = 'hello'
    print(plaintext)
    ciphertext = encrypt(key, plaintext)
    print(ciphertext)
    decrypted = decrypt(key, ciphertext)
    print(decrypted)
    print(plaintext == decrypted
            and ciphertext != plaintext
            and ciphertext != decrypted)
    print(encrypt('abcdefghijklmnopqrstuvwxyz', 'hello'))
    print(decrypt('abcdefghijklmnopqrstuvwxyz', 'uryyb'))
    print(encrypt('abcdefghijklmnopqrstuvwxyz', 'hello'))
    print(decrypt('abcdefghijklmnopqrstuvwxyz', 'uryyb'))
    