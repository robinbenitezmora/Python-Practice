
# Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number between 20 and 100, inclusive.

from random import randint

def how_old_is_teddy():
    age = randint(20, 100)
    return f'Teddy is {age} years old!'

print(how_old_is_teddy())