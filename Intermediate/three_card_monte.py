import __main__
import random, time

NUM_SWAPS = 16
DELAY = 0.5

HEARTS = chr(9829)
DIAMONDS = chr(9830)
CLUBS = chr(9827)
SPADES = chr(9824)

LEFT = 0
MIDDLE = 1
RIGHT = 2

def displayCards(cards):
    '''Display the cards in the list'''
    print(" " * 40, end="")
    rows = ['', '', '', '', '']
    for i, card in enumerate(cards):
        rows[0] += " ___  "
        rows[1] += f"|{card[0]} | "
        rows[2] += f"| {card[1]} | "
        rows[3] += f"| {card[2]}| "
        rows[4] += " ---  "
    for row in rows:
        print(row)

def getRandomCard():
    '''Return a random card from the deck'''
    suits = [HEARTS, DIAMONDS, CLUBS, SPADES]
    faceValues = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return [random.choice(faceValues), random.choice(suits)]

def getCardName(card):
    '''Return the name of the card'''
    return f"{card[0]} {card[1]}"

def getCardValue(card):
    '''Return the value of the card'''
    faceValues = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return faceValues.index(card[0]) + 1

def swapCards(cards, index1, index2):
    '''Swap the cards at the given indexes'''
    cards[index1], cards[index2] = cards[index2], cards[index1]

def main():
    '''Three card monte game'''
    print("Three Card Monte")
    print("You have to follow the queen")
    print("Press ENTER to continue...")
    input()

    cards = [getRandomCard(), getRandomCard(), getRandomCard()]
    queenIndex = random.randint(0, 2)
    displayCards(cards)
    print("I'm swapping the cards")
    for _ in range(NUM_SWAPS):
        index1, index2 = random.sample([LEFT, MIDDLE, RIGHT], 2)
        swapCards(cards, index1, index2)
        displayCards(cards)
        time.sleep(DELAY)
    print("I have swapped the cards")
    print("Now guess where the queen is")
    print("Enter L for left, M for middle, R for right")
    guess = input("Enter your guess: ").upper()
    if guess == 'L':
        guessIndex = LEFT
    elif guess == 'M':
        guessIndex = MIDDLE
    else:
        guessIndex = RIGHT
    if guessIndex == queenIndex:
        print("You won!")
    else:
        print("You lost!")
    print(f"The queen was at {getCardName(cards[queenIndex])}")

if __main__ == '__main__':
    main()
