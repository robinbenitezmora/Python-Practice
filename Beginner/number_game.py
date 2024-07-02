def nearestMultiple(num):
    if num > 4:
        near = num + (4 - num % 4)
    else:
        near = 4
    return near

def lose1():
    print("You lose! You have to drink 1 shot of beer.")
    print("Better luck next time!")
    exit(0)

def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False
        i += 1
    return True

def start1():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the first turn.")
        print("Enter 'S' to take the second turn.")
        print("Enter 'Q' to quit the game.")
        turn = input('> ')

        if turn == 'Q':
            print("You quit the game.")
            print("Better luck next time!")
            exit(0)
        elif turn == 'F':
            print("You took the first turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            xyz.append(num)
            last = num
            break
        elif turn == 'S':
            print("You took the second turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            xyz.append(num)
            last = num
            break
        else:
            print("Invalid input.")
            continue

    while True:
        print("Enter 'F' to take the first turn.")
        print("Enter 'S' to take the second turn.")
        print("Enter 'Q' to quit the game.")
        turn = input('> ')

        if turn == 'Q':
            print("You quit the game.")
            print("Better luck next time!")
            exit(0)
        elif turn == 'F':
            print("You took the first turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            if num <= last:
                print("Enter a number greater than", last)
                continue
            xyz.append(num)
            last = num
            if check(xyz):
                lose1()
            continue
        elif turn == 'S':
            print("You took the second turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            if num <= last:
                print("Enter a number greater than", last)
                continue
            xyz.append(num)
            last = num
            if check(xyz):
                lose1()
            continue
        else:
            print("Invalid input.")
            continue

def start2():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the first turn.")
        print("Enter 'S' to take the second turn.")
        print("Enter 'Q' to quit the game.")
        turn = input('> ')

        if turn == 'Q':
            print("You quit the game.")
            print("Better luck next time!")
            exit(0)
        elif turn == 'F':
            print("You took the first turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            xyz.append(num)
            last = num
            break
        elif turn == 'S':
            print("You took the second turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            xyz.append(num)
            last = num
            break
        else:
            print("Invalid input.")
            continue

    while True:
        print("Enter 'F' to take the first turn.")
        print("Enter 'S' to take the second turn.")
        print("Enter 'Q' to quit the game.")
        turn = input('> ')

        if turn == 'Q':
            print("You quit the game.")
            print("Better luck next time!")
            exit(0)
        elif turn == 'F':
            print("You took the first turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            if num <= last:
                print("Enter a number greater than", last)
                continue
            xyz.append(num)
            last = num
            if check(xyz):
                lose1()
            continue
        elif turn == 'S':
            print("You took the second turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue

            if num <= last:
                print("Enter a number greater than", last)
                continue
            xyz.append(num)
            last = num
            if check(xyz):
                lose1()
            continue
        else:
            print("Invalid input.")
            continue

def start3():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the first turn.")
        print("Enter 'S' to take the second turn.")
        print("Enter 'Q' to quit the game.")
        turn = input('> ')

        if turn == 'Q':
            print("You quit the game.")
            print("Better luck next time!")
            exit(0)
        elif turn == 'F':
            print("You took the first turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            xyz.append(num)
            last = num
            break
        elif turn == 'S':
            print("You took the second turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            xyz.append(num)
            last = num
            break
        else:
            print("Invalid input.")
            continue

    while True:
        print("Enter 'F' to take the first turn.")
        print("Enter 'S' to take the second turn.")
        print("Enter 'Q' to quit the game.")
        turn = input('> ')

        if turn == 'Q':
            print("You quit the game.")
            print("Better luck next time!")
            exit(0)
        elif turn == 'F':
            print("You took the first turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            if num <= last:
                print("Enter a number greater than", last)
                continue
            xyz.append(num)
            last = num
            if check(xyz):
                lose1()
            continue
        elif turn == 'S':
            print("You took the second turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            if num <= last:
                print("Enter a number greater than", last)
                continue
            xyz.append(num)
            last = num
            if check(xyz):
                lose1()
            continue
        else:
            print("Invalid input.")
            continue

def start4():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the first turn.")
        print("Enter 'S' to take the second turn.")
        print("Enter 'Q' to quit the game.")
        turn = input('> ')

        if turn == 'Q':
            print("You quit the game.")
            print("Better luck next time!")
            exit(0)
        elif turn == 'F':
            print("You took the first turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            xyz.append(num)
            last = num
            break
        elif turn == 'S':
            print("You took the second turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            xyz.append(num)
            last = num
            break
        else:
            print("Invalid input.")
            continue

    while True:
        print("Enter 'F' to take the first turn.")
        print("Enter 'S' to take the second turn.")
        print("Enter 'Q' to quit the game.")
        turn = input('> ')

        if turn == 'Q':
            print("You quit the game.")
            print("Better luck next time!")
            exit(0)
        elif turn == 'F':
            print("You took the first turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            if num <= last:
                print("Enter a number greater than", last)
                continue
            xyz.append(num)
            last = num
            if check(xyz):
                lose1()
            continue
        elif turn == 'S':
            print("You took the second turn.")
            print("Enter a number between 1 and 100.")
            num = int(input('> '))
            if num < 1 or num > 100:
                print("Enter a number between 1 and 100.")
                continue
            if num <= last:
                print("Enter a number greater than", last)
                continue
            xyz.append(num)
            last = num
            if check(xyz):
                lose1()
            continue

        else:
            print("Invalid input.")
            continue
