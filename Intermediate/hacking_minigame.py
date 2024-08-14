import random, sys

GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

with open('sevenletterswords.txt') as wordListFile:
    WORDS = wordListFile.readlines()

for i in range(len(WORDS)):
    WORDS[i] = WORDS[i].strip().upper()

def getWord():
    return random.choice(WORDS)

def displayBoard(board):
    print(' '.join(board))

def getGuess():
    while True:
        print('Guess a seven-letter word.')
        guess = input().upper()
        if len(guess) != 7:
            print('Your guess must be seven letters long.')
        elif guess not in WORDS:
            print('That is not a valid word.')
        else:
            return guess
        
def getClues(word, guess):
    clues = []
    for i in range(7):
        if guess[i] == word[i]:
            clues.append('X')
        elif guess[i] in word:
            clues.append('O')
        else:
            clues.append('-')
    random.shuffle(clues)
    return clues

def main():
    print('HACKING MINIGAME')
    print('You have seven guesses to guess a seven-letter word.')
    print('After each guess, you will receive clues.')
    print('X means a correct letter in the correct position.')
    print('O means a correct letter in the wrong position.')
    print('- means a letter is not in the word at all.')
    print()

    word = getWord()
    board = ['*' for i in range(7)]

    for i in range(7):
        displayBoard(board)
        guess = getGuess()
        clues = getClues(word, guess)

        if guess == word:
            print('You have correctly guessed the word!')
            print('The word was', word)
            sys.exit()
        else:
            print('Clues:')
            displayBoard(clues)
            print()

    print('You have run out of guesses.')
    print('The word was', word)

if __name__ == '__main__':
    main()
