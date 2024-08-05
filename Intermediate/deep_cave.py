import random, sys, time

WIDTH = 60
PAUSE_AMOUNT = 0.05

print('Deep Cave')
print('---------')
print('You are in a deep cave. You have one minute to find the treasure.')
print('Try to get out of the cave before the cave collapses!')
print()
time.sleep(2)

leftWidth = 20
rightWidth = 10

while True:
    leftWidth += random.randint(-1, 1)
    rightWidth += random.randint(-1, 1)

    if leftWidth < 10:
        leftWidth = 10
    if leftWidth > 30:
        leftWidth = 30
    if rightWidth < 2:
        rightWidth = 2
    if rightWidth > 20:
        rightWidth = 20

    print(('=' * leftWidth) + (' ' * (WIDTH - leftWidth - rightWidth)) + ('=' * rightWidth))
    time.sleep(PAUSE_AMOUNT)

    if leftWidth == 10 and rightWidth == 20:
        print('You escaped!')
        sys.exit()
    elif leftWidth == 30 and rightWidth == 2:
        print('You were squished by the cave!')
        sys.exit()

# The deep_cave.py program is a game where the player tries to escape from a cave before it collapses. The cave is represented by a line of equal signs, and the player can move to the left or right by changing the width of the left and right sides of the cave. The player wins if the left side is 10 characters wide and the right side is 20 characters wide, and loses if the left side is 30 characters wide and the right side is 2 characters wide. The width of the sides of the cave randomly changes by 1 character each turn, and the game pauses for a short amount of time between each turn. The game continues until the player wins or loses.