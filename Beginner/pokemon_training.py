'''
How to play Pokemon training game:
1. Enter your name and choose a Pokemon to train
2. Train your Pokemon by selecting a training method
3. The Pokemon will gain experience points based on the training method
4. The Pokemon will level up after gaining a certain number of experience points
5. The game ends when the Pokemon reaches the maximum level
'''

import random

class Pokemon:
    def __init__(self, name, level=1, exp=0):
        self.name = name
        self.level = level
        self.exp = exp

    def train(self, method):
        if method == 'Battle':
            exp_gained = random.randint(10, 20)
        elif method == 'Training':
            exp_gained = random.randint(5, 10)
        elif method == 'Rest':
            exp_gained = random.randint(1, 5)
        else:
            exp_gained = 0
        self.exp += exp_gained
        print(f'{self.name} gained {exp_gained} experience points from {method} training.')

    def level_up(self):
        if self.exp >= 100:
            self.level += 1
            self.exp -= 100
            print(f'{self.name} leveled up to level {self.level}!')

    def is_max_level(self):
        return self.level >= 10
    
    def __str__(self):
        return f'{self.name} (Level {self.level})'
    
def main():
    name = input('Enter your name:\n')
    pokemon_name = input('Choose a Pokemon to train:\n')
    pokemon = Pokemon(pokemon_name)

    while not pokemon.is_max_level():
        print(f'\n{pokemon}')
        method = input('Select a training method (Battle/Training/Rest):\n')
        pokemon.train(method)
        pokemon.level_up()

    print(f'\nCongratulations! {pokemon.name} has reached the maximum level!')

if __name__ == '__main__':
    main()
