import random

def generate_character_map():
    character_map = {}
    for i in range(0, 26):
        character_map[chr(i + 65)] = chr(i + 97)
    return character_map

def generate_random_key():
    key = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    random.shuffle(key)
    return ''.join(key)

def encrypt_message(character_map, key, message):
    encrypted_message = ''
    for character in message:
        if character in character_map:
            encrypted_message += key[ord(character_map[character]) - 97]
        else:
            encrypted_message += character
    return encrypted_message

def decrypt_message(character_map, key, message):
    decrypted_message = ''
    for character in message:
        if character in character_map:
            decrypted_message += character_map[key.index(character) + 97]
        else:
            decrypted_message += character
    return decrypted_message

def main():
    character_map = generate_character_map()
    key = generate_random_key()
    message = 'Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist.'
    encrypted_message = encrypt_message(character_map, key, message)
    decrypted_message = decrypt_message(character_map, key, encrypted_message)
    
    print('Key: %s' % (key))
    print('Original message:')
    print(message)
    print('Encrypted message:')
    print(encrypted_message)
    print('Decrypted message:')
    print(decrypted_message)

if __name__ == '__main__':
    main()
