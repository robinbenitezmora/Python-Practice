name = input('What is your name? ')
print(f'Hello, {name}! Welcome to choose your own adventure!')

answer = input('You are in a dirt road, it has come to an end you can go left or right. Which way would you like to go? ').lower()

if answer == 'left':
    answer = input('You come across a river, you can walk around it or swim across. What would you like to do? ').lower()
    
    if answer == 'walk':
        print('You walked around the river and reached the other side safely.')
    elif answer == 'swim':
        print('You swam across the river and were eaten by an alligator.')
    else:
        print('Not a valid option. You lose.')

elif answer == 'right':
    answer = input('You come across a bridge, you can cross it or jump off. What would you like to do? ').lower()
    
    if answer == 'cross':
        print('You crossed the bridge and reached the other side safely.')
    elif answer == 'jump':
        print('You jumped off the bridge and died.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print('Thanks for playing!')