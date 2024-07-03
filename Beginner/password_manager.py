pwd = input('Enter the master password: ')

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split('|')
            print('User:', user, 'Password:', password)

def add():
    name = input('Account name: ')
    pwd = input('Password: ')
    
    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + pwd + '\n')

while True:
    if pwd == '123':
        mode = input('Would you like to add a new password or view existing ones (view, add), press q to quit? ').lower()
        if mode == 'q':
            break
        if mode == 'view':
            view()
        elif mode == 'add':
            add()
        else:
            print('Invalid mode.')
            continue
    else:
        print('Wrong password. Try again.')
        break
print('Goodbye!')