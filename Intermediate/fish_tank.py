import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you can install by running: pip install bext')
    sys.exit()

WIDTH, HEIGHT = bext.size()
WIDTH -= 1

NUM_KELP = 2
NUM_FISH = 10
NUM_BUBBLES = 1
FRAMES_PER_SECOND = 12

FISH_TYPES = [
    {'right': '><>',
     'left': '<><'},
    {'right': '>>==>',
     'left': '<==<<'},
    {'right': '>>==))>',
     'left': '<<<(==<<'},
    {'right': '°)))彡',
     'left': '°\\\\\\(°°'}
]

LONGEST_FISH_LENGTH = 10
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2

def main():
    global FISHES, BUBBLES, KELPS, BUBBLERS, STEP

    bext.bg('blue')
    bext.clear()

    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append({'x': random.randint(LEFT_EDGE, RIGHT_EDGE),
                       'y': random.randint(TOP_EDGE, BOTTOM_EDGE),
                       'direction': random.choice(['left', 'right']),
                       'type': random.choice(FISH_TYPES)})
    BUBBLES = [{'x': random.randint(LEFT_EDGE, RIGHT_EDGE),
                'y': random.randint(TOP_EDGE, BOTTOM_EDGE)}
               for _ in range(NUM_BUBBLES)]
    KELPS = [{'x': random.randint(LEFT_EDGE, RIGHT_EDGE),
                'length': random.randint(3, 6)}
                 for _ in range(NUM_KELP)]
    BUBBLERS = [{'x': random.randint(LEFT_EDGE, RIGHT_EDGE),
                    'y': random.randint(TOP_EDGE, BOTTOM_EDGE)}
                    for _ in range(NUM_FISH)]
    STEP = 0

    try:
        while True:
            draw()
            move()
            time.sleep(1 / FRAMES_PER_SECOND)
            STEP += 1
    except KeyboardInterrupt:
        sys.exit()

def draw():
    bext.fg('white')
    bext.goto(0, 0)
    bext.clear()

    for kelp in KELPS:
        bext.goto(kelp['x'], BOTTOM_EDGE)
        bext.fg('green')
        bext.bg('green')
        for _ in range(kelp['length']):
            print('W', end='')

    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])
        if fish['direction'] == 'right':
            print(fish['type']['right'], end='')
        else:
            print(fish['type']['left'], end='')

    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print('o', end='')

    for bubbler in BUBBLERS:
        bext.goto(bubbler['x'], bubbler['y'])
        print('O', end='')

    bext.goto(0, HEIGHT - 1)
    bext.fg('white')
    bext.bg('blue')
    print('Press Ctrl-C to quit.', end='')
    bext.bg('blue')
    bext.fg('black')
    print(' ' * (WIDTH - 17), end='')
    bext.goto(0, 0)

def move():
    for fish in FISHES:
        if random.randint(0, 1) == 0:
            fish['y'] += random.randint(-1, 1)
        if fish['direction'] == 'right':
            fish['x'] += 1
            if fish['x'] > RIGHT_EDGE:
                fish['x'] = RIGHT_EDGE
                fish['direction'] = 'left'
        else:
            fish['x'] -= 1
            if fish['x'] < LEFT_EDGE:
                fish['x'] = LEFT_EDGE
                fish['direction'] = 'right'

    for bubble in BUBBLES:
        bubble['y'] -= 1
        if bubble['y'] < TOP_EDGE:
            bubble['y'] = BOTTOM_EDGE

    for bubbler in BUBBLERS:
        if random.randint(0, 1) == 0:
            bubbler['x'] += random.randint(-1, 1)
        if random.randint(0, 1) == 0:
            bubbler['y'] += random.randint(-1, 1)
        if bubbler['x'] < LEFT_EDGE:
            bubbler['x'] = LEFT_EDGE
        if bubbler['x'] > RIGHT_EDGE:
            bubbler['x'] = RIGHT_EDGE
        if bubbler['y'] < TOP_EDGE:
            bubbler['y'] = TOP_EDGE
        if bubbler['y'] > BOTTOM_EDGE:
            bubbler['y'] = BOTTOM_EDGE

if __name__ == '__main__':
    main()
        