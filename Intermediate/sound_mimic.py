import random, sys, time

try:
    import playsound
except ImportError:
    print("Please install playsound module: pip install playsound")
    print("Exiting...")
    sys.exit()

    input("Press Enter to continue...")

    pattern = ''
    while True:
        print('\n' * 100)
        pattern += random.choice('ASDF')
        print('Pattern:', end=' ')
        for letter in pattern:
            print(letter, end=' ')
            time.sleep(0.5)
            playsound.playsound(f'sounds/{letter}.wav', False)
        time.sleep(1)
        print()
        print('Your turn:')
        guess = input()
        if guess.upper() != pattern:
            print('Game over!')
            break
        time.sleep(1)
        print('Good job!')
        time.sleep(1)
        print('Next round...')
        time.sleep(1)
        print()
        time.sleep(1)
        print('Your turn:')
        guess = input()
        if guess.upper() != pattern:
            print('Game over!')
            break
        time.sleep(1)
        print('Good job!')
        time.sleep(1)
        print('Next round...')
        time.sleep(1)
        print()
        time.sleep(1)