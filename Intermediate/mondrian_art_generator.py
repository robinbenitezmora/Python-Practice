import sys, random

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you can install by running pip install bext from the command line.')
    sys.exit()

MIN_X_INCREASE = 5
MAX_X_INCREASE = 20
MIN_Y_INCREASE = 5
MAX_Y_INCREASE = 20
WHITE = 'white'
BLACK = 'black'
RED = 'red'
YELLOW = 'yellow'
BLUE = 'blue'

width, height = bext.size()
width -= 1  # Adjust for the border
height -= 3  # Adjust for the border

while True:
    canvas = {}
    for x in range(width):
        for y in range(height):
            canvas[(x, y)] = WHITE

    numberOfSegmentsToDelete = 0
    x = random.randint(MIN_X_INCREASE, MAX_X_INCREASE)
    while x < widht - MIN_X_INCREASE:
        numberOfSegmentsToDelete += 1
        for y in range(height):
            canvas[(x, y)] = BLACK
        x += random.randint(MIN_X_INCREASE, MAX_X_INCREASE)

    y = random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)
    while y < height - MIN_Y_INCREASE:
        numberOfSegmentsToDelete += 1
        for x in range(width):
            canvas[(x, y)] = BLACK
        y += random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)

    numberOfRectanglesToPaint = numberOfSegmentsToDelete - 3
    numberOfSegmentsToDelete = int(numberOfSegmentsToDelete * 1.5)

    for i in range(numberOfSegmentsToDelete):
        while True:
            startx = random.randint(1, width - 2)
            starty = random.randint(1, height - 2)
            if canvas[(startx, starty)] == WHITE:
                continue
            if canvas[(startx + 1, starty)] == WHITE and canvas[(startx - 1, starty)] == WHITE:
                orientation = 'vertical'
            elif canvas[(startx, starty + 1)] == WHITE and canvas[(startx, starty - 1)] == WHITE:
                orientation = 'horizontal'
            else:
                continue

            pointsToDelete = [(startx, starty)]

            canDeleteSegment = True
            if orientation == 'vertical':
                for y in range(starty + 1, height - 1):
                    if canvas[(startx, y)] == BLACK:
                        break
                    pointsToDelete.append((startx, y))
                else:
                    canDeleteSegment = False
            else:
                for x in range(startx + 1, width - 1):
                    if canvas[(x, starty)] == BLACK:
                        break
                    pointsToDelete.append((x, starty))
                else:
                    canDeleteSegment = False

            if canDeleteSegment:
                break

        for x, y in pointsToDelete:
            canvas[(x, y)] = WHITE

    for i in range(numberOfRectanglesToPaint):
        while True:
            left = random.randint(1, width - 2)
            top = random.randint(1, height - 2)
            right = random.randint(left + 1, width - 1)
            bottom = random.randint(top + 1, height - 1)
            if canvas[(left, top)] == WHITE and canvas[(right, top)] == WHITE and canvas[(left, bottom)] == WHITE and canvas[(right, bottom)] == WHITE:
                break

        for x in range(left, right + 1):
            canvas[(x, top)] = RED
            canvas[(x, bottom)] = RED
        for y in range(top, bottom + 1):
            canvas[(left, y)] = RED
            canvas[(right, y)] = RED

    for x in range(width):
        for y in range(height):
            if canvas[(x, y)] == WHITE:
                bext.fg(WHITE)
            elif canvas[(x, y)] == BLACK:
                bext.fg(BLACK)
            elif canvas[(x, y)] == RED:
                bext.fg(RED)
            print(BLOCK, end='')
        print()
    bext.fg(WHITE)

    print('Press Ctrl-C to stop, or Enter to generate a new picture.')
    try:
        input()
    except KeyboardInterrupt:
        sys.exit()
