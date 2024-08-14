import random, sys

HANGMANPICS = [r'''
    +---+
        |
        |
        |
         ===''', r'''
    +---+
    O   |
        |
        |
         ===''', r'''
    +---+
    O   |
    |   |
        |
         ===''', r'''
    +---+
    O   |
     /|   |
        |
         ===''', r'''
    +---+
    O   |
     /|\  |
        |
         ===''', r'''
    +---+
    O   |
     /|\  |
     /    |
         ===''', r'''
    +---+
    O   |
     /|\  |
     / \  |
         ===''']

CATEGORY = 'ANIMALS'
WORDS = '''ALLIGATOR BEAR CAT DOG ELEPHANT FROG GIRAFFE HORSE IGUANA JAGUAR KANGAROO LION MONKEY NEWT OSTRICH PENGUIN QUAIL RABBIT SNAKE TURTLE URCHIN VULTURE WOLF XERUS YAK ZEBRA'''.split()

for i in range(len(WORDS)):
    WORDS[i] = WORDS[i].strip().upper()

def getWord():
    return random.choice(WORDS)

def displayBoard(board):
    print(HANGMANPICS[len(board) - 1])
    print(' '.join(board))

def getGuess():
    while True:
        print('Guess a letter.')
        guess = input().upper()
        if len(guess) != 1:
            print('Your guess must be a single letter.')
        elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print('Your guess must be a letter.')
        else:
            return guess
        
def getClues(word, board, guess):
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                board[i] = guess
    else:
        return False
    return True

def main():
    print('HANGMAN MINIGAME')
    print('You have seven guesses to guess the word.')
    print('The category is', CATEGORY)
    print()

    word = getWord()
    board = ['*' for i in range(len(word))]
    missedLetters = ''
    correctLetters = ''
    gameIsDone = False

    while True:
        displayBoard(board)
        print('Missed letters:', missedLetters)
        print('Correct letters:', correctLetters)
        guess = getGuess()

        if guess in missedLetters or guess in correctLetters:
            print('You have already guessed that letter.')
        elif getClues(word, board, guess):
            correctLetters += guess
            foundAllLetters = True
            for i in range(len(word)):
                if board[i] == '*':
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is', word)
                print('You have won!')
                gameIsDone = True
        else:
            missedLetters += guess
            if len(missedLetters) == len(HANGMANPICS) - 1:
                displayBoard(board)
                print('You have run out of guesses!')
                print('The word was', word)
                gameIsDone = True

        if gameIsDone:
            print('Do you want to play again? (yes or no)')
            if not input().lower().startswith('y'):
                break

if __name__ == '__main__':
    main()
    