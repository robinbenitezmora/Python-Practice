'''
Rainbow is a simple Python program that generates a rainbow on the terminal. It uses the colorama library to print colored text on the terminal. The program prints a rainbow on the terminal by printing colored text in a loop. The colors of the rainbow are red, orange, yellow, green, blue, indigo, and violet. The program prints the rainbow by printing the colors in a loop. The program uses the colorama library to print colored text on the terminal
'''

import time, sys

try:
    import bext
except ImportError:
    print('bext module is not installed. Install it using pip install bext')
    sys.exit()

print('Rainbow')
print('Press Ctrl-C to exit')
time.sleep(1)

indent = 0
indent_increasing = True

try:
    while True:
        print(' ' * indent, end='')
        bext.fg('red')
        print('R', end='')
        bext.fg('reset')
        bext.fg('yellow')
        print('a', end='')
        bext.fg('reset')
        bext.fg('green')
        print('i', end='')
        bext.fg('reset')
        bext.fg('blue')
        print('n', end='')
        bext.fg('reset')
        bext.fg('cyan')
        print('b', end='')
        bext.fg('reset')
        bext.fg('magenta')
        print('o', end='')
        bext.fg('reset')
        bext.fg('red')
        print('w', end='')
        bext.fg('reset')
        time.sleep(0.1)

        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
    