import random
import sys

JAPENESE_NUMBERS = {
    '1': 'Ichi',
    '2': 'Ni',
    '3': 'San',
    '4': 'Shi',
    '5': 'Go',
    '6': 'Roku',
    '7': 'Shichi',
    '8': 'Hachi',
    '9': 'Kyuu',
    '0': 'Zero'
}

print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)')
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads += 1
    flips += 1

    if flips == 900:
        print('900 flips and there have been {} heads.'.format(heads))
    if flips == 100:
        print('At 100 tosses, heads has come up {} times so far.'.format(heads))
    if flips == 500:
        print('Halfway done, and heads has come up {} times.'.format(heads))

print()
print('Out of 1000 coin tosses, heads came up {} times!'.format(heads))
print('Were you close?')

print('Japanese Numbers:')
for i in range(10):
    print(JAPENESE_NUMBERS[str(i)])

sys.exit()

# Compare this snippet from Intermediate/cho_han.py:
#     sys.exit()
#
# WIDTH, HEIGHT = bext.size()

# Compare this snippet from Intermediate/carrot_in_a_box.py:
#     sys.exit()
