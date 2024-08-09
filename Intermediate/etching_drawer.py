import shutil, sys

UP_DOWN_CHAR = chr(9474)
LEFT_RIGHT_CHAR = chr(9472)
DOWN_RIGHT_CHAR = chr(9484)
DOWN_LEFT_CHAR = chr(9488)
UP_RIGHT_CHAR = chr(9492)
UP_LEFT_CHAR = chr(9496)
UP_DOWN_RIGHT_CHAR = chr(9500)
UP_DOWN_LEFT_CHAR = chr(9508)
DOWN_LEFT_RIGHT_CHAR = chr(9516)
UP_LEFT_RIGHT_CHAR = chr(9524)
CROSS_CHAR = chr(9532)

CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH -= 1
CANVAS_HEIGHT -= 5

canvas = {}
cursox = 0
cursory = 0

def getCanvasString(canvasData, cx, cy):
    canvasString = ''
    for y in range(CANVAS_HEIGHT):
        for x in range(CANVAS_WIDTH):
            if x == cx and y == cy:
                canvasString += '#'
                continue

            cell = canvasData.get((x, y), ' ')
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvasString += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasString += LEFT_RIGHT_CHAR
            elif cell in (set(['S', 'D'])):
                canvasString += DOWN_RIGHT_CHAR
            elif cell in (set(['A', 'S'])):
                canvasString += DOWN_LEFT_CHAR
            elif cell in (set(['W', 'D'])):
                canvasString += UP_RIGHT_CHAR
            elif cell in (set(['W', 'A'])):
                canvasString += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvasString += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvasString += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                canvasString += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                canvasString += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A', 'D']):
                canvasString += CROSS_CHAR
            elif cell == None:
                canvasString += ' '
        canvasString += '\n'
    return canvasString

moves = []
while True:
    print(getCanvasString(canvas, cursox, cursory))
    print('WASD keys to move, H for help, C to clear, ' + 'F to save, Q to quit')
    response = input('> ').upper()

    if response == 'Q':
        print('Quitting...')
        sys.exit()
    elif response == 'H':
        print('WASD keys to move the cursor')
        print('H for help')
        print('C to clear the canvas')
        print('F to save the canvas')
        print('Q to quit')
    elif response == 'C':
        canvas = {}
        moves.append('C')
    elif response == 'F':
        try:
            print('Enter the filename to save the canvas to:')
            filename = input('> ')

            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(getCanvasString(canvas, None, None))
        except:
            print('ERROR: Could not save file')

    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue
        moves.append(command)

        if canvas == {}:
            if command in ('W', 'S'):
                canvas[(cursox, cursory)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                canvas[(cursox, cursory)] = set(['A', 'D'])

        if command == 'W' and cursory > 0:
            canvas[(cursox, cursory)].add(command)
            cursory -= 1
        elif command == 'S' and cursory < CANVAS_HEIGHT - 1:
            canvas[(cursox, cursory)].add(command)
            cursory += 1
        elif command == 'D' and cursox < CANVAS_WIDTH - 1:
            canvas[(cursox, cursory)].add(command)
            cursox += 1
        else:
            continue

        if (cursox, cursory) not in canvas:
            canvas[(cursox, cursory)] = set()

        if command == 'W':
            canvas[(cursox, cursory)].add('S')
        elif command == 'S':
            canvas[(cursox, cursory)].add('W')
        elif command == 'A':
            canvas[(cursox, cursory)].add('D')
        elif command == 'D':
            canvas[(cursox, cursory)].add('A')

        if len(canvas[(cursox, cursory)]) == 4:
            canvas[(cursox, cursory)] = set(['W', 'S', 'A', 'D'])
        elif len(canvas[(cursox, cursory)]) == 3:
            if 'W' in canvas[(cursox, cursory)] and 'S' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['W', 'S'])
            elif 'A' in canvas[(cursox, cursory)] and 'D' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['A', 'D'])
        elif len(canvas[(cursox, cursory)]) == 2:
            if 'W' in canvas[(cursox, cursory)] and 'S' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['W', 'S'])
            elif 'A' in canvas[(cursox, cursory)] and 'D' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['A', 'D'])
            elif 'W' in canvas[(cursox, cursory)] and 'A' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['W', 'A'])
            elif 'W' in canvas[(cursox, cursory)] and 'D' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['W', 'D'])
            elif 'S' in canvas[(cursox, cursory)] and 'A' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['S', 'A'])
            elif 'S' in canvas[(cursox, cursory)] and 'D' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['S', 'D'])
        elif len(canvas[(cursox, cursory)]) == 1:
            if 'W' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['W'])
            elif 'S' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['S'])
            elif 'A' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['A'])
            elif 'D' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['D'])
        elif len(canvas[(cursox, cursory)]) == 0:
            canvas[(cursox, cursory)] = None

        if (cursox, cursory) not in canvas:
            canvas[(cursox, cursory)] = set()

        if command == 'W':
            canvas[(cursox, cursory)].add('S')
        elif command == 'S':
            canvas[(cursox, cursory)].add('W')
        elif command == 'A':
            canvas[(cursox, cursory)].add('D')
        elif command == 'D':
            canvas[(cursox, cursory)].add('A')

        if len(canvas[(cursox, cursory)]) == 4:
            canvas[(cursox, cursory)] = set(['W', 'S', 'A', 'D'])
        elif len(canvas[(cursox, cursory)]) == 3:
            if 'W' in canvas[(cursox, cursory)] and 'S' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['W', 'S'])
            elif 'A' in canvas[(cursox, cursory)] and 'D' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['A', 'D'])
        elif len(canvas[(cursox, cursory)]) == 2:
            if 'W' in canvas[(cursox, cursory)] and 'S' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['W', 'S'])
            elif 'A' in canvas[(cursox, cursory)] and 'D' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['A', 'D'])
            elif 'W' in canvas[(cursox, cursory)] and 'A' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['W', 'A'])
            elif 'W' in canvas[(cursox, cursory)] and 'D' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['W', 'D'])
            elif 'S' in canvas[(cursox, cursory)] and 'A' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['S', 'A'])
            elif 'S' in canvas[(cursox, cursory)] and 'D' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['S', 'D'])
        elif len(canvas[(cursox, cursory)]) == 1:
            if 'W' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['W'])
            elif 'S' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['S'])
            elif 'A' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['A'])
            elif 'D' in canvas[(cursox, cursory)]:
                canvas[(cursox, cursory)] = set(['D'])
        elif len(canvas[(cursox, cursory)]) == 0:
            canvas[(cursox, cursory)] = None
