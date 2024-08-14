import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you can install by running pip install bext from the command line.')
    sys.exit()

PAUSE_LENGTH = 0.5
WIDE_FALL_CHANCE = 50   

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 20

X = 0
Y = 1
SAND = chr(9617)
WALL = chr(9608)

HOURGLASS = set()
for x in range(3, 8):
    HOURGLASS.add((x, 3))
    HOURGLASS.add((x, 7))
for y in range(4, 7):
    HOURGLASS.add((3, y))
    HOURGLASS.add((7, y))

def main():
    bext.clear()
    bext.set_title('Hourglass')

    sandClock = set()
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_HEIGHT):
            sandClock.add((x, y))

    while True:
        displaySandClock(sandClock)
        time.sleep(PAUSE_LENGTH)

        if random.randint(1, 100) <= WIDE_FALL_CHANCE:
            sandClock = wideFall(sandClock)
        else:
            sandClock = narrowFall(sandClock)

        if sandClock == HOURGLASS:
            break

    bext.clear()
    print('The hourglass is complete and time has run out!')

def displaySandClock(sandClock):
    bext.goto(0, 0)
    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            if (x, y) in sandClock:
                print(SAND, end='')
            else:
                print(WALL, end='')
        print()

def narrowFall(sandClock):
    nextSandClock = set()
    for x, y in sandClock:
        if (x, y + 1) in sandClock or (x, y + 1) == (x, SCREEN_HEIGHT - 1):
            nextSandClock.add((x, y))
        else:
            nextSandClock.add((x, y + 1))
    return nextSandClock

def wideFall(sandClock):
    nextSandClock = set()
    for x, y in sandClock:
        if (x, y + 1) in sandClock or (x, y + 1) == (x, SCREEN_HEIGHT - 1):
            nextSandClock.add((x, y))
        else:
            nextSandClock.add((x, y + 1))

        if x != 0 and (x - 1, y) not in sandClock:
            nextSandClock.add((x - 1, y))
        if x != SCREEN_WIDTH - 1 and (x + 1, y) not in sandClock:
            nextSandClock.add((x + 1, y))

    return nextSandClock

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
