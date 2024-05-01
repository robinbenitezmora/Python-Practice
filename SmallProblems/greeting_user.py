
# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase). If the user does not append a !, the computer will print the greeting normally.

name = input('What is your name?\n')

def greetings(name):
    if name[-1] == '!':
        return f'HELLO {name.upper()}. WHY ARE WE YELLING?'
    else:
        return f'Hello {name}.'

print(greetings(name))