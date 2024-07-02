'''
How to play Rock-Paper-Scissors game:
1. Enter your choice (Rock, Paper, or Scissors)
2. The computer will randomly select a choice
3. The winner is decided based on the following rules:
    - Rock beats Scissors
    - Scissors beats Paper
    - Paper beats Rock
'''

import random

def play_game(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'It\'s a tie!'
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper') or \
         (player_choice == 'Paper' and computer_choice == 'Rock'):
        return 'You win!'
    else:
        return 'You lose!'
    
def main():
    choices = ['Rock', 'Paper', 'Scissors']
    player_choice = input('Enter your choice (Rock/Paper/Scissors):\n')
    computer_choice = random.choice(choices)
    print(f'Computer choice: {computer_choice}')
    result = play_game(player_choice, computer_choice)
    print(result)

if __name__ == '__main__':
    main()
    