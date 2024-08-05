'''
Draws diamonds of different sizes.
'''

def main():
    print('Diamonds of different sizes:')

    for diamondSize in range(0, 6):
        displayOutlineDiamond(diamondSize)
        print()
        displayFilledDiamond(diamondSize)
        print()

def displayOutlineDiamond(size):
    for i in range(size):
        print(' ' * (size - i - 1) + '*' + ' ' * (i * 2) + '*')
    for i in range(size - 2, -1, -1):
        print(' ' * (size - i - 1) + '*' + ' ' * (i * 2) + '*')

def displayFilledDiamond(size):
    print(' ' * (size) + '*')
    for i in range(1, size):
        print(' ' * (size - i) + '*' + ' ' * (i * 2 - 1) + '*')
    for i in range(size - 2, 0, -1):
        print(' ' * (size - i) + '*' + ' ' * (i * 2 - 1) + '*')
    print(' ' * (size) + '*')

if __name__ == '__main__':
    main()
# The diamonds.py program draws diamonds of different sizes. The displayOutlineDiamond() function draws an outline of a diamond of the given size, and the displayFilledDiamond() function draws a filled diamond of the given size. The main() function displays diamonds of sizes 0 through 5 using these functions.