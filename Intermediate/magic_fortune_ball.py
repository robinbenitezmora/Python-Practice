import random, time

def slowSpacePrint(text, interval=0.1):
    for char in text:
        if char == 'I':
            print('I', end='', flush=True)
        else:
            print(char + ' ', end='', flush=True)
        time.sleep(interval)
    print()
    print()

slowSpacePrint("Ask me a yes/no question and I will tell you your fortune.")
time.sleep(1)
slowSpacePrint("Thinking...")
time.sleep(1)
input('> ')

replies = [
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes - definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy, try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    "Don't count on it.",
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.',
]

slowSpacePrint(random.choice(replies))

slowSpacePrint('I have an answer for you. Do you have another question? (yes/no)')
time.sleep(1)

while True:
    answer = input('> ')
    if answer.lower() == 'yes':
        slowSpacePrint("Ask me a yes/no question and I will tell you your fortune.")
        time.sleep(1)
        slowSpacePrint("Thinking...")
        time.sleep(1)
        input('> ')
        slowSpacePrint(random.choice(replies))
        slowSpacePrint('I have an answer for you. Do you have another question? (yes/no)')
        time.sleep(1)
    else:
        slowSpacePrint("Goodbye!")
        break

# This program is a magic fortune ball that answers yes/no questions. The program displays a message asking the user to ask a yes/no question. The program then displays a "Thinking..." message and waits for the user to press Enter. The program then displays a random answer from the replies list. The program then asks the user if they have another question. If the user answers "yes", the program repeats the process. If the user answers "no", the program displays a goodbye message and exits. The slowSpacePrint() function prints text one character at a time with a delay between each character. This gives the illusion of the text being typed out slowly. The time.sleep() function pauses the program for a specified number of seconds. The random.choice() function selects a random item from a list. The input() function reads a line of input from the user. The while True loop runs indefinitely until the user enters "no" to exit the program. The answer variable stores the user's response to the question "Do you have another question? (yes/no)". The answer.lower() method converts the user's response to lowercase. The break statement exits the loop and ends the program. The slowSpacePrint() function is used to print text one character at a time with a delay between each character. The time.sleep() function is used to pause the program for a specified number of seconds. The random.choice() function is used to select a random item from a list. The input() function is used to read a line of input from the user. The while True loop runs indefinitely until the user enters "no" to exit the program. The answer variable stores the user's response to the question "Do you have another question? (yes/no)". The answer.lower() method converts the user's response to lowercase. The break statement exits the loop and ends the program. The slowSpacePrint() function is used to print text one character at a time with a delay between each character. The time.sleep() function is used to pause the program for a specified number of seconds. The random.choice() function is used to select a random item from a list. The input() function is used to read a line of input from the user. The while True loop runs indefinitely until the user enters "no" to exit the program. The answer variable stores the user's response to the question "Do you have another question? (yes/no)". The answer.lower() method converts the user's response to lowercase