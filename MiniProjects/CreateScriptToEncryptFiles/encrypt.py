import sys
import os
from Crytodome.Cipher import AES
from Crytodome import Random
from binascii import b2a_hex

def encrypt_dir(path):
    for root, _, files in os.walk('.'):
        for file in files:
            path = os.path.join(root, file)
            print(path + ' is encrypting.')
            encrypt_file(path)

def encrypt_file(path):
    with open(path) as f:
        plain_text = f.read()

    key = b'this is a 16 key'

    iv = Random.new().read(AES.block_size)
    mycipher = AES.new(key, AES.MODE_CFB, iv)
    cipher_text = iv + mycipher.encrypt(plain_text.encode())

    with open(path + '.bin', 'wb') as file_out:
        file_out.write(cipher_text[16])

path = sys.argv[1]

if os.path.isdir(path) and os.path.exists(path):
    encrypt_dir(path)
elif os.path.isfile(path) and os.path.exists(path):
    encrypt_file(path)
else:
    print('Invalid path')
    