import random
from game_data import data
from art import *
from replit import clear
from google.colab import output

def assign():
    return random.choice(data)

def play_higher_lower():
    print(logo)
    score = 0
    game_over = False
    while not game_over:
        account_a = assign()
        account_b = assign()
        while account_a == account_b:
            account_b = assign()
        print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
        print(vs)
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
        guess = input('Who has more followers? Type "A" or "B": ').lower()
        if account_a['follower_count'] > account_b['follower_count']:
            correct_answer = 'a'
        else:
            correct_answer = 'b'
        if guess == correct_answer:
            score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {score}.")
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_over = True

def compare(p1, p2, user_input):
    sum1 = p1['follower_count']
    sum2 = p2['follower_count']

    max = ''

    if sum1 > sum2:
        max = p1['name']
    elif sum1 < sum2:
        max = p2['name']

    if max == user_input:
        return True
    else:
        return False

want_to_play = input('Do you want to play the Higher Lower game? (yes/no): ').lower()
if want_to_play == 'yes':
    clear()
    play_higher_lower()
elif want_to_play == 'no':
    print('Okay, see you next time!')
else:
    print('Invalid input. Please try again.')







