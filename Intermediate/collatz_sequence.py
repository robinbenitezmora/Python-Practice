import sys, time

print('''Collatz Sequence Simulator
Enter a number and see the Collatz sequence.
The Collatz sequence will always end at 1.''')

print('Enter a number:')
response = input('> ')
if not response.isdecimal() or response == '0':
    print('Please enter a positive number.')
    sys.exit()

number = int(response)
print(number, end='', flush=True)
while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(', ' + str(number), end='', flush=True)
    time.sleep(0.1)
print()

sys.exit()
