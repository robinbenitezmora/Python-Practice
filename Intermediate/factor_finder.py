import math, sys

print('''
Factor Finder,
press Ctrl-C to quit...
''')

while True:
    print('Enter a number to find its factors or press QUIT to quit:')
    response = input('> ').upper()
    if response == 'QUIT':
        sys.exit()

    if not response.isdecimal() and int(response) > 0:
        continue
    number = int(response)

    factors = []

    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)

    factors = list(set(factors))
    factors.sort()
    print('Factors of', number, 'are:')
    for factor in factors:
        print(factor)
    print()
    print('Press Enter to continue...')
    input()
    print()
