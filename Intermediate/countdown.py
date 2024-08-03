import sys, time
import sevseg

secondsLeft = 30

try:
    while True:
        print('\n' + 60 * ' ' + '\r', end='')
        hours = secondsLeft // 3600
        minutes = (secondsLeft % 3600) // 60
        seconds = secondsLeft % 60

        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()
        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        print(hTopRow + '     ' + mTopRow + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '     ' + mBottomRow + '     ' + sBottomRow)

        if secondsLeft == 0:
            print('\n' + 60 * ' ' + '\r', end='')
            print('Time is up.')
            break

        print('\n\nTime remaining: (H)ours:(M)inutes:(S)econds')
        response = input('> ').lower()

        if response == 'h':
            secondsLeft += 3600
        elif response == 'm':
            secondsLeft += 60
        elif response == 's':
            secondsLeft += 1
        else:
            print('Invalid input. Enter H, M, or S.')

        if secondsLeft < 0:
            secondsLeft = 0

except KeyboardInterrupt:
    print('Countdown, stopped.')
    sys.exit()