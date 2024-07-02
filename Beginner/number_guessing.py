import random
import math

def main():
    lower = 0
    upper = 0
    x = 0
    guess = 0
    count = 0
    flag = 0
    total_chances = 0

    print("Enter the lower bound: ")
    lower = int(input())

    print("Enter the upper bound: ")
    upper = int(input())

    random.seed()

    x = random.randint(lower, upper)
    total_chances = math.ceil(math.log(upper - lower + 1) / math.log(2))

    print('\nYou have only', total_chances, 'chances to guess the number\n')

    while count < total_chances:
        count += 1

        print('Guess the number: ')
        guess = int(input())

        if x == guess:
            print('Congratulations! You have guessed the number in', count, 'attempts\n')
            flag = 1
            break
        elif x < guess:
            print('The number is smaller than', guess, '\n')
        else:
            print('The number is greater than', guess, '\n')

    if not flag:
        print('\nThe number is', x, '\n')
        print('Better luck next time\n')

    return 0
    