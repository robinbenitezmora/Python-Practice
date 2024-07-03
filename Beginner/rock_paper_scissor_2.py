import random

user_wins = 0
computer_wins = 0

while True:
    print('Welcome to rock, paper, scissors!')
    user_choice = input('Choose rock, paper, or scissors: ').lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print('Please choose a valid option.')
        continue

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print('Computer chose:', computer_choice)

    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('You win!')
        user_wins += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('You win!')
        user_wins += 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('You win!')
        user_wins += 1
    else:
        print('Computer wins!')
        computer_wins += 1

    print('You:', user_wins, 'Computer:', computer_wins)

    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again != 'yes':
        break

print('Thanks for playing!')
