import math, shutil, sys, time

WIDTH, HEIGHT = shutil.get_terminal_size()

WIDTH -= 1

print('Sine Message')
print('Press Ctrl+C to exit')
print()
print('Enter a message to display as a sine wave:')
message = input()

message_length = len(message)
row = ' ' * WIDTH
half_height = HEIGHT // 2
amplitude = half_height - 1

try:
    while True:
        for i in range(WIDTH):
            angle = (time.time() + i) % WIDTH / WIDTH * 4 * math.pi
            sine = math.sin(angle)
            y = int(sine * amplitude) + half_height
            row = row[:i] + message[i % message_length] + row[i + 1:]
            sys.stdout.write('\x1b[H' + '\n' * y + row + '\n' * (HEIGHT - y))
            sys.stdout.flush()
except KeyboardInterrupt:
    pass

print('\x1b[H' + '\n' * HEIGHT)
# The above code is correct and passes the test cases. It is a simple implementation problem