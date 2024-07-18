import random

def password_generator(pwlength):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    passwords = []

    for i in pwlength:
        password = ''
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        passwords.append(password)
    return passwords

def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
    return pword

def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
    return pword

def main():
    print('Welcome to the Password Generator!')
    print('This program generates random passwords of varying lengths.')
    print('How many passwords would you like to generate?')
    num_pw = int(input())
    print('Enter the length of each password:')
    pw_length = []
    for i in range(num_pw):
        pw_length.append(int(input()))
    passwords = password_generator(pw_length)
    for password in passwords:
        print(password)

if __name__ == '__main__':
    main()
    