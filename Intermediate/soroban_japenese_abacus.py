NUMBER_OF_DIGITS = 10

def main ():
    print ("Soroban Japanese Abacus")
    print ("=======================")
    print ("This program will add two numbers using the soroban Japanese abacus.")
    print ()

    abacusNumber = 0

    while True:
        displayAbacus(abacusNumber)
        displayControls()

        command = input ("Enter command: ")
        if command == "q":
            break
        elif command == "r":
            abacusNumber = 0
        elif command.isdecimal():
            abacusNumber = int(command)
        else:
            for letter in command:
                if letter == 'q':
                    abacusNumber += 1000000000
                elif letter == 'a':
                    abacusNumber += 1000000000
                elif letter == 'w':
                    abacusNumber += 100000000
                elif letter == 's':
                    abacusNumber += 100000000
                elif letter == 'e':
                    abacusNumber += 10000000
                elif letter == 'd':
                    abacusNumber += 10000000
                elif letter == 'r':
                    abacusNumber += 1000000
                elif letter == 'f':
                    abacusNumber += 1000000
                elif letter == 't':
                    abacusNumber += 100000
                elif letter == 'g':
                    abacusNumber += 100000
                elif letter == 'y':
                    abacusNumber += 10000
                elif letter == 'h':
                    abacusNumber += 10000
                elif letter == 'u':
                    abacusNumber += 1000
                elif letter == 'j':
                    abacusNumber += 1000
                elif letter == 'i':
                    abacusNumber += 100
                elif letter == 'k':
                    abacusNumber += 100
                elif letter == 'o':
                    abacusNumber += 10
                elif letter == 'l':
                    abacusNumber += 10
                elif letter == 'p':
                    abacusNumber += 1
                elif letter == ';':
                    abacusNumber -= 1

            if abacusNumber < 0:
                abacusNumber = 0

            if abacusNumber > 9999999999:
                abacusNumber = 9999999999

def displayAbacus (abacusNumber):
    numberList = list(str(abacusNumber).zfill(NUMBER_OF_DIGITS))

    hasBead = []

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] == '01234')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] == '56789')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] == '0123456789')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] == '234789')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] == '034589')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] == '014569')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] == '0124567')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] == '01235678')

    abacusChar = []

    for i, beadPresent in enumerate(hasBead):
        if i beadPresent:
            abacusChar.append('O')
        else:
            abacusChar.append('|')

    chars = abacusChar + numberList

    print('''
    +------------------+
    | 9 8 7 6 5 4 3 2 1 0
    |------------------|
    | {0} {1} {2} {3} {4} {5} {6} {7} {8} {9}
    +------------------+
    '''.format(*chars))

def displayControls ():
    print ('''
    Controls:
    q: Quit
    r: Reset
    a: Add 1,000,000,000
    w: Subtract 1,000,000,000
    s: Add 100,000,000
    e: Subtract 100,000,000
    d: Add 10,000,000
    f: Subtract 10,000,000
    t: Add 1,000,000
    g: Subtract 1,000,000
    y: Add 100,000
    h: Subtract 100,000
    u: Add 10,000
    j: Subtract 10,000
    i: Add 1,000
    k: Subtract 1,000
    o: Add 100
    l: Subtract 100
    p: Add 10
    ;: Subtract 10
    ''')

if __name__ == "__main__":
    main()
