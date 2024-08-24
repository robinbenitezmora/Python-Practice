import random, sys

ALL_CLOSED = '''
+-----+ +-----+  +-----+
|     | |     |  |     |
|     | |     |  |     |
|     | |     |  |     |
+-----+ +-----+  +-----+
'''

FIRST_GOAT = '''
+-----+ +-----+  +-----+
|     | |     |  |     |
|  G  | |     |  |     |
|     | |     |  |     |
+-----+ +-----+  +-----+
'''

SECOND_GOAT = '''
+-----+ +-----+  +-----+
|     | |     |  |     |
|     | |  G  |  |     |
|     | |     |  |     |
+-----+ +-----+  +-----+
'''

THIRD_GOAT = '''
+-----+ +-----+  +-----+
|     | |     |  |     |
|     | |     |  |  G  |
|     | |     |  |     |
+-----+ +-----+  +-----+
'''

FIRST_CAR_OTHERS_GOAT = '''
+-----+ +-----+  +-----+
|  C  | |     |  |     |
|     | |     |  |     |
|     | |     |  |     |
+-----+ +-----+  +-----+
'''

SECOND_CAR_OTHERS_GOAT = '''
+-----+ +-----+  +-----+
|     | |  C  |  |     |
|     | |     |  |     |
|     | |     |  |     |
+-----+ +-----+  +-----+
'''

THIRD_CAR_OTHERS_GOAT = '''
+-----+ +-----+  +-----+
|     | |     |  |  C  |
|     | |     |  |     |
|     | |     |  |     |
+-----+ +-----+  +-----+
'''

print('Monty Hall Problem')

input('Press Enter to start...')

swapWins = 0
stickWins = 0
swapLoses = 0
stickLoses = 0

while True:
    # Set up the doors:
    doors = [FIRST_GOAT, SECOND_GOAT, THIRD_GOAT]
    random.shuffle(doors)

    # Display the doors to the player:
    print(ALL_CLOSED)
    input('Press Enter to open a door...')
    print(doors[0])

    # The player selects a door:
    while True:
        print('Select a door: 1, 2, or 3')
        response = input()
        if response in ['1', '2', '3']:
            break
    selectedDoorIndex = int(response) - 1

    # Monty opens a door:
    closedDoorIndexes = [0, 1, 2]
    closedDoorIndexes.remove(selectedDoorIndex)
    if doors[closedDoorIndexes[0]] == FIRST_GOAT:
        closedDoorIndexes.remove(closedDoorIndexes[0])
    else:
        closedDoorIndexes.remove(closedDoorIndexes[1])
    montyOpens = closedDoorIndexes[0]

    print('Monty opens door %s.' % (montyOpens + 1))
    input('Press Enter to swap doors...')
    print('You selected door %s.' % (selectedDoorIndex + 1))
    print('The car was behind door %s.' % ([FIRST_CAR_OTHERS_GOAT, SECOND_CAR_OTHERS_GOAT, THIRD_CAR_OTHERS_GOAT].index(doors) + 1))

    # Determine if the player wins:
    if doors[selectedDoorIndex] == FIRST_CAR_OTHERS_GOAT:
        stickWins += 1
    else:
        stickLoses += 1

    # Swap the player's selected door:
    swapDoorIndexes = [0, 1, 2]
    swapDoorIndexes.remove(selectedDoorIndex)
    swapDoorIndexes.remove(montyOpens)
    selectedDoorIndex = swapDoorIndexes[0]

    print('You selected door %s.' % (selectedDoorIndex + 1))
    print('The car was behind door %s.' % ([FIRST_CAR_OTHERS_GOAT, SECOND_CAR_OTHERS_GOAT, THIRD_CAR_OTHERS_GOAT].index(doors) + 1))

    # Determine if the player wins:
    if doors[selectedDoorIndex] == FIRST_CAR_OTHERS_GOAT:
        swapWins += 1
    else:
        swapLoses += 1

    # Display the results:
    print()
    print('Stick with the original door:')
    print('Wins: %s, Losses: %s' % (stickWins, stickLoses))
    print('Swap doors:')
    print('Wins: %s, Losses: %s' % (swapWins, swapLoses))
    print()
    print('Win ratio if you stick: %s' % (stickWins / (stickWins + stickLoses)))
    print('Win ratio if you swap: %s' % (swapWins / (swapWins + swapLoses)))
    print()

    print('Play again? (yes or no)')
    response = input()
    if not response.lower().startswith('y'):
        break

print('Thanks for playing!')
