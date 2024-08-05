import random, sys

print('''Dice Roller
Enter the number of dice to roll, followed by the number of sides each die has.
For example, 3d6 rolls three 6-sided dice.
Press Enter to roll or Q to quit.
''')

while True:
    try:
        diceStr = input('> ')
        if diceStr.upper() == 'Q':
            sys.exit()

        diceStr = diceStr.lower().replace(' ', '')

        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Invalid input. Example input: 3d6')
        
        numDice = int(diceStr[:dIndex])
        if not numDice.isdecimal():
            raise Exception('Invalid input. Example input: 3d6')
        
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        if modIndex == -1:
            numSides = int(diceStr[dIndex + 1:])
        else:
            numSides = int(diceStr[dIndex + 1:modIndex])
            modifier = int(diceStr[modIndex:])
    except Exception as e:
        print(e)
        continue

    rolls = []
    for _ in range(numDice):
        rolls.append(random.randint(1, numSides))

    print('Rolls: {}'.format(rolls))
    if modIndex != -1:
        print('Modifier: {}'.format(modifier))
        print('Total: {}'.format(sum(rolls) + modifier))
    else:
        print('Total: {}'.format(sum(rolls)))
    print()

# The Dice Roller program is a simple program that simulates rolling dice. The user enters the number of dice to roll and the number of sides each die has. The program then generates random numbers for each die and displays the results. The user can also add a modifier to the total result.
