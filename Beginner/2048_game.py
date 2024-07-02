'''
How to play 2048 game:
1. The game board is a 4x4 grid.
2. The game starts with two tiles with a value of 2 or 4.
3. When you swipe, all the tiles move in that direction.
4. If two tiles with the same number collide while moving, they will merge into a tile with the sum of their values.
5. The resulting tile cannot merge with another tile again in the same move.
6. The game ends when there are no more moves possible.
7. The player wins when a tile with a value of 2048 appears on the board.
'''

import random

def start_game():
    # Initialize the game board with two random tiles
    board = [[0] * 4 for _ in range(4)]
    board = add_new_tile(board)
    board = add_new_tile(board)
    return board

def add_new_tile(board):
    # Add a new tile (2 or 4) to a random empty cell
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])
    return board

def print_board(board):
    # Print the game board
    for row in board:
        print(' '.join(str(cell).rjust(4) for cell in row))
    print()

def swipe_left(board):
    # Swipe the tiles to the left
    new_board = []
    for row in board:
        new_row = [cell for cell in row if cell != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [cell for cell in new_row if cell != 0]
        new_row += [0] * (4 - len(new_row))
        new_board.append(new_row)
    return new_board

def swipe_right(board):
    # Swipe the tiles to the right
    new_board = [row[::-1] for row in board]
    new_board = swipe_left(new_board)
    new_board = [row[::-1] for row in new_board]
    return new_board

def swipe_up(board):
    # Swipe the tiles up
    new_board = [[board[j][i] for j in range(4)] for i in range(4)]
    new_board = swipe_left(new_board)
    new_board = [[new_board[j][i] for j in range(4)] for i in range(4)]
    return new_board

def swipe_down(board):
    # Swipe the tiles down
    new_board = [[board[j][i] for j in range(4)] for i in range(4)]
    new_board = swipe_right(new_board)
    new_board = [[new_board[j][i] for j in range(4)] for i in range(4)]
    return new_board

def check_game_over(board):
    # Check if the game is over (no more moves possible)
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
    return True

def check_game_win(board):
    # Check if the player wins (2048 tile appears on the board)
    for row in board:
        if 2048 in row:
            return True
    return False

def play_game():
    board = start_game()
    print_board(board)

    while True:
        move = input('Enter a move (W/A/S/D): ').upper()
        if move == 'W':
            board = swipe_up(board)
        elif move == 'A':
            board = swipe_left(board)
        elif move == 'S':
            board = swipe_down(board)
        elif move == 'D':
            board = swipe_right(board)
        else:
            print('Invalid move! Please enter W/A/S/D.')
            continue

        board = add_new_tile(board)
        print_board(board)

        if check_game_win(board):
            print('Congratulations! You win!')
            break

        if check_game_over(board):
            print('Game over! No more moves possible.')
            break

if __name__ == '__main__':
    play_game()
    