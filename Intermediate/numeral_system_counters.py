print('''
This script will count from 1 to 100 in the following numeral systems:
- Binary
- Octal
- Decimal
- Hexadecimal
''')

while True:
    response = input('Would you like to continue? (y/n): ')
    if response.lower() == 'y':
        for i in range(1, 101):
            print(f'Binary: {bin(i)}')
            print(f'Octal: {oct(i)}')
            print(f'Decimal: {i}')
            print(f'Hexadecimal: {hex(i)}')
            print()
    else:
        break
print('Goodbye!')
