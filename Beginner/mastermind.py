'''
Rules of the game:
1. The computer will think of 4 digit number that has no repeating digits.
2. You will then guess a 4 digit number
3. The computer will then give back clues, the possible clues are:
    - Close: You've guessed a correct number but in the wrong position
    - Match: You've guessed a correct number in the correct position
    - Nope: You haven't guess any of the numbers correctly
4. Based on these clues you will guess again until you break the code with a
    perfect match, the game will report "CODE CRACKED"!
    '''

import random

num = random.randrange(1000, 10000)
n = int(input('Enter a 4 digit number:\n'))

if n == num:
    print('Great! Youd guessed the number in the first attempt! You are a Mastermind!')
else:
    ctr = 0

    while n != num:
        ctr += 1
        count = 0
        n = str(n)
        num = str(num)

        correct = ['Match'] * 4
        for i in range(0, 4):
            if n[i] == num[i]:
                count += 1
                correct[i] = 'Close'
            else:
                correct[i] = 'Nope'

        print(''.join(correct))
        n = int(input('Enter a 4 digit number:\n'))

    if n == num:
        print('Great! You guessed the number in', ctr, 'attempts! You are a Mastermind!')
    else:
        print('Sorry! You are not a Mastermind! The number was', num)
