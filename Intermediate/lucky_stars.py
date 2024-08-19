import random

GOLD = 'GOLD'
SILVER = 'SILVER'
BRONZE = 'BRONZE'

STAR_FACE = [
    '+-----------------+',
    '|         .       |',
    '|    .   . .      |',
    '|   . . . . .     |',
    '|    . . . .      |',
    '|      . .        |',
    '|       .         |',
    '|                 |',
    '|                 |',
    '|                 |',
    '+-----------------+',
]

SKULL_FACE = [
    '+-----------------+',
    '|    . .    .     |',
    '|   .   . .  .    |',
    '|  . . . . . .   |',
    '|   . . . . .    |',
    '|    . . . .     |',
    '|     . . .      |',
    '|      . .       |',
    '|                 |',
    '|                 |',
    '+-----------------+',
]

QUESTION_FACE = [
    '+-----------------+',
    '|                 |',
    '|                 |',
    '|                 |',
    '|                 |',
    '|                 |',
    '|                 |',
    '|                 |',
    '|                 |',
    '|                 |',
    '+-----------------+',
]

def printFace(face):
    for line in face:
        print(line)

def printLuckyStar():
    print("Lucky Star:")
    printFace(STAR_FACE)
    print()

def printUnluckyStar():
    print("Unlucky Star:")
    printFace(SKULL_FACE)
    print()

def printQuestionStar():
    print("Question Star:")
    printFace(QUESTION_FACE)
    print()

def main():
    print("Enter the number of stars to draw:")
    numberOfStars = int(input())

    for i in range(numberOfStars):
        face = random.choice([STAR_FACE, SKULL_FACE, QUESTION_FACE])
        if face == STAR_FACE:
            printLuckyStar()
        elif face == SKULL_FACE:
            printUnluckyStar()
        elif face == QUESTION_FACE:
            printQuestionStar()

if __name__ == '__main__':
    main()
# This program randomly draws a lucky star, unlucky star, or question mark star. The faces of the stars are drawn using ASCII art. The program asks the user how many stars to draw and then draws that many stars.