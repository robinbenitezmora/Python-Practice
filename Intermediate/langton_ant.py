import copy, random, sys, time

try:
    import bext
except ImportError:
    print("This program requires the bext module.")
    print("You can install it by running: pip install bext")
    print("Exiting...")
    sys.exit()

WIDTH, HEIGHT = bext.size()
WIDTH -= 1
HEIGHT -= 1

NUMBER_OF_ANTS = 10
PAUSE_AMOUNT = 0.1

ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'

ANT_COLOR = 'red'
BLACK_TILE = 'black'
WHITE_TILE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

DIRECTIONS = (NORTH, EAST, SOUTH, WEST)
RIGHT_TURNS = {NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH}
LEFT_TURNS = {NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH}

# Create the board data structure.
board = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            board[(x, y)] = BLACK_TILE
        else:
            board[(x, y)] = WHITE_TILE

# Create the ants.
ants = []
for i in range(NUMBER_OF_ANTS):
    ant = {'x': random.randint(0, WIDTH - 1),
           'y': random.randint(0, HEIGHT - 1),
           'direction': random.choice(DIRECTIONS)}
    ants.append(ant)

while True:
    bext.clear()

    # Draw the board.
    for y in range(HEIGHT):
        for x in range(WIDTH):
            bext.goto(x, y)
            if board[(x, y)] == BLACK_TILE:
                print(' ', end='')
            else:
                print(' ', end='')

    # Move the ants.
    for ant in ants:
        if board[(ant['x'], ant['y'])] == WHITE_TILE:
            board[(ant['x'], ant['y'])] = BLACK_TILE
            if ant['direction'] in (NORTH, SOUTH):
                ant['direction'] = random.choice((EAST, WEST))
            else:
                ant['direction'] = random.choice((NORTH, SOUTH))
        else:
            board[(ant['x'], ant['y'])] = WHITE_TILE
            if ant['direction'] in (NORTH, SOUTH):
                ant['direction'] = random.choice((NORTH, SOUTH))
            else:
                ant['direction'] = random.choice((EAST, WEST))

        if ant['direction'] == NORTH:
            ant['y'] -= 1
            if ant['y'] < 0:
                ant['y'] = HEIGHT - 1
        elif ant['direction'] == SOUTH:
            ant['y'] += 1
            if ant['y'] == HEIGHT:
                ant['y'] = 0
        elif ant['direction'] == WEST:
            ant['x'] -= 1
            if ant['x'] < 0:
                ant['x'] = WIDTH - 1
        elif ant['direction'] == EAST:
            ant['x'] += 1
            if ant['x'] == WIDTH:
                ant['x'] = 0

        bext.goto(ant['x'], ant['y'])
        bext.fg(ANT_COLOR)
        if ant['direction'] == NORTH:
            print(ANT_UP, end='')
        elif ant['direction'] == SOUTH:
            print(ANT_DOWN, end='')
        elif ant['direction'] == WEST:
            print(ANT_LEFT, end='')
        elif ant['direction'] == EAST:
            print(ANT_RIGHT, end='')

    bext.goto(0, 0)
    sys.stdout.flush()
    time.sleep(PAUSE_AMOUNT)
