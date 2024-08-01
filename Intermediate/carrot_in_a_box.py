import random

print('''
Ceasar Hacker, a program that can decrypt a Ceasar cipher without knowing the key.
''')

print('Press Enter to begin...')
input()

p1Name = input('Enter player 1\'s name: ')
p2Name = input('Enter player 2\'s name: ')
playerNames = p1Name[:11].center(11) + ' ' + p2Name[:11].center(11)

print('''HERE ARE TWO BOXES. IN ONE BOX, THERE IS A PRIZE. THE OTHER BOX IS EMPTY.
YOU WILL TAKE TURNS SELECTING A BOX. AFTER YOU SELECT A BOX, I WILL SHOW YOU
ANOTHER BOX THAT IS EMPTY. YOU CAN THEN STICK WITH YOUR ORIGINAL BOX OR SWITCH
TO THE OTHER UNSELECTED BOX. AFTER YOU MAKE YOUR FINAL SELECTION, I WILL SHOW
YOU WHAT IS IN THE BOX YOU SELECTED. THE PLAYER WHO SELECTS THE BOX WITH THE
PRIZE WINS. GOOD LUCK!''')

print()
print(playerNames)
print('  +---+   +---+')
print('  |   |   |   |')
print('  | 1 |   | 2 |')
print('  |   |   |   |')
print('  +---+   +---+')
print()

prizeBox = random.randint(1, 2)
print('Press Enter to select a box...')
input()

if prizeBox == 1:
    emptyBox = 2
else:
    emptyBox = 1

print(playerNames)
print('  +---+   +---+')
print('  |   |   |   |')
print('  | {} |   | {} |'.format('X' * len(p1Name), 'X' * len(p2Name)))
print('  |   |   |   |')
print('  +---+   +---+')
print()

print('Press Enter to see what is in Box {}...'.format(emptyBox))
input()

if emptyBox == 1:

    print(playerNames)
    print('  +---+   +---+')
    print('  |   |   |   |')
    print('  |   |   | {} |'.format('X' * len(p2Name)))
    print('  |   |   |   |')
    print('  +---+   +---+')
    print()

else:
    
        print(playerNames)
        print('  +---+   +---+')
        print('  |   |   |   |')
        print('  | {} |   |   |'.format('X' * len(p1Name)))
        print('  |   |   |   |')
        print('  +---+   +---+')
        print()

print('Press Enter to make your final selection...')                    

input()

print(playerNames)

if prizeBox == 1:
    print('  +---+   +---+')
    print('  |   |   |   |')
    print('  | {} |   | {} |'.format('X' * len(p1Name), 'X' * len(p2Name)))
    print('  |   |   |   |')
    print('  +---+   +---+')
    print()
else:
    print('  +---+   +---+')
    print('  |   |   |   |')
    print('  | {} |   | {} |'.format('X' * len(p1Name), 'X' * len(p2Name)))
    print('  |   |   |   |')
    print('  +---+  +---+')                                      
    print()

if prizeBox == 1:
    print('Congratulations! {} wins!'.format(p1Name))
else:
    print('Congratulations! {} wins!'.format(p2Name))

# # # What is the output of the following code?
# # # A) The code will run a game where two players take turns selecting one of two boxes. One box contains a prize and the other is empty. After each player selects a box, the other box is revealed to be empty. The player who selects the box with the prize wins. The code will print out the winner of the game.

# # # B) The code will run a game where two players take turns selecting one of two boxes. One box contains a prize and the other is empty. After each player selects a box, the other box is revealed to be empty. The player who selects the box with the prize wins. The code will print out the winner of the game.

# # # C) The code will run a game where two players take turns selecting one of two boxes. One box contains a prize and the other is empty. After each player selects a box, the other box is revealed to be empty. The player who selects the box with the prize wins. The code will print out the winner of the game. The code will also print out the names of the players and the boxes they selected.

# # # D) The code will run a game where two players take turns selecting one of two boxes. One box contains a prize and the other is empty. After each player selects a box, the other box is revealed to be empty. The player who selects the box with the prize wins. The code will print out the winner of the game. The code will also print out the names of the players and the boxes they selected. The code will also print out the contents of the boxes before and after each player's selection.

















