import random

def getDigits(num):
    return [int(d) for d in str(num)]

def noDuplicates(num):
    numList = getDigits(num)
    
    if len(numList) == len(set(numList)):
        return True
    else:
        return False
    
def generateNumber():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num
        
def numOfBullsCows(num, guess):
    bull_cow = [0, 0]
    numList = getDigits(num)
    guessList = getDigits(guess)

    for i, j in zip(numList, guessList):
        if j in numList:
            if i == j:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1

    return bull_cow

num = generateNumber()
tries = int(input("Enter number of tries: "))

while tries > 0:
    guess = int(input('Enter your guess: '))

    if not noDuplicates(guess):
        print("Number should not have duplicate digits.")
        continue

    if guess < 1000 or guess > 9999:
        print("Number should be 4 digits long.")
        continue

    bulls_cows = numOfBullsCows(num, guess)
    print(f'Bulls: {bulls_cows[0]}, Cows: {bulls_cows[1]}')

    tries -= 1

    if bulls_cows[0] == 4:
        print("You won!")
        break
else:
    print(f'You lost! The number was {num}.')
# This code snippet is a simple implementation of the Cows and Bulls game in Python. The game generates a random 4-digit number with no duplicate digits, and the player has a limited number of tries to guess the number. The player enters their guess, and the program calculates the number of bulls (correct digits in the correct position) and cows (correct digits in the wrong position) in the guess. The game continues until the player correctly guesses the number or runs out of tries. The player wins if they guess the number correctly within the given number of tries, and loses if they do not. The game provides feedback on the number of bulls and cows in each guess to help the player refine their guesses. The game is a fun and challenging way to test the player's logic and deduction skills.