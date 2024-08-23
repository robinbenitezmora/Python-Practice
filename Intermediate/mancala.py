import sys

PLAYER_1_PITS = ('A', 'B', 'C', 'D', 'E', 'F')
PLAYER_2_PITS = ('G', 'H', 'I', 'J', 'K', 'L')

OPPOSITE_PIT = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K', 'F': 'L',
                'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D', 'K': 'E', 'L': 'F'}

NEXT_PIT = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1',
            '1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G', 'G': '2',
            '2': 'A'}

PIT_LABELS = ('ABCDEF1LKJIHG2')

STARTING_NUMBER_OF_SEEDS = 4

class Mancala:
    def __init__(self):
        self.board = {pit: 0 for pit in PIT_LABELS}
        for pit in PLAYER_1_PITS:
            self.board[pit] = STARTING_NUMBER_OF_SEEDS
        for pit in PLAYER_2_PITS:
            self.board[pit] = STARTING_NUMBER_OF_SEEDS
        self.board['1'] = 0
        self.board['2'] = 0

    def __str__(self):
        return ' '.join([str(self.board[pit]) for pit in PIT_LABELS])

    def play(self, pit):
        if pit not in PLAYER_1_PITS:
            raise ValueError('Invalid pit')
        if self.board[pit] == 0:
            raise ValueError('Empty pit')
        seeds = self.board[pit]
        self.board[pit] = 0
        while seeds > 0:
            pit = NEXT_PIT[pit]
            self.board[pit] += 1
            seeds -= 1
        if pit == '1' or pit == '2':
            return
        if self.board[pit] == 1 and pit in PLAYER_1_PITS:
            if self.board[OPPOSITE_PIT[pit]] > 0:
                self.board['1'] += self.board[OPPOSITE_PIT[pit]] + 1
                self.board[OPPOSITE_PIT[pit]] = 0
                self.board[pit] = 0
        if self.board[pit] == 1 and pit in PLAYER_2_PITS:
            if self.board[OPPOSITE_PIT[pit]] > 0:
                self.board['2'] += self.board[OPPOSITE_PIT[pit]] + 1
                self.board[OPPOSITE_PIT[pit]] = 0
                self.board[pit] = 0

    def is_game_over(self):
        return all([self.board[pit] == 0 for pit in PLAYER_1_PITS]) or all([self.board[pit] == 0 for pit in PLAYER_2_PITS])

    def winner(self):
        if self.board['1'] > self.board['2']:
            return 1
        if self.board['1'] < self.board['2']:
            return 2
        return 0
    
    def get_board(self):
        return self.board
    
    def get_pit_labels(self):
        return PIT_LABELS
    
    def get_player_1_pits(self):
        return PLAYER_1_PITS
    
    def get_player_2_pits(self):
        return PLAYER_2_PITS
    
    def get_opposite_pit(self):
        return OPPOSITE_PIT
    
    def get_next_pit(self):
        return NEXT_PIT
    
    def get_starting_number_of_seeds(self):
        return STARTING_NUMBER_OF_SEEDS
    
    def get_pit_labels(self):
        return PIT_LABELS
    
    def get_player_1_pits(self):
        return PLAYER_1_PITS
    
    def get_player_2_pits(self):
        return PLAYER_2_PITS
    
    def get_opposite_pit(self):
        return OPPOSITE_PIT
    
    def get_next_pit(self):
        return NEXT_PIT
    
    def get_starting_number_of_seeds(self):
        return STARTING_NUMBER_OF_SEEDS
    
    def get_pit_labels(self):
        return PIT_LABELS
    
    def get_player_1_pits(self):
        return PLAYER_1_PITS
    
    def get_player_2_pits(self):
        return PLAYER_2_PITS
    
    def get_opposite_pit(self):
        return OPPOSITE_PIT
    
    def get_next_pit(self):
        return NEXT_PIT
    
    def get_starting_number_of_seeds(self):
        return STARTING_NUMBER_OF_SEEDS
    
    def get_pit_labels(self):
        return PIT_LABELS
    
    def get_player_1_pits(self):
        return PLAYER_1_PITS
    
    def get_player_2_pits(self):
        return PLAYER_2_PITS
    
    def get_opposite_pit(self):
        return OPPOSITE_PIT
    
    def get_next_pit(self):
        return NEXT_PIT
    
    def get_starting_number_of_seeds(self):
        return STARTING_NUMBER_OF_SEEDS
    
    def get_pit_labels(self):
        return PIT_LABELS
    
    def get_player_1_pits(self):
        return PLAYER_1_PITS
    
    def get_player_2_pits(self):
        return PLAYER_2_PITS
    
    def get_opposite_pit(self):
        return OPPOSITE_PIT
    
    def get_next_pit(self):
        return NEXT_PIT