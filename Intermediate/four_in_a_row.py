import sys

EMPTY_SPACE = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')
assert len(COLUMN_LABELS) == BOARD_WIDTH

def main():
    print('''Four in a Row,
    The goal of this game is to get four of your pieces in a row horizontally, vertically, or diagonally.
    You will be playing against the computer. The computer is X and you are O.
    ''')
    input('Press Enter to begin...')

    while True:
        gameBoard = getNewBoard()
        currentPlayer, computerPlayer = PLAYER_O, PLAYER_X

        while True:
            drawBoard(gameBoard)
            if currentPlayer == PLAYER_O:
                move = getPlayerMove(gameBoard)
            else:
                move = getComputerMove(gameBoard, computerPlayer)

            gameBoard[move] = currentPlayer
            if isWinner(gameBoard, currentPlayer):
                drawBoard(gameBoard)
                print(currentPlayer + ' has won!')
                break
            elif isBoardFull(gameBoard):
                drawBoard(gameBoard)
                print('The game is a tie!')
                break
            else:
                currentPlayer = PLAYER_X if currentPlayer == PLAYER_O else PLAYER_O

        if not playAgain():
            break

def getNewBoard():
    board = {}
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = EMPTY_SPACE
    return board

def drawBoard(board):
    print()
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            print(board[(x, y)], end=' ')
        print()
    print(' '.join(COLUMN_LABELS))

def getPlayerMove(board):
    while True:
        print('Enter the column to drop your piece (1-7) or QUIT to quit:')
        response = input('> ').upper()
        if response == 'QUIT':
            sys.exit()

        if response not in COLUMN_LABELS:
            continue
        move = int(response) - 1

        if board[(move, 0)] == EMPTY_SPACE:
            for y in range(BOARD_HEIGHT - 1, -1, -1):
                if board[(move, y)] == EMPTY_SPACE:
                    return (move, y)
        else:
            print('That column is full.')

def getComputerMove(board, computerPlayer):
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(x, y)] == EMPTY_SPACE:
                boardCopy = board.copy()
                boardCopy[(x, y)] = computerPlayer
                if isWinner(boardCopy, computerPlayer):
                    return (x, y)

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(x, y)] == EMPTY_SPACE:
                boardCopy = board.copy()
                boardCopy[(x, y)] = PLAYER_O
                if isWinner(boardCopy, PLAYER_O):
                    return (x, y)

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(x, y)] == EMPTY_SPACE:
                return (x, y)
            
def isWinner(board, player):
    for x in range(BOARD_WIDTH - 3):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] == board[(x + 1, y)] == board[(x + 2, y)] == board[(x + 3, y)] == player:
                return True

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT - 3):
            if board[(x, y)] == board[(x, y + 1)] == board[(x, y + 2)] == board[(x, y + 3)] == player:
                return True

    for x in range(BOARD_WIDTH - 3):
        for y in range(BOARD_HEIGHT - 3):
            if board[(x, y)] == board[(x + 1, y + 1)] == board[(x + 2, y + 2)] == board[(x + 3, y + 3)] == player:
                return True

            if board[(x + 3, y)] == board[(x + 2, y + 1)] == board[(x + 1, y + 2)] == board[(x, y + 3)] == player:
                return True

    return False

def isBoardFull(board):
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] == EMPTY_SPACE:
                return False
    return True

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input('> ').lower().startswith('y')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
