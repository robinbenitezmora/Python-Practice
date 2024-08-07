import random, shutil, sys, time

PAUSE = 0.15
DENSITY = 0.10

DUCKLING_WIDTH = 10
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

DUCKLING = {
    'head': {
        'left': {
            'beady': '   .-.',
            'wide': '  .-.'
        },
        'right': {
            'beady': '.-.   ',
            'wide': '.-.  '
        }
    },
    'body': {
        'happy': {
            'left': ' (o o)',
            'right': '( o o)'
        },
        'aloof': {
            'left': ' (o o)',
            'right': '( o o)'
        },
        'chubby': {
            'left': ' (o o)',
            'right': '( o o)'
        },
        'very chubby': {
            'left': ' (o o)',
            'right': '( o o)'
        }
    },
    'feet': {
        'open': {
            'left': '  J J',
            'right': 'J J  '
        },
        'closed': {
            'left': '  " "',
            'right': '" "  '
        }
    }
}

try:
    print('Duckling Animation, press Ctrl-C to quit...')
    print('Press Ctrl-C to quit.')
    time.sleep(2)
    rowIndex = 0

    while True:
        rowIndex += 1
        if rowIndex == len(ROWS):
            rowIndex = 0

        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue

        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            print(ROWS[rowIndex].format('A', 'T'))
        elif randomSelection == 2:
            print(ROWS[rowIndex].format('T', 'A'))
        elif randomSelection == 3:
            print(ROWS[rowIndex].format('C', 'G'))
        elif randomSelection == 4:
            print(ROWS[rowIndex].format('G', 'C'))

        leftNucleoitide = 'A'
        rightNucleoitide = 'T'
        print(ROWS[rowIndex].format(leftNucleoitide, rightNucleoitide))
        time.sleep(PAUSE)
except KeyboardInterrupt:
    print('DNA Animation, stopped.')
    sys.exit()
# The Duckling Animation program is a simple program that displays a duckling animation. The program uses the shutil module to get the width of the terminal window. The program then prints the duckling animation to the terminal window and updates the animation every 0.15 seconds. The user can press Ctrl-C to quit the program.
