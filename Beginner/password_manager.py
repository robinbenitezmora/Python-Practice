from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "Password:", passw)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

def update():
    name = input("Account name: ")
    pwd = input("New password: ")

    with open('passwords.txt', 'r') as f:
        lines = f.readlines()

    with open('passwords.txt', 'w') as f:
        for line in lines:
            user, passw = line.strip().split("|")
            if user == name:
                f.write(user + "|" + pwd + "\n")
            else:
                f.write(user + "|" + passw + "\n")

def delete():
    name = input("Account name: ")

    with open('passwords.txt', 'r') as f:
        lines = f.readlines()

    with open('passwords.txt', 'w') as f:
        for line in lines:
            user, passw = line.strip().split("|")
            if user != name:
                f.write(user + "|" + passw + "\n")

def encrypt():
    with open('passwords.txt', 'r') as f:
        data = f.read()

    f = Fernet(master_pwd)
    encrypted = f.encrypt(data.encode())

    with open('passwords.txt', 'w') as f:
        f.write(encrypted.decode())

def decrypt():
    with open('passwords.txt', 'r') as f:
        data = f.read()

    f = Fernet(master_pwd)
    decrypted = f.decrypt(data.encode())

    with open('passwords.txt', 'w') as f:
        f.write(decrypted.decode())

while True:
    mode = input("Would you like to add a new password, view existing passwords, update a password, or delete a password (add, view, update, delete)? If you want to exit, type 'exit'. ").lower()
    if mode == 'exit':
        encrypt()
        break
    elif mode == 'view':
        decrypt()
        view()
    elif mode == 'add':
        decrypt()
        add()
    elif mode == 'update':
        decrypt()
        update()
    elif mode == 'delete':
        decrypt()
        delete()
    else:
        print("Invalid mode.")
        continue
    encrypt()
