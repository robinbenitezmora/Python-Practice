import sys, time
import sevseg

try:
    while True:
        print('\n' * 60)
        currentTime = time.localtime()
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)

        print(hTopRow + '     ' + mTopRow + '     ' + sDigits.splitlines()[0])
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sDigits.splitlines()[1])
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sDigits.splitlines()[2])
        print('     ' + '***' + '     ' + sDigits.splitlines()[3])
        print('Press Ctrl-C to quit.')

        time.sleep(1)
except KeyboardInterrupt:
    print('Digital Clock, stopped.')
    sys.exit()

# The Digital Clock program is a simple program that displays the current time in a digital clock format. The program uses the sevseg module to generate the seven-segment display for the hours, minutes, and seconds. The program then prints the seven-segment display for each time component and updates the display every second. The user can press Ctrl-C to quit the program.