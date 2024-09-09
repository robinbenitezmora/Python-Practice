import random, sys

BLANK = ''
BOARD_SIZE = 4
WINNING_TILE = 2048
DIRECTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']
TILES = [2, 4]
EMPTY = ' '
SCORE = 'SCORE'
BEST_SCORE = 'BEST_SCORE'
QUIT = 'QUIT'
RESTART = 'RESTART'
HELP = 'HELP'
COMMANDS = [QUIT, RESTART, HELP]
COMMANDS_HELP = {
    QUIT: 'Quit the game',
    RESTART: 'Restart the game',
    HELP: 'Show the help'
}

def main():
    '''2048 game'''
    best_score = 0
    board = [[BLANK] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    add_tile(board)
    add_tile(board)
    print_board(board)
    score = 0
    while True:
        if score > best_score:
            best_score = score
        command = get_command()
        if command == QUIT:
            break
        if command == RESTART:
            board = [[BLANK] * BOARD_SIZE for _ in range(BOARD_SIZE)]
            add_tile(board)
            add_tile(board)
            score = 0
            print_board(board)
            continue
        if command == HELP:
            print_help()
            continue
        moved = move(board, command)
        if not moved:
            print("Invalid move. Try again.")
            continue
        add_tile(board)
        print_board(board)
        score = get_score(board)
        print(f"Score: {score}")
        print(f"Best Score: {best_score}")
        if score == WINNING_TILE:
            print("You win!")
            break
        if is_game_over(board):
            print("Game over!")
            break

def get_command():
    '''Get the command'''
    while True:
        command = input("Enter the command: ").upper()
        if command in COMMANDS:
            return command
        print("Invalid command. Try again.")

def print_help():
    '''Print the help'''
    print("Commands:")
    for command in COMMANDS:
        print(f"{command}: {COMMANDS_HELP[command]}")

def add_tile(board):
    '''Add a tile to the board'''
    empty_tiles = [(row, col) for row in range(BOARD_SIZE) for col in range(BOARD_SIZE) if board[row][col] == BLANK]
    row, col = random.choice(empty_tiles)
    board[row][col] = random.choice(TILES)

def print_board(board):
    '''Print the board'''
    for row in board:
        print(" ".join(str(tile).rjust(4) for tile in row))
    print()

def move(board, direction):
    '''Move the tiles'''
    if direction == 'UP':
        return move_up(board)
    if direction == 'DOWN':
        return move_down(board)
    if direction == 'LEFT':
        return move_left(board)
    if direction == 'RIGHT':
        return move_right(board)
    return False

def move_up(board):
    '''Move the tiles up'''
    moved = False
    for col in range(BOARD_SIZE):
        tiles = [board[row][col] for row in range(BOARD_SIZE) if board[row][col] != BLANK]
        new_tiles = merge_tiles(tiles)
        for row in range(BOARD_SIZE):
            if new_tiles:
                board[row][col] = new_tiles.pop(0)
            else:
                board[row][col] = BLANK
        if tiles != new_tiles:
            moved = True
    return moved

def move_down(board):
    '''Move the tiles down'''
    moved = False
    for col in range(BOARD_SIZE):
        tiles = [board[row][col] for row in range(BOARD_SIZE - 1, -1, -1) if board[row][col] != BLANK]
        new_tiles = merge_tiles(tiles)
        for row in range(BOARD_SIZE - 1, -1, -1):
            if new_tiles:
                board[row][col] = new_tiles.pop(0)
            else:
                board[row][col] = BLANK
        if tiles != new_tiles:
            moved = True
    return moved

def move_left(board):
    '''Move the tiles left'''
    moved = False
    for row in range(BOARD_SIZE):
        tiles = [tile for tile in board[row] if tile != BLANK]
        new_tiles = merge_tiles(tiles)
        for col in range(BOARD_SIZE):
            if new_tiles:
                board[row][col] = new_tiles.pop(0)
            else:
                board[row][col] = BLANK
        if tiles != new_tiles:
            moved = True
    return moved

def move_right(board):
    '''Move the tiles right'''
    moved = False
    for row in range(BOARD_SIZE):
        tiles = [tile for tile in board[row][::-1] if tile != BLANK]
        new_tiles = merge_tiles(tiles)
        for col in range(BOARD_SIZE - 1, -1, -1):
            if new_tiles:
                board[row][col] = new_tiles.pop(0)
            else:
                board[row][col] = BLANK
        if tiles != new_tiles:
            moved = True
    return moved

def merge_tiles(tiles):
    '''Merge the tiles'''
    new_tiles = []
    while tiles:
        if len(tiles) == 1:
            new_tiles.append(tiles.pop(0))
        elif tiles[0] == tiles[1]:
            new_tiles.append(tiles.pop(0) * 2)
        else:
            new_tiles.append(tiles.pop(0))
    return new_tiles

def get_score(board):
    '''Get the score'''
    return max(max(row) for row in board)

def is_game_over(board):
    '''Check if the game is over'''
    for direction in DIRECTIONS:
        if move(copy_board(board), direction):
            return False
    return True

def copy_board(board):
    '''Copy the board'''
    return [row.copy() for row in board]

if __name__ == '__main__':
    main()
    