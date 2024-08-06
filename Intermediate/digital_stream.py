import random, sys, shutil, time

MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE_AMOUNT = 0.1
STREAM_CHARS = ['0', '1']

DENSITY = 0.2

WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

print('Digital Stream')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    while True:
        columns = [0] * WIDTH
        while True:
            for i in range(WIDTH):
                if columns[i] == 0:
                    if random.random() < DENSITY:
                        columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
                else:
                    print(random.choice(STREAM_CHARS), end='')
                    columns[i] -= 1
            print()
            time.sleep(PAUSE_AMOUNT)
except KeyboardInterrupt:
    print('Digital Stream, stopped.')
    sys.exit()

# The Digital Stream program is a simple program that displays a digital stream of characters on the terminal. The program generates random streams of characters that move down the screen. The user can press Ctrl-C to quit the program. The program uses the shutil module to get the terminal width and the time module to control the speed of the stream. The program also uses the random module to generate random streams of characters.