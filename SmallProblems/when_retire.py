
# Build a program that displays when the user will retire and how many years she has to work till retirement.

age = int(input('What is your age?\n'))
retire_age = int(input('At what age would you like to retire?\n'))

def retire():
    return f'It is 2024. You will retire in {2024 + retire_age - age}.'

print(retire())