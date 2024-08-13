import random

def askForGuess():
    print('I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    while True:
        guess = input()
        if guess.isdecimal():
            guess = int(guess)
        print('Please enter a number between 1 and 100.')

print('Guess the number')
print('I am thinking of a number between 1 and 100.')
print('Take a guess.')
secretNumber = random.randint(1, 100)

for i in range(10):
    print('You have', 10 - i, 'guesses left.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Good job! You guessed my number in', i + 1, 'guesses!')
else:
    print('Nope. The number I was thinking of was', secretNumber)
