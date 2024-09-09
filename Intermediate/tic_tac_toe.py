ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
WINNING_COMBOS = [
    ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
    ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
    ['1', '5', '9'], ['3', '5', '7']
]

def print_board(board):
    '''Print the board'''
    print()
    print(f" {board['1']} | {board['2']} | {board['3']}")
    print("---|---|---")
    print(f" {board['4']} | {board['5']} | {board['6']}")
    print("---|---|---")
    print(f" {board['7']} | {board['8']} | {board['9']}")
    print()

def check_winner(board, player):
    '''Check if the player has won'''
    for combo in WINNING_COMBOS:
        if all(board[space] == player for space in combo):
            return True
    return False

def main():
    '''Tic Tac Toe game'''
    print("Tic Tac Toe")
    print("Player 1 is X and Player 2 is O")
    print("Enter the number where you want to place your mark")
    print("1 is top left and 9 is bottom right")
    print("Press ENTER to continue...")
    input()

    board = {space: ' ' for space in ALL_SPACES}
    player = 'X'
    print_board(board)
    for _ in range(9):
        space = input(f"Player {player}, enter the space: ")
        if space not in ALL_SPACES or board[space] != ' ':
            print("Invalid space. Try again.")
            continue
        board[space] = player
        print_board(board)
        if check_winner(board, player):
            print(f"Player {player} wins!")
            break
        player = 'O' if player == 'X' else 'X'
    else:
        print("It's a tie!")

if __name__ == '__main__':
    main()