'''
The Royal Game of Ur is an ancient game that was played in Mesopotamia in the 3rd millennium BC. The game is played on a board with two players. Each player has 7 pieces that they need to move from one end of the board to the other. The game is played with 4 tetrahedral dice that have two sides marked with a dot and two sides marked with a line. The dice are rolled to determine the number of spaces a player can move their piece. The game is won by the player who moves all their pieces to the other end of the board first.

To write a Royal Game of Ur in Python, here are the steps we'll need to take:

1. Create a board with 14 spaces for each player.
2. Create 4 tetrahedral dice with 2 sides marked with a dot and 2 sides marked with a line.
3. Create 7 pieces for each player.
4. Roll the dice to determine the number of spaces a player can move their piece.
5. Move the player's piece on the board.
6. Check if the player has won the game.
'''

import random, sys

X_PLAYER = 'X'
O_PLAYER = 'O'
EMPTY = ' '

X_HOME = 'x_home'
O_HOME = 'o_home'
X_GOAL = 'x_goal'
O_GOAL = 'o_goal'

ALL_SPACES = 'hgfetsijklmnopdcbarq'
X_TRACK = 'HefghijklmnopstG'
O_TRACK = 'HabcdefgijklmnopqrG'

FLOWER_SPACES = ('h', 't', 'l', 'd', 'r')

BOARD_TEMPLATE = '''
                   {}            {}
                   Home         Goal
                     v            ^
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
'''

def print_board(board):
    print(BOARD_TEMPLATE.format(
        board[X_HOME], board['h'], board['g'], board['f'], board['e'], board['s'], board['i'], board['j'], board['k'], board['l'], board['m'], board['n'], board['o'], board['p'],
        board['t'], board['d'], board['c'], board['b'], board['a'], board['r'], board['q'], board[O_HOME]
    ))

def roll_dice():
    return random.choices(['.', '.', '|', '|'], k=4)

def move_piece(board, player, piece, spaces):
    if player == X_PLAYER:
        track = X_TRACK
        home = X_HOME
        goal = X_GOAL
    else:
        track = O_TRACK
        home = O_HOME
        goal = O_GOAL

    if piece in board[home]:
        if spaces[0] == '.':
            board[home] = board[home].replace(piece, '', 1)
            board[track[0]] += piece
        elif spaces[0] == '|':
            board[home] = board[home].replace(piece, '', 1)
            board[goal] += piece
        else:
            return False
    elif piece in board[goal]:
        if spaces[0] == '.':
            board[goal] = board[goal].replace(piece, '', 1)
            board[track[0]] += piece
        else:
            return False
    else:
        current_space = track.index(piece)
        next_space = current_space + spaces.count('|') - spaces.count('.')
        if next_space >= len(track):
            return False
        if track[next_space] in board[X_TRACK] or track[next_space] in board[O_TRACK]:
            return False
        board[track[current_space]] = board[track[current_space]].replace(piece, '', 1)
        board[track[next_space]] += piece
    return True

def check_win(board, player):
    if player == X_PLAYER:
        return not board[X_HOME] and not board[X_TRACK]
    else:
        return not board[O_HOME] and not board[O_TRACK]
    
def main():
    board = {
        X_HOME: 'XXXXXXX',
        O_HOME: 'OOOOOOO',
        X_GOAL: '',
        O_GOAL: '',
        X_TRACK: '',
        O_TRACK: '',
        'h': ' ', 'g': ' ', 'f': ' ', 'e': ' ', 's': ' ', 'i': ' ', 'j': ' ', 'k': ' ', 'l': ' ', 'm': ' ', 'n': ' ', 'o': ' ', 'p': ' ', 't': ' ', 'd': ' ', 'c': ' ', 'b': ' ', 'a': ' ', 'r': ' ', 'q': ' '
    }
    player = X_PLAYER
    print_board(board)
    while True:
        print(f'{player}\'s turn')
        input('Press Enter to roll the dice')
        dice = roll_dice()
        print(f'Dice: {dice}')
        for d in dice:
            if not board[X_TRACK] and not board[O_TRACK]:
                print('Game Over')
                sys.exit()
            if not board[X_TRACK]:
                player = O_PLAYER
                break
            if not board[O_TRACK]:
                player = X_PLAYER
                break
            if not move_piece(board, player, board[X_TRACK][0], dice):
                print('Invalid move')
                break
            print_board(board)
            if check_win(board, player):
                print(f'{player} wins')
                sys.exit()
        player = O_PLAYER if player == X_PLAYER else X_PLAYER

if __name__ == '__main__':
    main()
    