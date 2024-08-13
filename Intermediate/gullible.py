'''
Gullible, a program that asks the user for a number and then prints "That's impossible!" if the user doesn't enter 5.
'''

while True:
    print('Do you want to know how to keep an idiot in suspense? (yes or no)')
    response = input('> ').lower()
    if response.startswith('n'):
        break
    print('Enter a number:')
    number = input()
    if number != '5':
        print("That's impossible!")
    else:
        print("You're not an idiot!")

print('Thanks for playing!')
