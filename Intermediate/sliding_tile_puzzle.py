import random, sys

BLANK = ' '

def print_puzzle(puzzle):
    for row in puzzle:
        print(''.join(row))

def get_blank(puzzle):
    for y, row in enumerate(puzzle):
        for x, cell in enumerate(row):
            if cell == BLANK:
                return x, y
            
def move(puzzle, direction):
    x, y = get_blank(puzzle)
    if direction == 'up':
        if y > 0:
            puzzle[y][x], puzzle[y - 1][x] = puzzle[y - 1][x], puzzle[y][x]
    elif direction == 'down':
        if y < len(puzzle) - 1:
            puzzle[y][x], puzzle[y + 1][x] = puzzle[y + 1][x], puzzle[y][x]
    elif direction == 'left':
        if x > 0:
            puzzle[y][x], puzzle[y][x - 1] = puzzle[y][x - 1], puzzle[y][x]
    elif direction == 'right':
        if x < len(puzzle[0]) - 1:
            puzzle[y][x], puzzle[y][x + 1] = puzzle[y][x + 1], puzzle[y][x]
    return puzzle

def generate_puzzle(size):
    puzzle = [[str(i + 1 + j * size) for i in range(size)] for j in range(size)]
    puzzle[-1][-1] = BLANK
    return puzzle

def is_solved(puzzle):
    return all(puzzle[y][x] == str(1 + x + y * len(puzzle)) for y in range(len(puzzle)) for x in range(len(puzzle[0]))) and puzzle[-1][-1] == BLANK

def shuffle_puzzle(puzzle):
    for _ in range(1000):
        puzzle = move(puzzle, random.choice(['up', 'down', 'left', 'right']))
    return puzzle

def play_puzzle(puzzle):
    print_puzzle(puzzle)
    while not is_solved(puzzle):
        print('Enter a direction (up, down, left, right):')
        direction = input()
        puzzle = move(puzzle, direction)
        print_puzzle(puzzle)
    print('You solved the puzzle!')

if __name__ == '__main__':
    size = 3
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    puzzle = generate_puzzle(size)
    puzzle = shuffle_puzzle(puzzle)
    play_puzzle(puzzle)
    print_puzzle(puzzle)
    print(is_solved(puzzle))
    print_puzzle(generate_puzzle(2))
    print_puzzle(generate_puzzle(3))
    print_puzzle(generate_puzzle(4))
    print_puzzle(generate_puzzle(5))
    print_puzzle(generate_puzzle(6))
    print_puzzle(generate_puzzle(7))
    print_puzzle(generate_puzzle(8))
    print_puzzle(generate_puzzle(9))
    print_puzzle(generate_puzzle(10))
    print_puzzle(generate_puzzle(11))
    print_puzzle(generate_puzzle(12))
    print_puzzle(generate_puzzle(13))
    print_puzzle(generate_puzzle(14))
    print_puzzle(generate_puzzle(15))
    print_puzzle(generate_puzzle(16))
    print_puzzle(generate_puzzle(17))
    print_puzzle(generate_puzzle(18))
    print_puzzle(generate_puzzle(19))
    print_puzzle(generate_puzzle(20))
    print_puzzle(generate_puzzle(21))
    print_puzzle(generate_puzzle(22))
    print_puzzle(generate_puzzle(23))
    print_puzzle(generate_puzzle(24))
    print_puzzle(generate_puzzle(25))
    print_puzzle(generate_puzzle(26))
    print_puzzle(generate_puzzle(27))
    print_puzzle(generate_puzzle(28))
    print_puzzle(generate_puzzle(29))
    print_puzzle(generate_puzzle(30))
    print_puzzle(generate_puzzle(31))
    print_puzzle(generate_puzzle(32))
    print_puzzle(generate_puzzle(33))
    print_puzzle(generate_puzzle(34))
    print_puzzle(generate_puzzle(35))
    print_puzzle(generate_puzzle(36))
    print_puzzle(generate_puzzle(37))
    print_puzzle(generate_puzzle(38))
    print_puzzle(generate_puzzle(39))
    print_puzzle(generate_puzzle(40))
    print_puzzle(generate_puzzle(41))
    print_puzzle(generate_puzzle(42))
    