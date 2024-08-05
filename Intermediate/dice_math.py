import random, time

DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3

QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6

REWARD = 4
PENALTY = 1

MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)
 
D2a = (['+-------+',
         '| O     |',
         '|       |',
         '|     O |',
         '+-------+'], 2)
 
D2b = (['+-------+',
         '|     O |',
         '|       |',
         '| O     |',
         '+-------+'], 2)
  
D3a = (['+-------+',
         '| O     |',
         '|   O   |',
         '|     O |',
         '+-------+'], 3)
 
D3b = (['+-------+',
         '|     O |',
         '|   O   |',
         '| O     |',
         '+-------+'], 3)
 
D4 = (['+-------+',
        '| O   O |',
        '|       |',
        '| O   O |',
        '+-------+'], 4)
 
D5 = (['+-------+',
        '| O   O |',
        '|   O   |',
        '| O   O |',
        '+-------+'], 5)
  
D6a = (['+-------+',
         '| O   O |',
         '| O   O |',
         '| O   O |',
         '+-------+'], 6)
 
D6b = (['+-------+',
         '| O O O |',
         '|       |',
         '| O O O |',
         '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('Dice Math'
        '\n\nYou have {} seconds to answer as many math problems as you can.'
        '\nCorrect answers earn you {} points, but incorrect answers cost you {} points.'
        '\nPress Ctrl-C to quit.'.format(QUIZ_DURATION, REWARD, PENALTY))

time.sleep(1)

correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()

while time.time() < startTime + QUIZ_DURATION:
    dice = random.choice(ALL_DICE)
    numDice = random.randint(MIN_DICE, MAX_DICE)
    question = '{} {} = '.format(numDice, dice[1])
    answer = input(question)
    if answer == str(numDice * dice[1]):
        print('Correct! You earn {} points.'.format(REWARD))
        correctAnswers += 1
    else:
        print('Incorrect. The correct answer is {}. You lose {} points.'.format(numDice * dice[1], PENALTY))
        incorrectAnswers += 1

endTime = time.time()
print('Time\'s up!')
print('You got {} correct answers and {} incorrect answers.'.format(correctAnswers, incorrectAnswers))
print('Your score is {} points.'.format(correctAnswers * REWARD - incorrectAnswers * PENALTY))
if correctAnswers > 0:
    print('Your average time per question was {:.2f} seconds.'.format((endTime - startTime) / (correctAnswers + incorrectAnswers)))
else:
    print('You didn\'t answer any questions.')
print('Thanks for playing!')

# The Dice Math program is a simple math quiz game that uses ASCII art to display dice. The program randomly selects a die from a list of nine dice and a number of dice to display. The user must then multiply the number of dice by the number on the die and input the answer. The program keeps track of the number of correct and incorrect answers, as well as the time taken to answer each question. At the end of the quiz, the program displays the user's score and average time per question. The program also includes a timer that limits the duration of the quiz.