import random, time

numberOfDice = 2  # Replace with the desired number of dice
numberOfRolls = 1000  # Replace with the desired number of rolls

results = {}
for i in range(numberOfDice, numberOfDice * 6 + 1):
    results[i] = 0

print('Simulating %s dice rolls...' % (numberOfDice * numberOfRolls))
lastPrintTime = time.time()
for i in range(numberOfRolls):
    if time.time() - lastPrintTime > 1:
        print('%s rolls done...' % i)
        lastPrintTime = time.time()
    total = 0
    for j in range(numberOfDice):
        total += random.randint(1, 6)
    results[total] += 1

print('Done. Here are the results:')
for total in range(numberOfDice, numberOfDice * 6 + 1):
    print('%s: %s' % (total, results[total]))
