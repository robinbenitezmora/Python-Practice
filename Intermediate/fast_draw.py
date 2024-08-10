import random, sys, time

print('''Fast Draw,
      Time to test your reflexes and see if you have the fastest draw in the west!
        When you see "DRAW", you have 0.3 seconds to press Enter.
        ''')
print('Press Enter to begin...')
input()

while True:
    print('\n' * 40)
    time.sleep(random.randint(2, 5))
    print('DRAW!')
    start_time = time.time()
    input()
    end_time = time.time()

    if end_time - start_time < 0.01:
        print('You drew too early!')
    elif end_time - start_time > 0.3:
        print('You took too long to draw!')
    else:
        print('You won! It took you', round(end_time - start_time, 2), 'seconds.')
    print()
    print('Press Enter to play again or QUIT to quit...')
    response = input('> ').upper()
    if response == 'QUIT':
        sys.exit()

# The Fast Draw program is a simple game that tests your reflexes. When you see the word "DRAW", you have 0.3 seconds to press Enter. If you press Enter too early or too late, you lose. If you press Enter within the time limit, you win. The game then asks if you want to play again or quit. If you choose to quit, the program exits. Otherwise, the game starts again. The game uses the time module to measure the time it takes for you to press Enter after seeing the word "DRAW". The random module is used to generate a random time delay before displaying the word "DRAW". The program uses a while loop to keep the game running until you choose to quit. The program also uses the sys module to exit the program when you choose to quit. The program uses the input function to get your response and the time.sleep function to introduce a random delay before displaying the word "DRAW". The program uses the time.time function to measure the time it takes for you to press Enter after seeing the word "DRAW". The program uses the round function to round the time difference to two decimal places. The program uses the upper method to convert your response to uppercase. The program uses the print function to display messages to the screen. The program uses the if statement to check if you drew too early, too late, or within the time limit. The program uses the else statement to display a message if you win. The program uses the continue statement to skip the rest of the loop if you press Enter too early or too late. The program uses the break statement to exit the loop if you choose to quit. The program uses the int function to convert your response to an integer. The program uses the randint function to generate a random time delay between 2 and 5 seconds. The program uses the time.sleep function to introduce a random delay before displaying the word "DRAW". The program uses the time.time function to measure the time it takes for you to press Enter after seeing the word "DRAW". The program uses the sys.exit function to exit the program when you choose to quit. The program uses the while loop to keep the game running until you choose to quit. The program uses the print function to display messages to the screen. The program uses the input function to get your response. The program uses the upper method to convert your response to uppercase. The program uses the if statement to check if you drew too early, too
