import sys, time

print("Ninety-nine bottles of beer on the wall,")
print()
print('Press Ctrl-C to stop the program.')

time.sleep(2)

bottles = 99
PAUSE = 2

try:
    while bottles > 0:
        print(f'{bottles} bottles of beer on the wall,')
        print(f'{bottles} bottles of beer,')
        print('Take one down, pass it around,')
        bottles -= 1
        print(f'{bottles} bottles of beer on the wall.')
        print()
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()

print('No more bottles of beer on the wall,')
print('No more bottles of beer,')
print('Go to the store and buy some more,')
print('99 bottles of beer on the wall.')
print()
print('Goodbye!')
