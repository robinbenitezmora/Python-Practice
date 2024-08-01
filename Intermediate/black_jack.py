import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'

def main():
    print('''Blackjack
          
          Rules:
          Try to get as close to 21 without going over.
          Kings, Queens, and Jacks are worth 10 points.
          Aces are worth 1 or 11 points.
            Cards 2 through 10 are worth their face value.
            (H)it to take another card.
            (S)tand to stop taking cards.
            On your first play, you can (D)ouble down to increase your bet
            but must hit exactly one more time before standing.
            In case of a tie, the bet is returned to the player.
            The dealer stops hitting at 17.
            ''')
    
    money = 5000
    while True:
        # Set up the round and place initial bets
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        playerBet = takePlayerBet(money)
        print()
        
        # Check if the player has blackjack
        if getHandValue(playerHand) == 21:
            displayHands(playerHand, dealerHand)
            print('Blackjack! You win ${}'.format(playerBet * 1.5))
            money += int(playerBet * 1.5)
            continue
        
        # Player's turn
        while True:
            displayHands(playerHand, dealerHand)
            print()
            print('Money: ${}'.format(money))
            print('Bet: ${}'.format(playerBet))
            move = getPlayerMove(playerHand, money - playerBet)
            if move == 'D':
                playerBet += getPlayerBet(playerBet)
            if move in ('H', 'D'):
                newCard = deck.pop()
                playerHand.append(newCard)
                print('Card: {}'.format(getCardString(newCard)))
                if getHandValue(playerHand) > 21:
                    displayHands(playerHand, dealerHand)
                    print('You busted! You lose ${}'.format(playerBet))
                    money -= playerBet
                    break
            if move in ('S', 'C'):
                break
        
        # Dealer's turn
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                dealerHand.append(deck.pop())
            displayHands(playerHand, dealerHand)
            if getHandValue(dealerHand) > 21:
                print('Dealer busts! You win ${}'.format(playerBet))
                money += playerBet
            elif getHandValue(dealerHand) > getHandValue(playerHand):
                print('Dealer wins! You lose ${}'.format(playerBet))
                money -= playerBet
            elif getHandValue(dealerHand) < getHandValue(playerHand):
                print('You win ${}'.format(playerBet))
                money += playerBet
            else:
                print('It\'s a tie!')
        print()
        
        # Check if the player has run out of money
        if money == 0:
            print('You ran out of money!')
            break
        
        # Ask the player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def takePlayerBet(money):
    while True:
        print('Money: ${}'.format(money))
        print('How much do you want to bet?')
        bet = int(input('> '))
        if 0 < bet <= money:
            return bet
        print('Please enter a bet between 1 and {}'.format(money))

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append(str(rank) + suit)
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append(str(rank) + suit)
    random.shuffle(deck)
    return deck

def getHandValue(cards):
    value = 0
    numberOfAces = 0
    for card in cards:
        rank = card[:-1]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value

def displayHands(playerHand, dealerHand, showDealerHand=False):
    print()
    print('DEALER: ', end='')
    if showDealerHand:
        print(' '.join(getCardString(card) for card in dealerHand))
    else:
        print(getCardString(dealerHand[0]), 'XX')
    print('PLAYER: ', end='')
    print(' '.join(getCardString(card) for card in playerHand))
    print()

def getCardString(card):
    if card == BACKSIDE:
        return 'XX'
    return card

def getPlayerMove(playerHand, money):
    while True:
        print('Do you want to (H)it, (S)tand, (D)ouble down, or (C)heck money?')
        move = input('> ').upper()
        if move in ('H', 'S', 'D', 'C'):
            return move
        print('Please enter H, S, D, or C.')

def getPlayerBet(playerBet):
    while True:
        print('How much more do you want to bet?')
        bet = int(input('> '))
        if 0 < bet <= playerBet:
            return bet
        print('Please enter a bet between 1 and {}'.format(playerBet))

if __name__ == '__main__':
    main()
# What is the output of the following code?
# A) The code will run a blackjack game where the player can place bets and play against the dealer.
# B) The code will display the rules of blackjack but will not run the game.
# C) The code will display an error due to an undefined variable.
# D) The code will display the rules of blackjack and ask the player if they want to play again.
#
# Correct Answer: A) The code will run a blackjack game where the player can place bets and play against the dealer.
#
# Explanation: The code implements a simple blackjack game where the player can place bets and play against the dealer. The main() function sets up the game by initializing the deck, dealing cards to the player and dealer, and handling the player's turn. The player can choose to hit, stand, or double down based on the rules of blackjack. The dealer's turn is then simulated, and the outcome of the game is determined based on the hand values of the player and dealer. The game continues until the player runs out of money or chooses to stop playing.