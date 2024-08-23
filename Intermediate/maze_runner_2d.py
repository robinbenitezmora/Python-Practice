import sys, os

WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'

PLAYER = '@'
BLOCK = chr(9617)

def displayMaze(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (playerx, playery):
                print(PLAYER, end='')
            elif (x, y) == (exitx, exity):
                print(EXIT, end='')
            elif maze(x, y) == WALL:
                print(BLOCK, end='')
            else:
                print(maze[(x, y)], end='')
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
maze = {}
lines = mazefile.readlines()
playerx = None
playery = None
exitx = None
exity = None
y = 0
for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        maze[(x, y)] = character
        if character in (WALL, EMPTY):
            maze[(x, y)] = character
        elif character == START:
            playerx = x
            playery = y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exitx = x
            exity = y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

assert playerx != None and playery != None, 'No start position found'
assert exitx != None and exity != None, 'No exit found'

while True:
    displayMaze(maze)
    print('Enter W, A, S, D to move or Q to quit')
    move = input().upper()
    if move == 'Q':
        sys.exit()
    if move not in ('W', 'A', 'S', 'D'):
        print('Invalid move')
        continue
    newx = playerx
    newy = playery
    if move == 'W':
        newy -= 1
    elif move == 'S':
        newy += 1
    elif move == 'A':
        newx -= 1
    elif move == 'D':
        newx += 1
    if newx < 0 or newx >= WIDTH or newy < 0 or newy >= HEIGHT:
        print('You cannot move outside the maze')
        continue
    if maze[(newx, newy)] == WALL:
        print('You cannot move through walls')
        continue
    playerx = newx
    playery = newy
    if playerx == exitx and playery == exity:
        print('Congratulations! You have reached the exit')
        break
    maze[(playerx, playery)] = EMPTY
    os.system('cls' if os.name == 'nt' else 'clear')
    print('You have moved to', playerx, playery)

mazefile.close()
sys.exit()
