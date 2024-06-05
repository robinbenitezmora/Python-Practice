agenda = {}

def add_contact():
    name = input('\nEnter the name of the contact:\n')
    phone = input('\nEnter the phone number of the contact:\n')
    agenda[name] = phone
    print(f'\nContact {name} added successfully')

def search_contact():
    name = input('\nEnter the name of the contact:\n')
    if name in agenda:
        print(f'\nName: {name}, Phone: {agenda[name]}')
    else:
        print(f'\nContact {name} not found')

def delete_contact():
    name = input('\nEnter the name of the contact:\n')
    if name in agenda:
        del agenda[name]
        print(f'\nContact {name} deleted successfully\n')
    else:
        print(f'\nContact {name} not found\n')

def modify_contact():
    print('What do you want to modify?\n Write option 1 for name, and option 2 for phone number\n')
    option = int(input())
    name = input('\nEnter the name of the contact:\n')
    if name in agenda:
        if option == 1:
            new_name = input('\nEnter the new name of the contact:\n')
            agenda[new_name] = agenda.pop(name)
            print(f'\nContact {name} modified successfully\n')
        elif option == 2:
            new_phone = input('\nEnter the new phone number of the contact:\n')
            agenda[name] = new_phone
            print(f'\nContact {name} modified successfully')
        else:
            print('Invalid option')
    else:
        print(f'\nContact {name} not found')

def show_contacts():
    if len(agenda) == 0:
        print('\nNo contacts found')
    else:
        print('\nContacts:')
        for name, phone in agenda.items():
            print(f'Name: {name}, Phone: {phone}')

def main():
    while True:
        print('\nWelcome to the agenda')
        print('1. Add contact')
        print('2. Search contact')
        print('3. Delete contact')
        print('4. Modify contact')
        print('5. Show contacts')
        print('6. Exit\n')
        option = int(input('Choose an option:\n'))

        if option == 1:
            add_contact()
        elif option == 2:
            search_contact()
        elif option == 3:
            delete_contact()
        elif option == 4:
            modify_contact()
        elif option == 5:
            show_contacts()
        elif option == 6:
            break
        else:
            print('Invalid option')

if __name__ == '__main__':
    main()
