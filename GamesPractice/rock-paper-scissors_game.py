def player():
    answer = int(input('\nEnter your choice: 1 for rock, 2 for paper, and 3 for scissors: \n'))
    if answer == 1:
        answer = 'rock'
    elif answer == 2:
        answer = 'paper'
    elif answer == 3:
        answer = 'scissors'
    else:
        print('Invalid input')
    return answer

def computer():
    import random
    options = ['rock', 'paper', 'scissors']
    answer = random.choice(options)
    return answer

def compare(player, computer):
    winner = None
    if player == computer:
        winner = 'It is a tie'
    elif player == 'rock':
        if computer == 'scissors':
            winner = 'Player wins'
        else:
            winner = 'Computer wins'
    elif player == 'paper':
        if computer == 'rock':
            winner = 'Player wins'
        else:
            winner = 'Computer wins'
    elif player == 'scissors':
        if computer == 'paper':
            winner = 'Player wins'
        else:
            winner = 'Computer wins'
    else:
        winner = 'Invalid input'
    return winner

name = input('What is your name?:\n')
print(f'Hello {name}, welcome to the rock-paper-scissors game. We are going to bit ten times to check who wins more points')

player_score = 0
computer_score = 0
ties = 0

for i in range(10):
    player_choice = player()
    computer_choice = computer()
    print(f'Player choice: {player_choice}')
    print(f'Computer choice: {computer_choice}')
    result = compare(player_choice, computer_choice)
    print(result)
    if result == 'Player wins':
        player_score += 1
    elif result == 'Computer wins':
        computer_score += 1
    else:
        ties += 1

print(f'Player score: {player_score}\n')
print(f'Computer score: {computer_score}\n')
print(f'Ties: {ties}\n')

if player_score > computer_score:
    print('Player wins the game')
elif player_score < computer_score:
    print('Computer wins the game')
else:
    print('It is a tie')

print('Game over')
    