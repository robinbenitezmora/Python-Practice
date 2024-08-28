'''
Powerball lottery is a game where 6 numbers are drawn from a pool of 49 numbers. Players can purchase a ticket with 6 numbers for $2. If the ticket matches 2 numbers, the player wins $5. If the ticket matches 3 numbers, the player wins $100. If the ticket matches 4 numbers, the player wins $50,000. If the ticket matches 5 numbers, the player wins $1,000,000. If the ticket matches all 6 numbers, the player wins $10,000,000. Write a program that generates a ticket and then randomly draws 6 numbers. The program should then output the prize amount.
'''

import random

print('Powerball Lottery')

while True:
    ticket = set(random.sample(range(1, 50), 6))
    winning_numbers = set(random.sample(range(1, 50), 6))
    print(f'Ticket: {ticket}')
    print(f'Winning Numbers: {winning_numbers}')
    matches = ticket.intersection(winning_numbers)
    print(f'Matches: {matches}')
    if len(matches) == 2:
        print('You won $5')
    elif len(matches) == 3:
        print('You won $100')
    elif len(matches) == 4:
        print('You won $50,000')
    elif len(matches) == 5:
        print('You won $1,000,000')
    elif len(matches) == 6:
        print('You won $10,000,000')
    else:
        print('You did not win anything')
    print()
    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() != 'yes':
        break
print('Thanks for playing')
