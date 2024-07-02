import random
from collections import Counter

some_words = '''apple banana cherry date elderberry fig grapefruit honeydew kiwi lemon mango nectarine orange papaya quince raspberry strawberry tangerine ugli fruit vanilla watermelon ximenia citron yuzu zucchini'''.split()

word = random.choice(some_words)

if __name__ == '__main__':
    print('Welcome to Hangman!')
    print('The word contains', len(word), 'letters.')
    print('You have 6 chances to guess the word.\n')

    guessed = ['_'] * len(word)
    guessed_word = ''.join(guessed)
    chances = 6

    while chances > 0:
        print('Word:', guessed_word)
        print('Chances:', chances)
        letter = input('Enter a letter: ')

        if letter in word:
            for i, c in enumerate(word):
                if c == letter:
                    guessed[i] = letter
            guessed_word = ''.join(guessed)
        else:
            chances -= 1

        if guessed_word == word:
            print('Congratulations! You have guessed the word:', word)
            break

    if chances == 0:
        print('The word was:', word)
        print('Better luck next time!')
