import random, sys

WIDTH = 60
HEIGHT = 20
NUM_ROBOTS = 5
NUM_TELEPORTS = 5
NUM_DEAD_ROBOTS = 5
NUM_WALLS = 100

EMPTY_SPACE = ' '
PLAYER = '@'
ROBOT = 'R'
DEAD_ROBOT = 'X'

WALL = chr(9608)

def main():
    print('HUNGRY ROBOTS')

    # Create the walls
    walls = set()
    for i in range(NUM_WALLS):
        x = random.randint(1, WIDTH - 2)
        y = random.randint(1, HEIGHT - 2)
        walls.add((x, y))

    # Create the player
    player = {'x': random.randint(1, WIDTH - 2), 'y': random.randint(1, HEIGHT - 2)}

    # Create the robots
    robots = []
    for i in range(NUM_ROBOTS):
        robots.append({'x': random.randint(1, WIDTH - 2), 'y': random.randint(1, HEIGHT - 2)})
    for i in range(NUM_DEAD_ROBOTS):
        robots.append({'x': random.randint(1, WIDTH - 2), 'y': random.randint(1, HEIGHT - 2), 'state': DEAD_ROBOT})

    # Create the teleports
    teleports = []
    for i in range(NUM_TELEPORTS):
        teleports.append({'x': random.randint(1, WIDTH - 2), 'y': random.randint(1, HEIGHT - 2)})
    while True:
        displayGame(player, robots, teleports, walls)
        move = getPlayerMove(player)
        if move == 'QUIT':
            sys.exit()
        if move == 'TELEPORT':
            player = random.choice(teleports)
        else:
            movePlayer(player, move, walls)
            moveRobots(player, robots, walls)
            if player in robots:
                displayGame(player, robots, teleports, walls)
                print('You have been eaten by a robot!')
                sys.exit()
            if player in teleports:
                teleports.remove(player)
                player = random.choice(teleports)
            if len(teleports) == 0:
                displayGame(player, robots, teleports, walls)
                print('You have won!')
                sys.exit()

def displayGame(player, robots, teleports, walls):
    print('HUNGRY ROBOTS')
    print('Find the teleporters before the robots eat you!')
    print('WASD keys move. QUIT to quit. TELEPORT to teleport.')
    print()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == player:
                print(PLAYER, end='')
            elif (x, y) in robots:
                print(ROBOT, end='')
            elif (x, y) in teleports:
                print('*', end='')
            elif (x, y) in walls:
                print(WALL, end='')
            else:
                print(EMPTY_SPACE, end='')
        print()

def getPlayerMove(player):
    while True:
        print('Enter your move:')
        move = input().upper()
        if move in ('W', 'A', 'S', 'D', 'QUIT', 'TELEPORT'):
            return move
        print('Invalid move. Use W, A, S, or D to move, QUIT to quit, or TELEPORT to teleport.')

def movePlayer(player, move, walls):
    x = player['x']
    y = player['y']
    if move == 'W' and (x, y - 1) not in walls:
        player['y'] -= 1
    elif move == 'A' and (x - 1, y) not in walls:
        player['x'] -= 1
    elif move == 'S' and (x, y + 1) not in walls:
        player['y'] += 1
    elif move == 'D' and (x + 1, y) not in walls:
        player['x'] += 1

def moveRobots(player, robots, walls):
    for robot in robots:
        if robot['state'] == DEAD_ROBOT:
            continue
        if random.randint(0, 1) == 0:
            if player['x'] < robot['x'] and (robot['x'] - 1, robot['y']) not in walls:
                robot['x'] -= 1
            elif player['x'] > robot['x'] and (robot['x'] + 1, robot['y']) not in walls:
                robot['x'] += 1
        else:
            if player['y'] < robot['y'] and (robot['x'], robot['y'] - 1) not in walls:
                robot['y'] -= 1
            elif player['y'] > robot['y'] and (robot['x'], robot['y'] + 1) not in walls:
                robot['y'] += 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
        