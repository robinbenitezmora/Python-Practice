import copy, sys, os

WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617)
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'

def wallStrToWallDict(wallStr):
    wallDict = {}
    for y, line in enumerate(wallStr.split('\n')):
        for x, char in enumerate(line):
            wallDict[(x, y)] = char
    return wallDict

def wallDictToWallStr(wallDict):
    maxX = max([x for x, y in wallDict])
    maxY = max([y for x, y in wallDict])
    wallStr = ''
    for y in range(maxY + 1):
        for x in range(maxX + 1):
            wallStr += wallDict.get((x, y), EMPTY)
        wallStr += '\n'
    return wallStr

def movePlayer(wallDict, playerPos, direction):
    x, y = playerPos
    if direction == NORTH:
        if wallDict.get((x, y - 1), EMPTY) != WALL:
            return (x, y - 1)
    if direction == SOUTH:
        if wallDict.get((x, y + 1), EMPTY) != WALL:
            return (x, y + 1)
    if direction == EAST:
        if wallDict.get((x + 1, y), EMPTY) != WALL:
            return (x + 1, y)
    if direction == WEST:
        if wallDict.get((x - 1, y), EMPTY) != WALL:
            return (x - 1, y)
    return playerPos

def displayMaze(wallDict, playerPos):
    maxX = max([x for x, y in wallDict])
    maxY = max([y for x, y in wallDict])
    for y in range(maxY + 1):
        for x in range(maxX + 1):
            if (x, y) == playerPos:
                print(PLAYER, end='')
            else:
                print(wallDict.get((x, y), EMPTY), end='')
        print()

while True:
    try:
        print('Enter the name of the maze file:')
        filename = input().strip()

        if filename.upper() == 'Q':
            sys.exit()

        if filename.upper() == 'LIST':
            print('Maze files found in ' + os.getcwd())
            for fileInCurrentFolder in os.listdir():
                if fileInCurrentFolder.endswith('.txt'):
                    print(fileInCurrentFolder)
            continue

        if os.path.exists(filename):
            break
        else:
            print('File not found. Try again or type Q to quit.')
    except:
        print('An error occurred. Please try again.')

mazefile = open(filename, 'r')
wallStr = mazefile.read()
wallDict = wallStrToWallDict(wallStr)

playerPos = None
for pos, char in wallDict.items():
    if char == START:
        playerPos = pos
        break

while True:
    displayMaze(wallDict, playerPos)

    print('Enter a direction to move: (N)orth, (S)outh, (E)ast, (W)est')
    move = input().upper()
    if move in (NORTH, SOUTH, EAST, WEST):
        playerPos = movePlayer(wallDict, playerPos, move)
    else:
        print('Invalid move. Enter N, S, E, or W.')
        continue

    if wallDict.get(playerPos) == EXIT:
        print('You have reached the exit!')
        break
    else:
        wallDict[playerPos] = EMPTY
        continue

print('Congratulations! You have reached the exit!')
mazefile.close()
