import random, sys 

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you can install by running: pip install bext')
    sys.exit()

BOARD_WIDTH = 16
BOARD_HEIGHT = 14
MOVES_PER_GAME = 20

HEART = chr(9829)
DIAMOND = chr(9830)
SPADE = chr(9824)
CLUB = chr(9827)
BALL = chr(9679)
TRIANGLE = chr(9650)

BLOCK = chr(9608)
LEFTRIGHT = chr(9472)
UPDOWN = chr(9474)
DOWNRIGHT = chr(9484)
DOWNLEFT = chr(9488)
UPRIGHT = chr(9492)
UPLEFT = chr(9496)

TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {
    0: 'red',
    1: 'blue',
    2: 'green',
    3: 'yellow',
    4: 'purple',
    5: 'cyan'
}

COLORS_MODE = 'light'
SHAPES_MAP = {
    0: HEART,
    1: DIAMOND,
    2: SPADE,
    3: CLUB,
    4: BALL,
    5: TRIANGLE
}

SHAPE_MODE = 'solid'

def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print('''Flooder,
          The objective of this game is to fill the board with a single color in as few moves as possible.
          Press Enter to begin...''')
    input()
    response = input('> ').startswith('y')
    if response.upper().starswith('Y'):
        displayMode = SHAPE_MODE
    else:
        displayMode = COLORS_MODE

    game_board = getNewBoard()
    movesLeft = MOVES_PER_GAME

    while True:
        displayBoard(game_board, displayMode)
        print('Moves left:', movesLeft)
        playerMove = askForPlayerMove(displayMode)
        changeTile(playerMove, game_board, 0, 0)
        movesLeft -= 1

        if hasWon(game_board):
            displayBoard(game_board, displayMode)
            print('You have won!')
            break
        elif movesLeft == 0:
            displayBoard(game_board, displayMode)
            print('You have lost!')
            break

        print('Press Enter to continue...')
        input()

def getNewBoard():
    board = []
    for _ in range(BOARD_HEIGHT):
        new_row = []
        for _ in range(BOARD_WIDTH):
            new_row.append(random.choice(TILE_TYPES))
        board.append(new_row)
    return board

def displayBoard(board, mode):
    bext.goto(0, 0)
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if mode == COLORS_MODE:
                bext.fg(COLORS_MAP[board[y][x]])
                print(BLOCK, end='')
            elif mode == SHAPE_MODE:
                bext.fg(COLORS_MAP[board[y][x]])
                print(SHAPES_MAP[board[y][x]], end='')
        print()

def askForPlayerMove(mode):
    while True:
        print('Choose a color to flood the board with:')
        if mode == COLORS_MODE:
            print('R)ed, B)lue, G)reen, Y)ellow, P)urple, C)yan')
        elif mode == SHAPE_MODE:
            print('H)eart, D)iamond, S)pade, C)lub, B)all, T)riangle')
        print('Q)uit')
        response = input('> ').upper()
        if response == 'QUIT':
            sys.exit()
        if response in ('R', 'B', 'G', 'Y', 'P', 'C', 'H', 'D', 'S', 'C', 'B', 'T'):
            return response
        
def changeTile(move, board, x, y):
    if x < 0 or x >= BOARD_WIDTH or y < 0 or y >= BOARD_HEIGHT:
        return
    if board[y][x] == board[0][0]:
        board[y][x] = move
        changeTile(move, board, x + 1, y)
        changeTile(move, board, x - 1, y)
        changeTile(move, board, x, y + 1)
        changeTile(move, board, x, y - 1)

def hasWon(board):
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[y][x] != board[0][0]:
                return False
    return True

if __name__ == '__main__':
    main()    
