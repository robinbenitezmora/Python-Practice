import sys

print('''Fibonacci Sequence,
      The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
        ''')
print('Press Enter to begin...')
input()

while True:
    print('Enter the number of terms you want to generate or press QUIT to quit:')
    response = input('> ').upper()
    if response == 'QUIT':
        sys.exit()

    if not response.isdecimal() and int(response) > 0:
        continue
    terms = int(response)

    a, b = 0, 1
    sequence = [a, b]

    for i in range(terms - 2):
        a, b = b, a + b
        sequence.append(b)

    print('The first', terms, 'terms of the Fibonacci sequence are:')
    for term in sequence:
        print(term)
    print()
    print('Press Enter to continue...')
    input()
    print()
    