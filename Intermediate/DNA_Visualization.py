'''
DNA is a simple animation program that displays a DNA strand that is rotating. The program uses the turtle module to draw the DNA strand and the time module to control the speed of the rotation. The program creates a turtle object and sets the speed to 0. The program then creates a list of colors for the DNA strand and sets the initial angle of the rotation. The program then enters a loop that rotates the DNA strand by a small angle and updates the display. The user can press Ctrl-C to quit the program.
'''

import random, sys, time

PAUSE = 0.15

ROWS = [
    #123456789 <- Use this to measure the number of spaces:
'         ##',  # Index 0 has no {}.
'        #{}-{}#',
'       #{}---{}#',
'      #{}-----{}#',
'     #{}------{}#',
'    #{}------{}#',
'    #{}-----{}#',
'     #{}---{}#',
'     #{}-{}#',
'      ##',  # Index 9 has no {}.
'     #{}-{}#',
'     #{}---{}#',
'    #{}-----{}#',
'    #{}------{}#',
'     #{}------{}#',
'      #{}-----{}#',
'       #{}---{}#',
'        #{}-{}#']
#123456789 <- Use this to measure the number of spaces:

try:
    print('DNA Animation, press Ctrl-C to quit...')
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

