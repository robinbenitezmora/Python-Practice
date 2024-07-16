logo = """
  _    _ _       _                 _                            
 | |  | (_)     | |               | |                           
 | |__| |_  __ _| |__   ___ _ __  | |     _____      _____ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__| | |    / _ \ \ /\ / / _ \ '__|
 | |  | | | (_| | | | |  __/ |    | |___| (_) \ V  V /  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|    |______\___/ \_/\_/ \___|_|   
            __/ |                                               
           |___/                                                
"""
 
 
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brazil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 131,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 127,
        'description': 'Reality TV personality and model',
        'country': 'United States'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 119,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Nicki Minaj',
        'follower_count': 113,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 108,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 107,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 94,
        'description': 'Musician',
        'country': 'United States'
    },
]

import random
from Beginner.higher_lower import play_higher_lower
from art import logo, vs
from replit import clear

def assign():
    return random.choice(data)

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
    
    def play_higher_lower():
        playing_game = True

        while playing_game:
            clear()
            print(logo)

            score = 0

            person1 = assign()
            person2 = assign()

            if score > 0:
                person1 = person2
                person2 = assign()

                if person1 == person2:
                    person2 = assign()

            print(f'Name: {person1['name']}, Description: {person1['description']})')
            print(vs)

            print(f'Name: {person2['name']}, Description: {person2['description']})')

            print('---------------------------------------------------')
            print('Your current score is: ' + str(score))
            print('---------------------------------------------------')

            guess = input(f'Enter name of person with Higher Followers: ')

            if compare(person1, person2, guess):
                score += 1
            else
                still_guessing = False

        play_again = input('Do you want to play again? (yes/no): ').lower()

        if play_again == 'no':
            playing_game = False
            print('Thanks for playing!')
        else:
            playing_game = True

play_higher_lower()
