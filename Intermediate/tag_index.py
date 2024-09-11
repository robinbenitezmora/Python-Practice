import sys

print('You have a 3-gallon bucket and a 5-gallon bucket, and you must measure out exactly 4 gallons of water. How do you do it?')

GOAL = 4
steps = 0

waterInBucket = {'8': 0, '5': 0, '3': 0}

for i in range(1, 100):
    print('8-gallon bucket: %s gallons' % (waterInBucket['8']))
    print('5-gallon bucket: %s gallons' % (waterInBucket['5']))
    print('3-gallon bucket: %s gallons' % (waterInBucket['3']))

    if GOAL in waterInBucket.values():
        print('Congratulations! You measured out %s gallons of water in %s steps!' % (GOAL, steps))
        sys.exit()

    print('Enter the number of the bucket to fill (8, 5, or 3) or pour (f)rom one bucket to another.')
    print('For example, to fill the 8-gallon bucket, type: 8 fill')
    print('To pour from the 5-gallon bucket to the 3-gallon bucket, type: 5 3')
    print('To pour from the 3-gallon bucket to the 8-gallon bucket, type: 3 8')
    print('To quit, type: quit')

    response = input().lower().split()

    if response[0] == 'quit':
        sys.exit()

    if response[1] == 'fill':
        waterInBucket[response[0]] = int(response[0])
    else:
        fromBucket = response[0]
        toBucket = response[1]

        if waterInBucket[fromBucket] == 0:
            print('The %s-gallon bucket is empty.' % (fromBucket))
        elif waterInBucket[toBucket] == int(toBucket):
            print('The %s-gallon bucket is full.' % (toBucket))
        else:
            amountToPour = min(int(toBucket) - waterInBucket[toBucket], waterInBucket[fromBucket])
            waterInBucket[fromBucket] -= amountToPour
            waterInBucket[toBucket] += amountToPour

    steps += 1
    